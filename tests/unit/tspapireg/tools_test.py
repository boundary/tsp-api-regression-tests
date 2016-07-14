#!/usr/bin/env python
#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from tspapireg import AuthData
from unittest import TestCase
import os


class ToolsTests(TestCase):

    def setUp(self):
        pass

    def test_auth_data_default(self):
        a = AuthData()
        self.assertIsNone(a.api_host)
        self.assertIsNone(a.email)
        self.assertIsNone(a.api_token)

    def test_auth_data_environment(self):
        api_host = 'foo.bar'
        email = 'admin@example.com'
        api_token = 'DEADBEEF'

        os.environ['TSP_API_HOST'] = api_host
        os.environ['TSP_EMAIL'] = email
        os.environ['TSP_API_TOKEN'] = api_token

        a = AuthData()

        self.assertEqual(a.api_host, api_host)
        self.assertEqual(a.email, email)
        self.assertEqual(a.api_token, api_token)





