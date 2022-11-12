# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.workflows_v1beta.services.workflows import pagers
from google.cloud.workflows_v1beta.types import workflows
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import WorkflowsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import WorkflowsGrpcAsyncIOTransport
from .client import WorkflowsClient


class WorkflowsAsyncClient:
    """Workflows is used to deploy and execute workflow programs.
    Workflows makes sure the program executes reliably, despite
    hardware and networking interruptions.
    """

    _client: WorkflowsClient

    DEFAULT_ENDPOINT = WorkflowsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = WorkflowsClient.DEFAULT_MTLS_ENDPOINT

    workflow_path = staticmethod(WorkflowsClient.workflow_path)
    parse_workflow_path = staticmethod(WorkflowsClient.parse_workflow_path)
    common_billing_account_path = staticmethod(WorkflowsClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(WorkflowsClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(WorkflowsClient.common_folder_path)
    parse_common_folder_path = staticmethod(WorkflowsClient.parse_common_folder_path)
    common_organization_path = staticmethod(WorkflowsClient.common_organization_path)
    parse_common_organization_path = staticmethod(WorkflowsClient.parse_common_organization_path)
    common_project_path = staticmethod(WorkflowsClient.common_project_path)
    parse_common_project_path = staticmethod(WorkflowsClient.parse_common_project_path)
    common_location_path = staticmethod(WorkflowsClient.common_location_path)
    parse_common_location_path = staticmethod(WorkflowsClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WorkflowsAsyncClient: The constructed client.
        """
        return WorkflowsClient.from_service_account_info.__func__(WorkflowsAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            WorkflowsAsyncClient: The constructed client.
        """
        return WorkflowsClient.from_service_account_file.__func__(WorkflowsAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return WorkflowsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> WorkflowsTransport:
        """Returns the transport used by the client instance.

        Returns:
            WorkflowsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(WorkflowsClient).get_transport_class, type(WorkflowsClient))

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Union[str, WorkflowsTransport] = "grpc_asyncio",
            client_options: Optional[ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the workflows client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.WorkflowsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = WorkflowsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def list_workflows(self,
            request: Optional[Union[workflows.ListWorkflowsRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListWorkflowsAsyncPager:
        r"""Lists Workflows in a given project and location.
        The default order is not specified.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import workflows_v1beta

            async def sample_list_workflows():
                # Create a client
                client = workflows_v1beta.WorkflowsAsyncClient()

                # Initialize request argument(s)
                request = workflows_v1beta.ListWorkflowsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_workflows(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.workflows_v1beta.types.ListWorkflowsRequest, dict]]):
                The request object. Request for the
                [ListWorkflows][google.cloud.workflows.v1beta.Workflows.ListWorkflows]
                method.
            parent (:class:`str`):
                Required. Project and location from
                which the workflows should be listed.
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.workflows_v1beta.services.workflows.pagers.ListWorkflowsAsyncPager:
                Response for the
                   [ListWorkflows][google.cloud.workflows.v1beta.Workflows.ListWorkflows]
                   method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = workflows.ListWorkflowsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_workflows,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListWorkflowsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_workflow(self,
            request: Optional[Union[workflows.GetWorkflowRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> workflows.Workflow:
        r"""Gets details of a single Workflow.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import workflows_v1beta

            async def sample_get_workflow():
                # Create a client
                client = workflows_v1beta.WorkflowsAsyncClient()

                # Initialize request argument(s)
                request = workflows_v1beta.GetWorkflowRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_workflow(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.workflows_v1beta.types.GetWorkflowRequest, dict]]):
                The request object. Request for the
                [GetWorkflow][google.cloud.workflows.v1beta.Workflows.GetWorkflow]
                method.
            name (:class:`str`):
                Required. Name of the workflow which
                information should be retrieved. Format:
                projects/{project}/locations/{location}/workflows/{workflow}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.workflows_v1beta.types.Workflow:
                Workflow program to be executed by
                Workflows.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = workflows.GetWorkflowRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_workflow,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_workflow(self,
            request: Optional[Union[workflows.CreateWorkflowRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            workflow: Optional[workflows.Workflow] = None,
            workflow_id: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Creates a new workflow. If a workflow with the specified name
        already exists in the specified project and location, the long
        running operation will return
        [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS] error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import workflows_v1beta

            async def sample_create_workflow():
                # Create a client
                client = workflows_v1beta.WorkflowsAsyncClient()

                # Initialize request argument(s)
                workflow = workflows_v1beta.Workflow()
                workflow.source_contents = "source_contents_value"

                request = workflows_v1beta.CreateWorkflowRequest(
                    parent="parent_value",
                    workflow=workflow,
                    workflow_id="workflow_id_value",
                )

                # Make the request
                operation = client.create_workflow(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.workflows_v1beta.types.CreateWorkflowRequest, dict]]):
                The request object. Request for the
                [CreateWorkflow][google.cloud.workflows.v1beta.Workflows.CreateWorkflow]
                method.
            parent (:class:`str`):
                Required. Project and location in
                which the workflow should be created.
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            workflow (:class:`google.cloud.workflows_v1beta.types.Workflow`):
                Required. Workflow to be created.
                This corresponds to the ``workflow`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            workflow_id (:class:`str`):
                Required. The ID of the workflow to be created. It has
                to fulfill the following requirements:

                -  Must contain only letters, numbers, underscores and
                   hyphens.
                -  Must start with a letter.
                -  Must be between 1-64 characters.
                -  Must end with a number or a letter.
                -  Must be unique within the customer project and
                   location.

                This corresponds to the ``workflow_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.workflows_v1beta.types.Workflow`
                Workflow program to be executed by Workflows.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, workflow, workflow_id])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = workflows.CreateWorkflowRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if workflow is not None:
            request.workflow = workflow
        if workflow_id is not None:
            request.workflow_id = workflow_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_workflow,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            workflows.Workflow,
            metadata_type=workflows.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_workflow(self,
            request: Optional[Union[workflows.DeleteWorkflowRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Deletes a workflow with the specified name.
        This method also cancels and deletes all running
        executions of the workflow.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import workflows_v1beta

            async def sample_delete_workflow():
                # Create a client
                client = workflows_v1beta.WorkflowsAsyncClient()

                # Initialize request argument(s)
                request = workflows_v1beta.DeleteWorkflowRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_workflow(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.workflows_v1beta.types.DeleteWorkflowRequest, dict]]):
                The request object. Request for the
                [DeleteWorkflow][google.cloud.workflows.v1beta.Workflows.DeleteWorkflow]
                method.
            name (:class:`str`):
                Required. Name of the workflow to be
                deleted. Format:
                projects/{project}/locations/{location}/workflows/{workflow}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = workflows.DeleteWorkflowRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_workflow,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=workflows.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_workflow(self,
            request: Optional[Union[workflows.UpdateWorkflowRequest, dict]] = None,
            *,
            workflow: Optional[workflows.Workflow] = None,
            update_mask: Optional[field_mask_pb2.FieldMask] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> operation_async.AsyncOperation:
        r"""Updates an existing workflow.
        Running this method has no impact on already running
        executions of the workflow. A new revision of the
        workflow may be created as a result of a successful
        update operation. In that case, such revision will be
        used in new workflow executions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import workflows_v1beta

            async def sample_update_workflow():
                # Create a client
                client = workflows_v1beta.WorkflowsAsyncClient()

                # Initialize request argument(s)
                workflow = workflows_v1beta.Workflow()
                workflow.source_contents = "source_contents_value"

                request = workflows_v1beta.UpdateWorkflowRequest(
                    workflow=workflow,
                )

                # Make the request
                operation = client.update_workflow(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.workflows_v1beta.types.UpdateWorkflowRequest, dict]]):
                The request object. Request for the
                [UpdateWorkflow][google.cloud.workflows.v1beta.Workflows.UpdateWorkflow]
                method.
            workflow (:class:`google.cloud.workflows_v1beta.types.Workflow`):
                Required. Workflow to be updated.
                This corresponds to the ``workflow`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                List of fields to be updated. If not
                present, the entire workflow will be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.workflows_v1beta.types.Workflow`
                Workflow program to be executed by Workflows.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([workflow, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = workflows.UpdateWorkflowRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if workflow is not None:
            request.workflow = workflow
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_workflow,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("workflow.name", request.workflow.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            workflows.Workflow,
            metadata_type=workflows.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-workflows",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "WorkflowsAsyncClient",
)
