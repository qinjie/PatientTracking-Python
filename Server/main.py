import mysql.connector
import requests
import threading

if __name__ == "__main__":
    SEC = 5 #update per 5s
    # local = raw_input("Enter your localhost:")
    local = 'localhost'
    ip = 'http://' + local + '/patient-tracking-web/api/web/user/alert'
    print('Started')
    def batch():
        threading.Timer(SEC, batch).start()
    batch()