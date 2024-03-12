# CSC2106_IoT_HomeAutomation
IOT Home Automation Project

# Table of contents
1) [Set up Flask](#set-up-flask)
2) [Set up Mongo Database in Raspbery Pi](#set-up-mongo-database-in-raspberry-pi)

# Set up Flask
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

# Set up Mongo Database in Raspberry Pi
