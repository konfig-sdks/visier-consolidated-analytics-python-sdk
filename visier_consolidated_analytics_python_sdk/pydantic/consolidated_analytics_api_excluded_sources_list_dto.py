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
from pydantic import BaseModel, Field, RootModel

from visier_consolidated_analytics_python_sdk.pydantic.consolidated_analytics_api_excluded_sources_list_dto_excluded_sources import ConsolidatedAnalyticsAPIExcludedSourcesListDTOExcludedSources

class ConsolidatedAnalyticsAPIExcludedSourcesListDTO(BaseModel):
    excluded_sources: typing.Optional[ConsolidatedAnalyticsAPIExcludedSourcesListDTOExcludedSources] = Field(None, alias='excludedSources')
    class Config:
        arbitrary_types_allowed = True