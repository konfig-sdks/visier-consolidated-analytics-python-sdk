# coding: utf-8

"""
    Visier Consolidated Analytics APIs

    Visier APIs for managing consolidated analytics (CA) tenants.

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

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


class Status(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The response structure for errors.
    """


    class MetaOapg:
        
        class properties:
            errorCode = schemas.StrSchema
            message = schemas.StrSchema
            rci = schemas.StrSchema
            __annotations__ = {
                "errorCode": errorCode,
                "message": message,
                "rci": rci,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorCode"]) -> MetaOapg.properties.errorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rci"]) -> MetaOapg.properties.rci: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errorCode", "message", "rci", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorCode"]) -> typing.Union[MetaOapg.properties.errorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rci"]) -> typing.Union[MetaOapg.properties.rci, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errorCode", "message", "rci", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        errorCode: typing.Union[MetaOapg.properties.errorCode, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        rci: typing.Union[MetaOapg.properties.rci, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Status':
        return super().__new__(
            cls,
            *args,
            errorCode=errorCode,
            message=message,
            rci=rci,
            _configuration=_configuration,
            **kwargs,
        )