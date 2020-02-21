from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import unittest

from ansible_collections.os_migrate.os_migrate.tests.unit import fixtures
from ansible_collections.os_migrate.os_migrate.plugins.module_utils \
    import network


class TestSecurityGroup(unittest.TestCase):

    def test_serialize_security_group(self):
        sec = fixtures.sdk_security_group()
        serialized = network.serialize_security_group(sec)
        s_params = serialized['params']
        s_info = serialized['_info']

        self.assertEqual(serialized['type'], 'openstack.network.SecurityGroup')
        self.assertEqual(s_params['description'], 'Default security group')
        self.assertEqual(s_params['name'], 'default')
        self.assertEqual(s_params['tags'], [])

        self.assertEqual(s_info['created_at'], '2020-01-30T14:49:06Z')
        self.assertEqual(s_info['project_id'], 'uuid-project')
        self.assertEqual(s_info['updated_at'], '2020-01-30T14:49:06Z')

    def test_security_group_sdk_params(self):
        ser_sec = fixtures.serialized_security_group()
        sdk_params = network.security_group_sdk_params(ser_sec)

        self.assertEqual(sdk_params['description'], 'Default security group')
