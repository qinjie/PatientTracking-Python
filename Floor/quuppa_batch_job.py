import json
import threading
import time
import thread
import datetime

from requests.auth import HTTPBasicAuth

from quuppa_query import QuuppaQuery
from quuppa_tag_info import QuuppaTagInfo
from quuppa_tag_position import QuuppaTagPosition
from resident_location import Location
from button import Button

__author__ = 'zqi2'

## Put scripts to /home/pi/patient_tracking folder.
## Add following line to crontab so that it will run once after boot
## @reboot python /home/pi/quuppa_batch_job.py &
## sudo crontab -e

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

    SEC = 1  # seconds
    ButtonSEC = 5*10 # * 10 ^ -1 seconds

    timestamp_file = 'last_job_timestamp'

    query = QuuppaQuery()
    tag_info = QuuppaTagInfo()
    tag_pos = QuuppaTagPosition()
    location = Location()
    button = Button()

    def batch():
        # update file datetime to record last job timestamp
        try:
            data = {}
            # r1 = query.dummy_list_tag_position()
            r1 = query.list_tag_position()
            if r1:
                j = json.loads(r1)
                ls = j['tags']
		print time.strftime('--- %l:%M%p %Z on %b %d, %Y ---')
                for t in ls:
                    data['tagid'] = t['id']
		    data['name'] = t['name']
		    data['created_at'] =t['positionTS']
                    data['zone'] = t['zones'][0]['name']
                    data['coorx'] = t['position'][0]
                    data['coory'] = t['position'][1]
                    print "%15s: %20s %15s(%5s,%5s)" % (data['name'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(data['created_at'])/1000.0)), data['zone'], data['coorx'], data['coory'])
		    #print data
                    location.create(data, auth)
        except Exception as exc:
            print exc
        threading.Timer(SEC, batch).start()
    def batchButton():
        count = 0
        array = []
        while True:
            try:
                data = {}
                r1 = query.list_tag_info()
                # r1 = query.dummy_list_tag_info()
                if r1:
                    j = json.loads(r1)
                    ls = j['tags']
                    for t in ls:
                        if t['buttonState'] == 'pushed':
                            data['tagid'] = t['id']
                            if data not in array:
                                array.append(data)
                if count < ButtonSEC:
                    time.sleep(0.1)
                    count += 1
                else:
                    count = 0
                    for i in range(len(array)):
                        # print "button " + array[i]['tagid']
                        button.create(array[i], auth)
                    array = []
            except Exception as exc:
                print exc

    # call the function
    batch()
    thread.start_new_thread(batchButton())

