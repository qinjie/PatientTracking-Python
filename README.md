# PatientTracking-Python

##Introduction

Python background process have 2 applications which one is running in Server side and one is running in the Floor side;
    
- [Server side](#server)
    
- [Floor side](#floor)
    
## Server

Python application has reponsibility to check all the patient who have location signal is running out of date and send the notification to the server.

### Instruction

1. If you use remote server, SSH to server;
2. Recommend to go to: ```/var/www/html``` (Root directory of Apache);
3. Install library for those python library: ```requests```, ```mysql```;
4. Run: ```git clone https://github.com/qinjie/PatientTracking-Python```;
5. Go to: ```PatientTracking-Python/Server```;
6. Config database, loop time, PatientTracking-Web address in main.py;<br>
![Config Image](https://github.com/qinjie/PatientTracking-Python/blob/master/config_server.png)
7. Run: python main.py.


## Floor