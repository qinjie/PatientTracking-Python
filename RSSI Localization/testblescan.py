# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print "ble thread started"

except:
    print "error accessing bluetooth device..."
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
cnt = 0
size = 30
f = open('rssi', 'a')
while True:
    returnedList = blescan.parse_events(sock, 5)
    for beacon in returnedList:
        f.writelines(beacon + '\n')
        print(beacon)
        cnt += 1
        if (cnt == size):
            break
    if (cnt == size):
        break
print("Done")
f.close()
