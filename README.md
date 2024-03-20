<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for managing consolidated analytics (CA) tenants.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.add_excluded_sources`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphaadd_excluded_sources)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.add_source_tenants`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphaadd_source_tenants)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.create_tenant`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphacreate_tenant)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_excluded_sources`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphalist_excluded_sources)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_source_tenants`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphalist_source_tenants)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_tenants`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphalist_tenants)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.remove_excluded_sources`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alpharemove_excluded_sources)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.remove_source_tenants`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alpharemove_source_tenants)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.set_excluded_sources`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphaset_excluded_sources)
  * [`visierconsolidatedanalytics.consolidated_analytics_v1_alpha.set_source_tenants`](#visierconsolidatedanalyticsconsolidated_analytics_v1_alphaset_source_tenants)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=ConsolidatedAnalytics&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_consolidated_analytics_python_sdk import (
    VisierConsolidatedAnalytics,
    ApiException,
)

visierconsolidatedanalytics = VisierConsolidatedAnalytics()

try:
    # Add excluded sources to a consolidated analytics tenant
    add_excluded_sources_response = visierconsolidatedanalytics.consolidated_analytics_v1_alpha.add_excluded_sources(
        excluded_sources=["string_example"],
        tenant_id="string_example",
    )
    print(add_excluded_sources_response)
except ApiException as e:
    print(
        "Exception when calling ConsolidatedAnalyticsV1AlphaApi.add_excluded_sources: %s\n"
        % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from visier_consolidated_analytics_python_sdk import (
    VisierConsolidatedAnalytics,
    ApiException,
)

visierconsolidatedanalytics = VisierConsolidatedAnalytics()


async def main():
    try:
        # Add excluded sources to a consolidated analytics tenant
        add_excluded_sources_response = await visierconsolidatedanalytics.consolidated_analytics_v1_alpha.aadd_excluded_sources(
            excluded_sources=["string_example"],
            tenant_id="string_example",
        )
        print(add_excluded_sources_response)
    except ApiException as e:
        print(
            "Exception when calling ConsolidatedAnalyticsV1AlphaApi.add_excluded_sources: %s\n"
            % e
        )
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_consolidated_analytics_python_sdk import (
    VisierConsolidatedAnalytics,
    ApiException,
)

visierconsolidatedanalytics = VisierConsolidatedAnalytics()

try:
    # Add excluded sources to a consolidated analytics tenant
    add_excluded_sources_response = visierconsolidatedanalytics.consolidated_analytics_v1_alpha.raw.add_excluded_sources(
        excluded_sources=["string_example"],
        tenant_id="string_example",
    )
    pprint(add_excluded_sources_response.body)
    pprint(add_excluded_sources_response.body["excluded_sources"])
    pprint(add_excluded_sources_response.headers)
    pprint(add_excluded_sources_response.status)
    pprint(add_excluded_sources_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling ConsolidatedAnalyticsV1AlphaApi.add_excluded_sources: %s\n"
        % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.add_excluded_sources`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphaadd_excluded_sources"></a>

