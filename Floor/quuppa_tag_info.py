import json

__author__ = 'zqi2'

import ConfigParser

from requests.auth import HTTPBasicAuth

from entity import Entity


class QuuppaTagInfo(object, Entity):
    # config section
    _config_section = 'quuppa-tag-info'

    def __init__(self):
        Entity.__init__(self)

        parser = ConfigParser.SafeConfigParser()
        parser.read(self._config_file)


    def create(self, payload, auth=None):



        return super(QuuppaTagInfo, self).create(payload, auth)


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

    entity = QuuppaTagInfo()

    # LIST
    entity.list(auth)

    # VIEW
    entity.view(4)

    # CREATE
    data1 = """
            {
              "acceleration": [
                -65,
                0,
                -3
              ],
              "accelerationTS": 1409746404528,
              "batteryAlarm": "ok",
              "batteryAlarmTS": 1409746423225,
              "batteryVoltage": "2.68",
              "batteryVoltageTS": 1409746423225,
              "buttonState": "notPushed",
              "buttonStateTS": 1409746414540,
              "color": "#FF0000",
              "custom": null,
              "customTS": 1409746423224,
              "id": "001830ed4f4f",
              "ioStates": [
                "low",
                "low",
                "low",
                "low"
              ],
              "ioStatesTS": 1409746414540,
              "lastAreaId": "TrackingArea1",
              "lastAreaName": "KCM",
              "lastAreaTS": 1409746404525,
              "lastPacketTS": 1409746414540,
              "name": "Trolley_099",
              "rssi": 28,
              "rssiCoordinateSystemId": "CoordinateSystem1",
              "rssiCoordinateSystemName": null,
              "rssiLocator": "78c5e56f4078",
              "rssiLocatorCoords": [
                -18.95,
                22.64,
                4.3
              ],
              "rssiTS": 1409746423225,
              "tagState": "default",
              "tagStateTS": 1409746414540,
              "tagStateTransitionStatus": "normal",
              "tagStateTransitionStatusTS": 1409746414540,
              "triggerCount": 34286,
              "triggerCountTS": 1409746394506,
              "zones": []
            }
            """
    j1 = json.loads(data1)
    r1 = entity.create(j1, auth)
