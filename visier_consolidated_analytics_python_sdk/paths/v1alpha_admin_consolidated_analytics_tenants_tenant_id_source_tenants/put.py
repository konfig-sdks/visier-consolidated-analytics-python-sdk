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
from visier_consolidated_analytics_python_sdk.model.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO as ConsolidatedAnalyticsAPISourceTenantListDTOSchema
from visier_consolidated_analytics_python_sdk.model.tenant_code_body import TenantCodeBody as TenantCodeBodySchema
from visier_consolidated_analytics_python_sdk.model.tenant_code_body_tenant_codes import TenantCodeBodyTenantCodes as TenantCodeBodyTenantCodesSchema

from visier_consolidated_analytics_python_sdk.type.tenant_code_body_tenant_codes import TenantCodeBodyTenantCodes
from visier_consolidated_analytics_python_sdk.type.tenant_code_body import TenantCodeBody
from visier_consolidated_analytics_python_sdk.type.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier_consolidated_analytics_python_sdk.type.status import Status

from ...api_client import Dictionary
from visier_consolidated_analytics_python_sdk.pydantic.tenant_code_body import TenantCodeBody as TenantCodeBodyPydantic
from visier_consolidated_analytics_python_sdk.pydantic.status import Status as StatusPydantic
from visier_consolidated_analytics_python_sdk.pydantic.tenant_code_body_tenant_codes import TenantCodeBodyTenantCodes as TenantCodeBodyTenantCodesPydantic
from visier_consolidated_analytics_python_sdk.pydantic.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO as ConsolidatedAnalyticsAPISourceTenantListDTOPydantic

from . import path

# Query params
TenantIdSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'tenantId': typing.Union[TenantIdSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_tenant_id = api_client.QueryParameter(
    name="tenantId",
    style=api_client.ParameterStyle.FORM,
    schema=TenantIdSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = TenantCodeBodySchema


request_body_tenant_code_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ConsolidatedAnalyticsAPISourceTenantListDTOSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConsolidatedAnalyticsAPISourceTenantListDTO


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConsolidatedAnalyticsAPISourceTenantListDTO


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

    def _set_source_tenants_mapped_args(
        self,
        tenant_codes: typing.Optional[TenantCodeBodyTenantCodes] = None,
        tenant_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if tenant_codes is not None:
            _body["tenantCodes"] = tenant_codes
        args.body = _body
        if tenant_id is not None:
            _query_params["tenantId"] = tenant_id
        if limit is not None:
            _query_params["limit"] = limit
        args.query = _query_params
        return args

    async def _aset_source_tenants_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Set a consolidated analytics tenant&#x27;s source tenants
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_tenant_id,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_tenant_code_body.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _set_source_tenants_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Set a consolidated analytics tenant&#x27;s source tenants
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_tenant_id,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_tenant_code_body.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class SetSourceTenantsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aset_source_tenants(
        self,
        tenant_codes: typing.Optional[TenantCodeBodyTenantCodes] = None,
        tenant_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_source_tenants_mapped_args(
            tenant_codes=tenant_codes,
            tenant_id=tenant_id,
            limit=limit,
        )
        return await self._aset_source_tenants_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def set_source_tenants(
        self,
        tenant_codes: typing.Optional[TenantCodeBodyTenantCodes] = None,
        tenant_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_source_tenants_mapped_args(
            tenant_codes=tenant_codes,
            tenant_id=tenant_id,
            limit=limit,
        )
        return self._set_source_tenants_oapg(
            body=args.body,
            query_params=args.query,
        )

class SetSourceTenants(BaseApi):

    async def aset_source_tenants(
        self,
        tenant_codes: typing.Optional[TenantCodeBodyTenantCodes] = None,
        tenant_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConsolidatedAnalyticsAPISourceTenantListDTOPydantic:
        raw_response = await self.raw.aset_source_tenants(
            tenant_codes=tenant_codes,
            tenant_id=tenant_id,
            limit=limit,
            **kwargs,
        )
        if validate:
            return ConsolidatedAnalyticsAPISourceTenantListDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConsolidatedAnalyticsAPISourceTenantListDTOPydantic, raw_response.body)
    
    
    def set_source_tenants(
        self,
        tenant_codes: typing.Optional[TenantCodeBodyTenantCodes] = None,
        tenant_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ConsolidatedAnalyticsAPISourceTenantListDTOPydantic:
        raw_response = self.raw.set_source_tenants(
            tenant_codes=tenant_codes,
            tenant_id=tenant_id,
            limit=limit,
        )
        if validate:
            return ConsolidatedAnalyticsAPISourceTenantListDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConsolidatedAnalyticsAPISourceTenantListDTOPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        tenant_codes: typing.Optional[TenantCodeBodyTenantCodes] = None,
        tenant_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_source_tenants_mapped_args(
            tenant_codes=tenant_codes,
            tenant_id=tenant_id,
            limit=limit,
        )
        return await self._aset_source_tenants_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def put(
        self,
        tenant_codes: typing.Optional[TenantCodeBodyTenantCodes] = None,
        tenant_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_source_tenants_mapped_args(
            tenant_codes=tenant_codes,
            tenant_id=tenant_id,
            limit=limit,
        )
        return self._set_source_tenants_oapg(
            body=args.body,
            query_params=args.query,
        )

