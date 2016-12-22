# PatientTracking-Python

##Introduction

Python background process have 2 applications which one is running in Server side and one is running in the Floor side;
    
- [Server side](#server)
    
- [Floor side](#floor)
    
## Server

Python application has reponsibility to check all the patient who have location signal is running out of date and sends the notification to the server.

### Instruction

1. If you use remote server, SSH to server;
2. Recommend to go to: ```/var/www/html``` (Root directory of Apache);
3. Install library for those python library: ```requests```, ```mysql-connector``` (If need);
4. Run: ```git clone https://github.com/qinjie/PatientTracking-Python```;
5. Go to: ```PatientTracking-Python/Server```;
6. Config database, loop time, PatientTracking-Web address in main.py;<br>
![Config Image](https://github.com/qinjie/PatientTracking-Python/blob/master/config_server.png)
7. Run: ```python main.py``` or ```python3 main.py```.


## Floor

Python application is running in Floor which has responsibility to collect data from Quuppa locators and sends it to [Server](https://github.com/qinjie/PatientTracking-Web)

### Instruction

1. Recommend to go to Desktop;
2. Run: ```git clone https://github.com/qinjie/PatientTracking-Python```;
3. Go to: ```PatientTracking-Python/Floor```;
4. Config server address in: ```server.ini``` file:
    + ```url_base```: Web API address;
    + ```url_quuppa```: Quuppa server address;
5. Run: ```python3 quuppa_batch_job.py``` or ```python quuppa_batch_job.py```, to sends data to server.