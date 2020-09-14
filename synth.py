# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import logging

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()
excludes = ["README.rst", "setup.py", "nox*.py", "docs/conf.py", "docs/index.rst"]

# ----------------------------------------------------------------------------
# Generate redis GAPIC layer
# ----------------------------------------------------------------------------
for version in ["v1beta1", "v1"]:
    library = gapic.py_library(
        service="redis",
        version=version,
        bazel_target=f"//google/cloud/redis/{version}:redis-{version}-py",
        include_protos=True,
    )

    s.copy(library, excludes=excludes)

s.replace(
    "google/cloud/**/*client.py",
    "from collections import OrderedDict",
    r"""import builtins
from collections import OrderedDict"""
)
s.replace(
    "google/cloud/**/*client.py",
    "any\(",
    "builtins.any(",
)

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(
    samples=False,
    microgenerator=True,
)
s.move(templated_files, excludes=[".coveragerc"])  # microgenerator has a good .coveragerc file

s.replace("noxfile.py", '[\"\']-W[\"\']', '# "-W"')

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
