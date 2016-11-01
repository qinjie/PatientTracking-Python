import mysql.connector
import requests
import threading

if __name__ == "__main__":
    SEC = 5 #update per 5s
    # local = raw_input("Enter your localhost:")
    local = 'localhost'
    ip = 'http://' + local + '/patient-tracking-web/api/web/user/alert'
    print 'Started'
    def batch():
        cnx = mysql.connector.connect(user='sa', password='abcd1234',
                                      host='localhost:3',
                                      database='patient_tracking')
        cursor = cnx.cursor()
        cursor.execute("""
                select resident_id, floor_id
                from location as rl
                where created_at < DATE_SUB(NOW(), INTERVAL 6 second)
                """)
        results = cursor.fetchall()
        for row in results:
            resident_id = row[0]
            last_position = row[1]
            ipa = ip + '?resident_id=' + str(row[0]) + '&last_position=' + str(row[1]) + '&type=3'
            print 'Alert resident id: ' + str(resident_id) + ' at position ' + str(last_position)
            r = requests.post(ipa)
        cursor.close()
        cnx.close()
        threading.Timer(SEC, batch).start()
    batch()