This API adds excluded sources to the list of excluded sources for a consolidated analytics tenant.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_excluded_sources_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.add_excluded_sources(
        excluded_sources=["string_example"],
        tenant_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### excluded_sources: [`ExcludedSourcesBodyExcludedSources`](./visier_consolidated_analytics_python_sdk/type/excluded_sources_body_excluded_sources.py)<a id="excluded_sources-excludedsourcesbodyexcludedsourcesvisier_consolidated_analytics_python_sdktypeexcluded_sources_body_excluded_sourcespy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExcludedSourcesBody`](./visier_consolidated_analytics_python_sdk/type/excluded_sources_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPIExcludedSourcesListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_excluded_sources_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.add_source_tenants`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphaadd_source_tenants"></a>

This API adds source tenants to the list of source tenants for a consolidated analytics tenant.

 If successful, the response returns an updated list of source tenants.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_source_tenants_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.add_source_tenants(
        tenant_codes=["string_example"],
        tenant_id="string_example",
        limit=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_codes: [`TenantCodeBodyTenantCodes`](./visier_consolidated_analytics_python_sdk/type/tenant_code_body_tenant_codes.py)<a id="tenant_codes-tenantcodebodytenantcodesvisier_consolidated_analytics_python_sdktypetenant_code_body_tenant_codespy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

##### limit: `int`<a id="limit-int"></a>

The maximum number of source tenants to return. The maximum value is 1000. Default is 400.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TenantCodeBody`](./visier_consolidated_analytics_python_sdk/type/tenant_code_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPISourceTenantListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_source_tenant_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.create_tenant`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphacreate_tenant"></a>

This API allows you to create a consolidated analytics tenant.

 A new CA tenant has no source tenants and no excluded sources.

 **Note:** CA tenant codes must have a prefix of CA. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}
 is the consolidated analytic tenant code.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_tenant_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.create_tenant(
        tenant_code="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConsolidatedAnalyticsAPITenantCreateRequestDTO`](./visier_consolidated_analytics_python_sdk/type/consolidated_analytics_api_tenant_create_request_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPITenantCreateRequestDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_tenant_create_request_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_excluded_sources`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphalist_excluded_sources"></a>

This API allows you to retrieve a CA tenant's excluded sources.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_excluded_sources_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_excluded_sources(
        tenant_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPIExcludedSourcesListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_excluded_sources_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_source_tenants`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphalist_source_tenants"></a>

This API allows you to retrieve a CA tenant's source tenants.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_source_tenants_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_source_tenants(
        tenant_id="string_example",
        limit=1,
        start=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

##### limit: `int`<a id="limit-int"></a>

The maximum number of source tenants to return. The maximum value is 1000. Default is 400.

##### start: `int`<a id="start-int"></a>

The starting index of the first source tenant to return. Default is 0.

#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPISourceTenantListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_source_tenant_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_tenants`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphalist_tenants"></a>

This API allows you to retrieve the full list of consolidated analytics tenants in your administrating tenant.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tenants_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.list_tenants(
        limit=1,
        start=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of tenants to return. The maximum value is 1000. Default is 400.

##### start: `int`<a id="start-int"></a>

The starting index of the first tenant to return. Default is 0.

#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPITenantListResponseDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_tenant_list_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.remove_excluded_sources`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alpharemove_excluded_sources"></a>

This API removes excluded sources from the list of excluded sources for a consolidated analytics tenant.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_excluded_sources_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.remove_excluded_sources(
        excluded_sources=["string_example"],
        tenant_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### excluded_sources: [`ExcludedSourcesBodyExcludedSources`](./visier_consolidated_analytics_python_sdk/type/excluded_sources_body_excluded_sources.py)<a id="excluded_sources-excludedsourcesbodyexcludedsourcesvisier_consolidated_analytics_python_sdktypeexcluded_sources_body_excluded_sourcespy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExcludedSourcesBody`](./visier_consolidated_analytics_python_sdk/type/excluded_sources_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPIExcludedSourcesListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_excluded_sources_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.remove_source_tenants`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alpharemove_source_tenants"></a>

This API removes source tenants from the list of source tenants for a consolidated analytics tenant.

 If successful, the response returns an updated list of source tenants.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_source_tenants_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.remove_source_tenants(
        tenant_codes=["string_example"],
        tenant_id="string_example",
        limit=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_codes: [`TenantCodeBodyTenantCodes`](./visier_consolidated_analytics_python_sdk/type/tenant_code_body_tenant_codes.py)<a id="tenant_codes-tenantcodebodytenantcodesvisier_consolidated_analytics_python_sdktypetenant_code_body_tenant_codespy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

##### limit: `int`<a id="limit-int"></a>

The maximum number of source tenants to return. The maximum value is 1000. Default is 400.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TenantCodeBody`](./visier_consolidated_analytics_python_sdk/type/tenant_code_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPISourceTenantListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_source_tenant_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.set_excluded_sources`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphaset_excluded_sources"></a>

This API defines the excluded sources for a consolidated analytics tenant.

 After you create a CA tenant, you may optionally define a list of excluded sources. The excluded sources are the sources whose data is excluded from the CA tenant.
 You can also use this API to replace the list of excluded sources for an existing CA tenant.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_excluded_sources_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.set_excluded_sources(
        excluded_sources=["string_example"],
        tenant_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### excluded_sources: [`ExcludedSourcesBodyExcludedSources`](./visier_consolidated_analytics_python_sdk/type/excluded_sources_body_excluded_sources.py)<a id="excluded_sources-excludedsourcesbodyexcludedsourcesvisier_consolidated_analytics_python_sdktypeexcluded_sources_body_excluded_sourcespy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExcludedSourcesBody`](./visier_consolidated_analytics_python_sdk/type/excluded_sources_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPIExcludedSourcesListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_excluded_sources_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierconsolidatedanalytics.consolidated_analytics_v1_alpha.set_source_tenants`<a id="visierconsolidatedanalyticsconsolidated_analytics_v1_alphaset_source_tenants"></a>

This API defines the source tenants for a consolidated analytics tenant.

 After you create a CA tenant, you must define a list of its source tenants. The source tenants are the tenants whose data is aggregated in the CA tenant.
 You can also use this API to replace the list of source tenants for an existing CA tenant.

 If successful, the response returns an updated list of source tenants.

 <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.
 If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_source_tenants_response = (
    visierconsolidatedanalytics.consolidated_analytics_v1_alpha.set_source_tenants(
        tenant_codes=["string_example"],
        tenant_id="string_example",
        limit=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_codes: [`TenantCodeBodyTenantCodes`](./visier_consolidated_analytics_python_sdk/type/tenant_code_body_tenant_codes.py)<a id="tenant_codes-tenantcodebodytenantcodesvisier_consolidated_analytics_python_sdktypetenant_code_body_tenant_codespy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

##### limit: `int`<a id="limit-int"></a>

The maximum number of source tenants to return. The maximum value is 1000. Default is 400.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TenantCodeBody`](./visier_consolidated_analytics_python_sdk/type/tenant_code_body.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConsolidatedAnalyticsAPISourceTenantListDTO`](./visier_consolidated_analytics_python_sdk/pydantic/consolidated_analytics_api_source_tenant_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
