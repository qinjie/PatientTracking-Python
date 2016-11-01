import json

__author__ = 'zqi2'

import ConfigParser

from requests.auth import HTTPBasicAuth

from entity import Entity


class QuuppaTagPosition(object, Entity):
    # config section
    _config_section = 'quuppa-tag-position'

    def __init__(self):
        Entity.__init__(self)

        parser = ConfigParser.SafeConfigParser()
        parser.read(self._config_file)

    def create(self, payload, auth=None):
        payload["tagId"] = payload["id"]
        payload["positionX"] = payload["position"][0]
        payload["positionY"] = payload["position"][1]
        payload["positionZ"] = payload["position"][2]
        payload["smoothedPositionX"] = payload["smoothedPosition"][0]
        payload["smoothedPositionY"] = payload["smoothedPosition"][1]
        payload["smoothedPositionZ"] = payload["smoothedPosition"][2]

        payload["covarianceMatrix"] = str(payload["covarianceMatrix"])
        payload["zones"] = str(payload["zones"])
        payload["positionTS"] = str(payload["positionTS"])
        payload["position"] = str(payload["position"])
        payload["smoothedPosition"] = str(payload["smoothedPosition"])

        return super(QuuppaTagPosition, self).create(payload, auth)


if __name__ == '__main__':
    # # Read options from command line
    # argParser = argparse.ArgumentParser('API Entity')
    # argParser.add_argument('-c', '--configFile', help="Configuration file", required=False)
    # argParser.add_argument('-s', '--configSession', help="Configuration session", required=False)
    # argParser.add_argument('-u', '--username', help="Username", required=False)
    # argParser.add_argument('-p', '--password', help="Password", required=False)
    # args = argParser.parse_args()

    # Username and Password for Authentication
    username = 'user1'
    password = '123456'
    auth = HTTPBasicAuth(username, password)

    entity = QuuppaTagPosition()

    # LIST
    entity.list(auth)

    # VIEW
    entity.view(1)

    # CREATE
    data1 = """
             {
              "areaId": "TrackingArea1",
              "areaName": "KCM",
              "color": "#0000FF",
              "coordinateSystemId": "CoordinateSystem1",
              "covarianceMatrix": [
                0.24,
                0.12,
                0.12,
                0.16
              ],
              "id": "001830ecece4",
              "name": "Basket_010",
              "position": [
                -8.11,
                25.06,
                0.8
              ],
              "positionAccuracy": 0.57,
              "positionTS": 1409746065430,
              "smoothedPosition": [
                -7.25,
                25.42,
                0.8
              ],
              "zones": [{
                "id": "Zone005",
                "name": "cashier"
              }]
            }
            """
    j1 = json.loads(data1)
    r1 = entity.create(j1, auth)
