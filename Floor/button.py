import json

__author__ = 'zqi2'

import ConfigParser

from requests.auth import HTTPBasicAuth

from entity import Entity


class Button(object, Entity):
    # config section
    _config_section = 'button'

    def __init__(self):
        Entity.__init__(self)
        parser = ConfigParser.SafeConfigParser()
        parser.read(self._config_file)

    def create(self, payload, auth=None):
        Entity.__init__(self)
        return super(Button, self).create(payload, auth)
