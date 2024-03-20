# coding: utf-8

"""
    Visier Consolidated Analytics APIs

    Visier APIs for managing consolidated analytics (CA) tenants.

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from visier_consolidated_analytics_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from visier_consolidated_analytics_python_sdk.api_response import AsyncGeneratorResponse
from visier_consolidated_analytics_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_consolidated_analytics_python_sdk import schemas  # noqa: F401

from visier_consolidated_analytics_python_sdk.model.status import Status as StatusSchema
from visier_consolidated_analytics_python_sdk.model.consolidated_analytics_api_tenant_create_request_dto import ConsolidatedAnalyticsAPITenantCreateRequestDTO as ConsolidatedAnalyticsAPITenantCreateRequestDTOSchema

from visier_consolidated_analytics_python_sdk.type.status import Status
from visier_consolidated_analytics_python_sdk.type.consolidated_analytics_api_tenant_create_request_dto import ConsolidatedAnalyticsAPITenantCreateRequestDTO

from ...api_client import Dictionary
from visier_consolidated_analytics_python_sdk.pydantic.status import Status as StatusPydantic
from visier_consolidated_analytics_python_sdk.pydantic.consolidated_analytics_api_tenant_create_request_dto import ConsolidatedAnalyticsAPITenantCreateRequestDTO as ConsolidatedAnalyticsAPITenantCreateRequestDTOPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = ConsolidatedAnalyticsAPITenantCreateRequestDTOSchema


request_body_consolidated_analytics_api_tenant_create_request_dto = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ConsolidatedAnalyticsAPITenantCreateRequestDTOSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConsolidatedAnalyticsAPITenantCreateRequestDTO


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConsolidatedAnalyticsAPITenantCreateRequestDTO


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = StatusSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Status


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Status


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_tenant_mapped_args(
        self,
        tenant_code: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if tenant_code is not None:
            _body["tenantCode"] = tenant_code
        args.body = _body
        return args

    async def _acreate_tenant_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a consolidated analytics tenant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1alpha/admin/consolidated-analytics/tenants',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_consolidated_analytics_api_tenant_create_request_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_tenant_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a consolidated analytics tenant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1alpha/admin/consolidated-analytics/tenants',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_consolidated_analytics_api_tenant_create_request_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateTenantRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
        )
        return await self._acreate_tenant_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
        )
        return self._create_tenant_oapg(
            body=args.body,
        )

class CreateTenant(BaseApi):

    async def acreate_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConsolidatedAnalyticsAPITenantCreateRequestDTOPydantic:
        raw_response = await self.raw.acreate_tenant(
            tenant_code=tenant_code,
            **kwargs,
        )
        if validate:
            return ConsolidatedAnalyticsAPITenantCreateRequestDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConsolidatedAnalyticsAPITenantCreateRequestDTOPydantic, raw_response.body)
    
    
    def create_tenant(
        self,
        tenant_code: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ConsolidatedAnalyticsAPITenantCreateRequestDTOPydantic:
        raw_response = self.raw.create_tenant(
            tenant_code=tenant_code,
        )
        if validate:
            return ConsolidatedAnalyticsAPITenantCreateRequestDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConsolidatedAnalyticsAPITenantCreateRequestDTOPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        tenant_code: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
        )
        return await self._acreate_tenant_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        tenant_code: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_tenant_mapped_args(
            tenant_code=tenant_code,
        )
        return self._create_tenant_oapg(
            body=args.body,
        )

