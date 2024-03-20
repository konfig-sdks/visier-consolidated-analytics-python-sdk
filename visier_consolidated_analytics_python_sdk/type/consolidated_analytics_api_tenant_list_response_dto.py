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

from visier_consolidated_analytics_python_sdk.type.consolidated_analytics_api_tenant_list_response_dto_tenant_codes import ConsolidatedAnalyticsAPITenantListResponseDTOTenantCodes

class RequiredConsolidatedAnalyticsAPITenantListResponseDTO(TypedDict):
    pass

class OptionalConsolidatedAnalyticsAPITenantListResponseDTO(TypedDict, total=False):
    tenantCodes: ConsolidatedAnalyticsAPITenantListResponseDTOTenantCodes

class ConsolidatedAnalyticsAPITenantListResponseDTO(RequiredConsolidatedAnalyticsAPITenantListResponseDTO, OptionalConsolidatedAnalyticsAPITenantListResponseDTO):
    pass
