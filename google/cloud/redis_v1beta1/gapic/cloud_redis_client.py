# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.redis.v1beta1 CloudRedis API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.redis_v1beta1.gapic import cloud_redis_client_config
from google.cloud.redis_v1beta1.gapic import enums
from google.cloud.redis_v1beta1.gapic.transports import cloud_redis_grpc_transport
from google.cloud.redis_v1beta1.proto import cloud_redis_pb2
from google.cloud.redis_v1beta1.proto import cloud_redis_pb2_grpc
from google.longrunning import operations_pb2
from google.protobuf import any_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-redis").version


class CloudRedisClient(object):
    """
    Input and output type names. These are resolved in the same way as
    FieldDescriptorProto.type_name, but must refer to a message type.
    """

    SERVICE_ADDRESS = "redis.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.redis.v1beta1.CloudRedis"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudRedisClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def instance_path(cls, project, location, instance):
        """Return a fully-qualified instance string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/instances/{instance}",
            project=project,
            location=location,
            instance=instance,
        )

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.CloudRedisGrpcTransport,
                    Callable[[~.Credentials, type], ~.CloudRedisGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = cloud_redis_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=cloud_redis_grpc_transport.CloudRedisGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = cloud_redis_grpc_transport.CloudRedisGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_instances(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        An annotation that describes a resource reference, see
        ``ResourceReference``.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_instances(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_instances(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): For extensions, this is the name of the type being extended. It is
                resolved in the same manner as type_name.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.redis_v1beta1.types.Instance` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_instances" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_instances"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_instances,
                default_retry=self._method_configs["ListInstances"].retry,
                default_timeout=self._method_configs["ListInstances"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.ListInstancesRequest(
            parent=parent, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_instances"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="instances",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_instance(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets the details of a specific Redis instance.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> name = client.instance_path('[PROJECT]', '[LOCATION]', '[INSTANCE]')
            >>>
            >>> response = client.get_instance(name)

        Args:
            name (str): If set, all the classes from the .proto file are wrapped in a single
                outer class with the given name. This applies to both Proto1 (equivalent
                to the old "--one_java_file" option) and Proto2 (where a .proto always
                translates to a single class, but you may want to explicitly choose the
                class name).
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types.Instance` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_instance,
                default_retry=self._method_configs["GetInstance"].retry,
                default_timeout=self._method_configs["GetInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.GetInstanceRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_instance(
        self,
        parent,
        instance_id,
        instance,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If type_name is set, this need not be set. If both this and
        type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or
        TYPE_GROUP.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>> from google.cloud.redis_v1beta1 import enums
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>> instance_id = 'test_instance'
            >>> tier = enums.Instance.Tier.BASIC
            >>> memory_size_gb = 1
            >>> instance = {'tier': tier, 'memory_size_gb': memory_size_gb}
            >>>
            >>> response = client.create_instance(parent, instance_id, instance)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): Required. The resource name of the instance location using the form:
                ``projects/{project_id}/locations/{location_id}`` where ``location_id``
                refers to a GCP region.
            instance_id (str): STANDARD_HA tier: highly available primary/replica instances
            instance (Union[dict, ~google.cloud.redis_v1beta1.types.Instance]): Lists all Redis instances owned by a project in either the specified
                location (region) or all locations.

                The location should have the following format:

                -  ``projects/{project_id}/locations/{location_id}``

                If ``location_id`` is specified as ``-`` (wildcard), then all regions
                available to the project are queried, and the results are aggregated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.redis_v1beta1.types.Instance`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_instance,
                default_retry=self._method_configs["CreateInstance"].retry,
                default_timeout=self._method_configs["CreateInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.CreateInstanceRequest(
            parent=parent, instance_id=instance_id, instance=instance
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["create_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            cloud_redis_pb2.Instance,
            metadata_type=any_pb2.Any,
        )

    def update_instance(
        self,
        update_mask,
        instance,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates the metadata and configuration of a specific Redis instance.

        Completed longrunning.Operation will contain the new instance object
        in the response field. The returned operation is automatically deleted
        after a few hours, so there is no need to call DeleteOperation.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> paths_element = 'display_name'
            >>> paths_element_2 = 'memory_size_gb'
            >>> paths = [paths_element, paths_element_2]
            >>> update_mask = {'paths': paths}
            >>> display_name = 'UpdatedDisplayName'
            >>> name = 'projects/<project-name>/locations/<location>/instances/<instance>'
            >>> memory_size_gb = 4
            >>> instance = {'display_name': display_name, 'name': name, 'memory_size_gb': memory_size_gb}
            >>>
            >>> response = client.update_instance(update_mask, instance)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            update_mask (Union[dict, ~google.cloud.redis_v1beta1.types.FieldMask]): JSON name of this field. The value is set by protocol compiler. If
                the user has set a "json_name" option on this field, that option's value
                will be used. Otherwise, it's deduced from the field's name by
                converting it to camelCase.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.redis_v1beta1.types.FieldMask`
            instance (Union[dict, ~google.cloud.redis_v1beta1.types.Instance]): The name of the uninterpreted option. Each string represents a
                segment in a dot-separated name. is_extension is true iff a segment
                represents an extension (denoted with parentheses in options specs in
                .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false]
                } represents "foo.(bar.baz).qux".

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.redis_v1beta1.types.Instance`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_instance,
                default_retry=self._method_configs["UpdateInstance"].retry,
                default_timeout=self._method_configs["UpdateInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.UpdateInstanceRequest(
            update_mask=update_mask, instance=instance
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("instance.name", instance.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["update_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            cloud_redis_pb2.Instance,
            metadata_type=any_pb2.Any,
        )

    def import_instance(
        self,
        name,
        input_config,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.

        Redis may stop serving during this operation. Instance state will be
        IMPORTING for entire operation. When complete, the instance will contain
        only data from the imported file.

        The returned operation is automatically deleted after a few hours, so
        there is no need to call DeleteOperation.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> # TODO: Initialize `input_config`:
            >>> input_config = {}
            >>>
            >>> response = client.import_instance(name, input_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): See ``HttpRule``.
            input_config (Union[dict, ~google.cloud.redis_v1beta1.types.InputConfig]): Required. Specify data to be imported.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.redis_v1beta1.types.InputConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "import_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "import_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.import_instance,
                default_retry=self._method_configs["ImportInstance"].retry,
                default_timeout=self._method_configs["ImportInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.ImportInstanceRequest(
            name=name, input_config=input_config
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["import_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            cloud_redis_pb2.Instance,
            metadata_type=any_pb2.Any,
        )

    def export_instance(
        self,
        name,
        output_config,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Export Redis instance data into a Redis RDB format file in Cloud Storage.

        Redis will continue serving during this operation.

        The returned operation is automatically deleted after a few hours, so
        there is no need to call DeleteOperation.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> # TODO: Initialize `output_config`:
            >>> output_config = {}
            >>>
            >>> response = client.export_instance(name, output_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): A developer-facing error message, which should be in English. Any
                user-facing error message should be localized and sent in the
                ``google.rpc.Status.details`` field, or localized by the client.
            output_config (Union[dict, ~google.cloud.redis_v1beta1.types.OutputConfig]): Required. Specify data to be exported.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.redis_v1beta1.types.OutputConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "export_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "export_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.export_instance,
                default_retry=self._method_configs["ExportInstance"].retry,
                default_timeout=self._method_configs["ExportInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.ExportInstanceRequest(
            name=name, output_config=output_config
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["export_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            cloud_redis_pb2.Instance,
            metadata_type=any_pb2.Any,
        )

    def failover_instance(
        self,
        name,
        data_protection_mode=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Initiates a failover of the master node to current replica node for a
        specific STANDARD tier Cloud Memorystore for Redis instance.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> name = client.instance_path('[PROJECT]', '[LOCATION]', '[INSTANCE]')
            >>>
            >>> response = client.failover_instance(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): A simple descriptor of a resource type.

                ResourceDescriptor annotates a resource message (either by means of a
                protobuf annotation or use in the service config), and associates the
                resource's schema, the resource type, and the pattern of the resource
                name.

                Example:

                ::

                    message Topic {
                      // Indicates this message defines a resource schema.
                      // Declares the resource type in the format of {service}/{kind}.
                      // For Kubernetes resources, the format is {api group}/{kind}.
                      option (google.api.resource) = {
                        type: "pubsub.googleapis.com/Topic"
                        name_descriptor: {
                          pattern: "projects/{project}/topics/{topic}"
                          parent_type: "cloudresourcemanager.googleapis.com/Project"
                          parent_name_extractor: "projects/{project}"
                        }
                      };
                    }

                The ResourceDescriptor Yaml config will look like:

                ::

                    resources:
                    - type: "pubsub.googleapis.com/Topic"
                      name_descriptor:
                        - pattern: "projects/{project}/topics/{topic}"
                          parent_type: "cloudresourcemanager.googleapis.com/Project"
                          parent_name_extractor: "projects/{project}"

                Sometimes, resources have multiple patterns, typically because they can
                live under multiple parents.

                Example:

                ::

                    message LogEntry {
                      option (google.api.resource) = {
                        type: "logging.googleapis.com/LogEntry"
                        name_descriptor: {
                          pattern: "projects/{project}/logs/{log}"
                          parent_type: "cloudresourcemanager.googleapis.com/Project"
                          parent_name_extractor: "projects/{project}"
                        }
                        name_descriptor: {
                          pattern: "folders/{folder}/logs/{log}"
                          parent_type: "cloudresourcemanager.googleapis.com/Folder"
                          parent_name_extractor: "folders/{folder}"
                        }
                        name_descriptor: {
                          pattern: "organizations/{organization}/logs/{log}"
                          parent_type: "cloudresourcemanager.googleapis.com/Organization"
                          parent_name_extractor: "organizations/{organization}"
                        }
                        name_descriptor: {
                          pattern: "billingAccounts/{billing_account}/logs/{log}"
                          parent_type: "billing.googleapis.com/BillingAccount"
                          parent_name_extractor: "billingAccounts/{billing_account}"
                        }
                      };
                    }

                The ResourceDescriptor Yaml config will look like:

                ::

                    resources:
                    - type: 'logging.googleapis.com/LogEntry'
                      name_descriptor:
                        - pattern: "projects/{project}/logs/{log}"
                          parent_type: "cloudresourcemanager.googleapis.com/Project"
                          parent_name_extractor: "projects/{project}"
                        - pattern: "folders/{folder}/logs/{log}"
                          parent_type: "cloudresourcemanager.googleapis.com/Folder"
                          parent_name_extractor: "folders/{folder}"
                        - pattern: "organizations/{organization}/logs/{log}"
                          parent_type: "cloudresourcemanager.googleapis.com/Organization"
                          parent_name_extractor: "organizations/{organization}"
                        - pattern: "billingAccounts/{billing_account}/logs/{log}"
                          parent_type: "billing.googleapis.com/BillingAccount"
                          parent_name_extractor: "billingAccounts/{billing_account}"

                For flexible resources, the resource name doesn't contain parent names,
                but the resource itself has parents for policy evaluation.

                Example:

                ::

                    message Shelf {
                      option (google.api.resource) = {
                        type: "library.googleapis.com/Shelf"
                        name_descriptor: {
                          pattern: "shelves/{shelf}"
                          parent_type: "cloudresourcemanager.googleapis.com/Project"
                        }
                        name_descriptor: {
                          pattern: "shelves/{shelf}"
                          parent_type: "cloudresourcemanager.googleapis.com/Folder"
                        }
                      };
                    }

                The ResourceDescriptor Yaml config will look like:

                ::

                    resources:
                    - type: 'library.googleapis.com/Shelf'
                      name_descriptor:
                        - pattern: "shelves/{shelf}"
                          parent_type: "cloudresourcemanager.googleapis.com/Project"
                        - pattern: "shelves/{shelf}"
                          parent_type: "cloudresourcemanager.googleapis.com/Folder"
            data_protection_mode (~google.cloud.redis_v1beta1.types.DataProtectionMode): Required. Unique name of the resource in this scope including
                project and location using the form:
                ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``

                Note: Redis instances are managed and addressed at regional level so
                location_id here refers to a GCP region; however, users may choose which
                specific zone (or collection of zones for cross-zone instances) an
                instance should be provisioned in. Refer to ``location_id`` and
                ``alternative_location_id`` fields for more details.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "failover_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "failover_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.failover_instance,
                default_retry=self._method_configs["FailoverInstance"].retry,
                default_timeout=self._method_configs["FailoverInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.FailoverInstanceRequest(
            name=name, data_protection_mode=data_protection_mode
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["failover_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            cloud_redis_pb2.Instance,
            metadata_type=any_pb2.Any,
        )

    def delete_instance(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a specific Redis instance.  Instance stops serving and data is
        deleted.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> name = client.instance_path('[PROJECT]', '[LOCATION]', '[INSTANCE]')
            >>>
            >>> response = client.delete_instance(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): The status code, which should be an enum value of
                ``google.rpc.Code``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_instance,
                default_retry=self._method_configs["DeleteInstance"].retry,
                default_timeout=self._method_configs["DeleteInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.DeleteInstanceRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["delete_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            empty_pb2.Empty,
            metadata_type=any_pb2.Any,
        )

    def upgrade_instance(
        self,
        name,
        redis_version,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Upgrades Redis instance to the newer Redis version specified in the
        request.

        Example:
            >>> from google.cloud import redis_v1beta1
            >>>
            >>> client = redis_v1beta1.CloudRedisClient()
            >>>
            >>> name = client.instance_path('[PROJECT]', '[LOCATION]', '[INSTANCE]')
            >>>
            >>> # TODO: Initialize `redis_version`:
            >>> redis_version = ''
            >>>
            >>> response = client.upgrade_instance(name, redis_version)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): The resource has one pattern, but the API owner expects to add more
                later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
                that from being necessary once there are multiple patterns.)
            redis_version (str): Required. Specifies the target version of Redis software to upgrade to.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.redis_v1beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "upgrade_instance" not in self._inner_api_calls:
            self._inner_api_calls[
                "upgrade_instance"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.upgrade_instance,
                default_retry=self._method_configs["UpgradeInstance"].retry,
                default_timeout=self._method_configs["UpgradeInstance"].timeout,
                client_info=self._client_info,
            )

        request = cloud_redis_pb2.UpgradeInstanceRequest(
            name=name, redis_version=redis_version
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["upgrade_instance"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            cloud_redis_pb2.Instance,
            metadata_type=any_pb2.Any,
        )
