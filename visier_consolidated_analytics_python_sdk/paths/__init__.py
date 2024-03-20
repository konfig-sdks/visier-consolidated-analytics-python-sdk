# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_consolidated_analytics_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1ALPHA_ADMIN_CONSOLIDATEDANALYTICS_TENANTS = "/v1alpha/admin/consolidated-analytics/tenants"
    V1ALPHA_ADMIN_CONSOLIDATEDANALYTICS_TENANTS_TENANT_ID_EXCLUDEDSOURCES = "/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources"
    V1ALPHA_ADMIN_CONSOLIDATEDANALYTICS_TENANTS_TENANT_ID_SOURCETENANTS = "/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants"
