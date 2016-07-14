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
import os


class AuthData(object):

    def __init__(self):
        self._api_host = None
        self._email = None
        self._api_token = None

        self.get_environment()

    def get_environment(self):

        if 'TSP_API_HOST' in os.environ:
            self._api_host = os.environ['TSP_API_HOST']

        if 'TSP_EMAIL' in os.environ:
            self._email = os.environ['TSP_EMAIL']

        if 'TSP_API_TOKEN' in os.environ:
            self._api_token = os.environ['TSP_API_TOKEN']

    @property
    def api_host(self):
        return self._api_host

    @property
    def email(self):
        return self._email

    @property
    def api_token(self):
        return self._api_token

