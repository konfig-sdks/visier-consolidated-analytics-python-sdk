# coding: utf-8

"""
    Visier Consolidated Analytics APIs

    Visier APIs for managing consolidated analytics (CA) tenants.

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import visier_consolidated_analytics_python_sdk
from visier_consolidated_analytics_python_sdk.paths.v1alpha_admin_consolidated_analytics_tenants_tenant_id_excluded_sources import get
from visier_consolidated_analytics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1alphaAdminConsolidatedAnalyticsTenantsTenantIdExcludedSources(ApiTestMixin, unittest.TestCase):
    """
    V1alphaAdminConsolidatedAnalyticsTenantsTenantIdExcludedSources unit test stubs
        Retrieve a consolidated analytics tenant's excluded sources
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
