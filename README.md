# CSC2106_IoT_HomeAutomation
IOT Home Automation Project

## Setup
### Install Flask server packages
```
pip install -r requirements.txt
```


## Run flask server
### Go into flask folder
```
cd flask
```

### get hostname ip address on Raspberry Pi
```
hostname -I
```

### Run flask website
*replace 'ip_address' with your raspberry pi's actual ip
```
flask --app dashboard run --host=ip_address
```
if above not working, run the command below instead:
```
FLASK_APP=dashboard.py flask run --host=ip_address
```

### Launch flask website
open browser url to '<ip_address>:5000'