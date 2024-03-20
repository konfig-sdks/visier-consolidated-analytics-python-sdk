# coding: utf-8

"""
    Visier Consolidated Analytics APIs

    Visier APIs for managing consolidated analytics (CA) tenants.

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredConsolidatedAnalyticsAPITenantCreateRequestDTO(TypedDict):
    pass

class OptionalConsolidatedAnalyticsAPITenantCreateRequestDTO(TypedDict, total=False):
    # The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    tenantCode: str

class ConsolidatedAnalyticsAPITenantCreateRequestDTO(RequiredConsolidatedAnalyticsAPITenantCreateRequestDTO, OptionalConsolidatedAnalyticsAPITenantCreateRequestDTO):
    pass