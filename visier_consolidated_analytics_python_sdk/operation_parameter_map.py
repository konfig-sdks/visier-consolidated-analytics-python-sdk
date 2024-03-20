operation_parameter_map = {
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources-PATCH': {
        'parameters': [
            {
                'name': 'excludedSources'
            },
            {
                'name': 'tenantId'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants-PATCH': {
        'parameters': [
            {
                'name': 'tenantCodes'
            },
            {
                'name': 'tenantId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants-POST': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants-GET': {
        'parameters': [
            {
                'name': 'tenantId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources-DELETE': {
        'parameters': [
            {
                'name': 'excludedSources'
            },
            {
                'name': 'tenantId'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants-DELETE': {
        'parameters': [
            {
                'name': 'tenantCodes'
            },
            {
                'name': 'tenantId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/excluded-sources-PUT': {
        'parameters': [
            {
                'name': 'excludedSources'
            },
            {
                'name': 'tenantId'
            },
        ]
    },
    '/v1alpha/admin/consolidated-analytics/tenants/:tenantId/source-tenants-PUT': {
        'parameters': [
            {
                'name': 'tenantCodes'
            },
            {
                'name': 'tenantId'
            },
            {
                'name': 'limit'
            },
        ]
    },
};