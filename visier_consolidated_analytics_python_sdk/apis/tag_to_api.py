import typing_extensions

from visier_consolidated_analytics_python_sdk.apis.tags import TagValues
from visier_consolidated_analytics_python_sdk.apis.tags.consolidated_analytics_v1_alpha_api import ConsolidatedAnalyticsV1AlphaApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CONSOLIDATED_ANALYTICS_V1ALPHA: ConsolidatedAnalyticsV1AlphaApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CONSOLIDATED_ANALYTICS_V1ALPHA: ConsolidatedAnalyticsV1AlphaApi,
    }
)
