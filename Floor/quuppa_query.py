import json

__author__ = 'zqi2'

import ConfigParser

import requests
from requests.auth import HTTPBasicAuth
from random import randint

from entity import Entity


class QuuppaQuery(Entity):
    # config section
    _config_section = 'quuppa-query'

    def __init__(self):
        Entity.__init__(self)

        parser = ConfigParser.SafeConfigParser()
        parser.read(self._config_file)
        self._url_quuppa = parser.get('default', 'url_quuppa')
        self._urls['tag_info'] = self._url_quuppa + parser.get(self._config_section, 'tag_info')
        self._urls['tag_position'] = self._url_quuppa + parser.get(self._config_section, 'tag_position')

    def dummy_list_tag_position(self, auth=None):
        x1 = randint(-20, 20)
        y1 = randint(-20, 20)
        x2 = randint(-20, 20)
        y2 = randint(-20, 20)
        t = """
            {
              "responseTS": 1409746066235,
              "tags": [
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
                    """+str(x1)+""",
                    """+str(y1)+""",
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
                    "id": \""""+str(randint(1, 7))+"""\",
                    "name": "cashier"
                  }]
                },
                {
                  "areaId": "TrackingArea1",
                  "areaName": "KCM",
                  "color": "#0000FF",
                  "coordinateSystemId": "CoordinateSystem1",
                  "covarianceMatrix": [
                    0.27,
                    -0.05,
                    -0.05,
                    0.76
                  ],
                  "id": "001830ecf762",
                  "name": "Basket_042",
                  "position": [
                    """+str(x2)+""",
                    """+str(y2)+""",
                    0.8
                  ],
                  "positionAccuracy": 0.88,
                  "positionTS": 1409746057001,
                  "smoothedPosition": [
                    26.5,
                    -12.83,
                    0.8      ],
                  "zones": [{
                    "id": \""""+str(randint(1, 14))+"""\",
                    "name": "Bread"
                  }]
                }
              ],
              "version": "2.0"
            }
        """
        return t

    def dummy_list_tag_info(self, auth=None):
        if randint(0,200) < 1: state = "pushed"
        else: state = "notPushed"
        t = """
            {
              "message": "TagInfo",
              "tags": [
                {
                  "batteryAlarm": "ok",
                  "txRateTS": 1467250903813,
                  "txRate": 9,
                  "tagStateTS": 1467250903813,
                  "accelerationTS": 1467185848281,
                  "acceleration": [
                    -50,
                    12,
                    27
                  ],
                  "buttonStateTS": 1467250903813,
                  "rssiLocatorCoords": [
                    -2,
                    2,
                    2.4
                  ],
                  "rssiCoordinateSystemName": null,
                  "batteryVoltage": "2.59",
                  "id": "001830ecece4",
                  "buttonState": \""""+state+"""\",
                  "tagState": "temporary",
                  "deviceType": "General",
                  "name": "Test_Tag",
                  "rssiTS": 1467250903826,
                  "rssi": 42,
                  "batteryAlarmTS": 1467250903360,
                  "lastAreaTS": 1467250903416,
                  "batteryVoltageTS": 1467250902792,
                  "tagStateTransitionStatusTS": 1467250903813,
                  "configStatus": "Done",
                  "txPower": 0,
                  "ioStatesTS": 1467250903813,
                  "zones": [
                    {
                      "id": "Zone001",
                      "name": "room"
                    }
                  ],
                  "triggerCount": 2,
                  "txPowerTS": 1467250903813,
                  "lastAreaId": "0001",
                  "tagStateTransitionStatus": "normal",
                  "configStatusTS": 1467250899887,
                  "lastPacketTS": 1467250903813,
                  "rssiLocator": "001830ed47ad",
                  "color": "#99FF33",
                  "lastAreaName": "Demo",
                  "triggerCountTS": 1467185848014,
                  "ioStates": [
                    "low",
                    "low",
                    "low",
                    "low"
                  ],
                  "group": "Student",
                  "rssiCoordinateSystemId": "0001"
                }
              ],
              "responseTS": 1467250903826,
              "status": "Ok",
              "command": "http://153.20.9.167:8080/qpe/getTagInfo?version=2",
              "code": 0,
              "version": "2.1"
            }
        """
        return t

    def list_tag_info(self, auth=None):
        try:
            url = self._urls['tag_info']
            self.log.info("list_tag_info: %s", url)
            headers = {'Accept': 'application/json'}
            r = requests.get(url, auth=auth, headers=headers)
            self.log.info("%s %s", r.status_code, r.headers['content-type'])
            if r.status_code == 200:
                return r.text
            else:
                return None
        except requests.exceptions.RequestException as e:
            self.log.error("Exception: " + str(e.message))
            return None

    def list_tag_position(self, auth=None):
        try:
            url = self._urls['tag_position']
            self.log.info("list_tag_position: %s", url)
            headers = {'Accept': 'application/json'}
            r = requests.get(url, auth=auth, headers=headers)
            self.log.info("%s %s", r.status_code, r.headers['content-type'])
            self.log.info(r.text)
            if r.status_code == 200:
                return r.text
            else:
                return None
        except requests.exceptions.RequestException as e:
            self.log.error("Exception: " + str(e.message))
            return None

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

    entity = QuuppaQuery()

    # LIST
    r1 = entity.dummy_list_tag_info()
    print r1

    r2 = entity.dummy_list_tag_position()
    print r2

    # entity.list_tag_info(auth)
    # entity.list_tag_position(auth)
