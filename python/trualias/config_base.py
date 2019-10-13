#!/usr/bin/python3
# Copyright (c) 2019 by Fred Morris Tacoma WA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Miscellaneous configuration prerequisites."""

import logging
from ipaddress import ip_address

CASE_SENSITIVE = False
HOST = ip_address('127.0.0.1')
PORT = 3047
LOGGING = logging.WARNING
DEBUG_ACCOUNT = None

class Loader(object):
    """Base class for all config generators/loaders."""
    pass

class ConfigurationError(Exception):
    """An invalid/inconsistent configuration."""
    def __init__(self, reason, additional=None):
        self.reason = reason
        self.additional = additional or []
        return
    
    def __str__(self):
        return '{} ({})'.format(self.reason,
                                ', '.join('{}:{}'.format(k,str(self.additional[k])) for k in self.additional.keys())
                               )

def DEFAULT_CONFIG(minimal=False):
    """A function so that it generates a fresh one every time.
    
    Minimal causes the dictionary to be suitable for updating another
    config.
    """
    
    if minimal:
        config = dict()
    else:
        config = dict(
                    case_sensitive=CASE_SENSITIVE,
                    host=HOST,
                    port=PORT,
                    logging=LOGGING,
                    debug_account=DEBUG_ACCOUNT
                 )
    config['aliases'] = []
    return config

