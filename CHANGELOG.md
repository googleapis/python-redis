# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-redis/#history

## [1.0.2](https://github.com/googleapis/python-redis/compare/v1.0.1...v1.0.2) (2022-06-08)


### Bug Fixes

* **deps:** require protobuf<4.0.0 on v1 branch ([#200](https://github.com/googleapis/python-redis/issues/200)) ([9285d25](https://github.com/googleapis/python-redis/commit/9285d25b9b909e45df8bacb6520b2f07297a00a0))

### [1.0.1](https://github.com/googleapis/python-redis/compare/v1.0.0...v1.0.1) (2022-03-25)


### Bug Fixes

* **deps:** require google-api-core >= 1.31.5, >= 2.3.2 on v1 release ([#171](https://github.com/googleapis/python-redis/issues/171)) ([9cc282b](https://github.com/googleapis/python-redis/commit/9cc282bde9f1b9f770bb898f43ff2f73f2a04974))

## [1.0.0](https://www.github.com/googleapis/python-redis/compare/v0.4.0...v1.0.0) (2020-05-12)


### Features

* set release_status to production/stable ([#11](https://www.github.com/googleapis/python-redis/issues/11)) ([effc368](https://www.github.com/googleapis/python-redis/commit/effc368f6904cb6321ec9a8100460a0df36132ab))

## [0.4.0](https://www.github.com/googleapis/python-redis/compare/v0.3.0...v0.4.0) (2020-02-12)


### Features

* **redis:** undeprecate resource name helper methods, add 2.7 deprecation warning (via synth) ([#10049](https://www.github.com/googleapis/python-redis/issues/10049)) ([b8a8c24](https://www.github.com/googleapis/python-redis/commit/b8a8c242c3f8f91b4615190006f5a2da720c8f40))
* add ConnectMode and upgrade_instance ([#5](https://www.github.com/googleapis/python-redis/issues/5)) ([e55220b](https://www.github.com/googleapis/python-redis/commit/e55220b5c189bc96589abac492a490d1d99b53ff))


### Bug Fixes

* **redis:** deprecate resource name helper methods (via synth) ([#9840](https://www.github.com/googleapis/python-redis/issues/9840)) ([75342ef](https://www.github.com/googleapis/python-redis/commit/75342ef43750ec5709694ac39306e5747e01fcdc))

## 0.3.0

07-24-2019 17:15 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8400](https://github.com/googleapis/google-cloud-python/pull/8400))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Remove unused message exports. ([#7272](https://github.com/googleapis/google-cloud-python/pull/7272))
- Protoc-generated serialization update. ([#7092](https://github.com/googleapis/google-cloud-python/pull/7092))
- Pick up stub docstring fix in GAPIC generator. ([#6979](https://github.com/googleapis/google-cloud-python/pull/6979))

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8519](https://github.com/googleapis/google-cloud-python/pull/8519))
- Add 'import_instance' / 'export_instance' support (via synth). ([#8220](https://github.com/googleapis/google-cloud-python/pull/8220))
- Remove v1 'import_instance' / 'export_instance'; add v1beta1 'failover_instance' (via synth). ([#7937](https://github.com/googleapis/google-cloud-python/pull/7937))
- Add support for instance import / export / failover (via synth). ([#7423](https://github.com/googleapis/google-cloud-python/pull/7423))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Pin black version (via synth). ([#8592](https://github.com/googleapis/google-cloud-python/pull/8592))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Update year: 2018 -> 2019. ([#7154](https://github.com/googleapis/google-cloud-python/pull/7154))

### Internal / Testing Changes
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8360](https://github.com/googleapis/google-cloud-python/pull/8360))
- Add disclaimer to auto-generated template files (via synth).  ([#8324](https://github.com/googleapis/google-cloud-python/pull/8324))
- Suppress checking 'cov-fail-under' in nox default session (via synth). ([#8249](https://github.com/googleapis/google-cloud-python/pull/8249))
- Fix coverage in 'types.py' (via synth). ([#8161](https://github.com/googleapis/google-cloud-python/pull/8161))
- Blacken noxfile.py, setup.py (via synth). ([#8129](https://github.com/googleapis/google-cloud-python/pull/8129))
- Add empty lines (via synth). ([#8068](https://github.com/googleapis/google-cloud-python/pull/8068))
- Finsh setup for 'docs' session in nox. ([#8101](https://github.com/googleapis/google-cloud-python/pull/8101))
- Use alabaster theme everwhere. ([#8021](https://github.com/googleapis/google-cloud-python/pull/8021))
- Copy lintified proto files (via synth).
- Add clarifying comment to blacken nox target. ([#7400](https://github.com/googleapis/google-cloud-python/pull/7400))
- Copy proto files alongside protoc versions.
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))

## 0.2.1

12-18-2018 09:40 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAPIC generator. ([#6504](https://github.com/googleapis/google-cloud-python/pull/6504))
- Assorted synth fixups / cleanups ([#6400](https://github.com/googleapis/google-cloud-python/pull/6400))
- Fix `client_info` bug, update docstrings. ([#6419](https://github.com/googleapis/google-cloud-python/pull/6419))
- Re-generate library using redis/synth.py ([#6016](https://github.com/googleapis/google-cloud-python/pull/6016))
- Re-generate library using redis/synth.py ([#5993](https://github.com/googleapis/google-cloud-python/pull/5993))

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))

### Internal / Testing Changes
- Add baseline for synth.metadata
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Don't synth 'README.rst'. ([#6262](https://github.com/googleapis/google-cloud-python/pull/6262))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))

## 0.2.0

### New Features

- Add the v1 API client library. ([#5945](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5945))

### Documentation

- Docs: Replace links to '/stable/' with '/latest/'. ([#5901](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5901))
- Redis: Fix README.md links ([#5745](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5745))
- Add redis documentation to main index.rst ([#5405](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5405))

### Internal / Testing Changes

- Nox: use inplace installs ([#5865](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5865))
- Avoid overwriting '__module__' of messages from shared modules. ([#5364](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5364))
- Unit tests require grpcio. ([#5363](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5363))

## 0.1.0

### New Features
Initial version of Redis client library v1beta1.
