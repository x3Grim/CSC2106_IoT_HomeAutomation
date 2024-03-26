# CSC2106_IoT_HomeAutomation
IOT Home Automation Project

# Table of contents
1) [Set up Flask](#set-up-flask)
2) [Set up Mongo Database in Raspbery Pi](#set-up-mongo-database-in-raspberry-pi)

# Set up Flask
## Setup
### Install Flask server packages
```shell
pip install -r requirements.txt
```

## Run flask server
### Go into flask folder
```shell
cd flask
```
### get hostname ip address on Raspberry Pi
```shell
hostname -I
```
### Run flask website
*replace 'ip_address' with your raspberry pi's actual ip
```shell
flask --app dashboard run --host=ip_address
```
if above not working, run the command below instead:
```shell
FLASK_APP=dashboard.py flask run --host=ip_address
```
### Launch flask website
open browser url to '<ip_address>:5000'

# Set up Mongo Database in Raspberry Pi
Reference link:
```shell
https://www.donskytech.com/how-to-install-mongodb-on-raspberry-pi/
```

### Update Raspberry Pi
```shell
sudo apt update && sudo apt upgrade -y
```

### Add GPG Key for MongoDB
```shell
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
```

### Add the MongoDB source location
```shell
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```

### After installing, enter the following command to find the following file in Raspberry Pi
```shell
ls -l /etc/apt/sources.list.d/
```

### Update source list
```shell
sudo apt-get update
```

### Install MongoDB
```shell
sudo apt-get install -y mongodb-org=4.4.18 mongodb-org-server=4.4.18 mongodb-org-shell=4.4.18 mongodb-org-mongos=4.4.18 mongodb-org-tools=4.4.18
```

### Run MongoDB
```shell
sudo systemctl start mongod
```

### If everything works well, enter the following command to see the status of the MongoDB
```shell
sudo systemctl status mongod
```

### Should see the following output
```shell
mongod.service - MongoDB Database Server
     Loaded: loaded (/lib/systemd/system/mongod.service; disabled; vendor preset: enabled)
     Active: active (running) since Sun 2023-03-05 13:12:29 PST; 11s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 5589 (mongod)
     CGroup: /system.slice/mongod.service
             └─5589 /usr/bin/mongod --config /etc/mongod.conf

Mar 05 13:12:29 raspberrypi systemd[1]: Started MongoDB Database Server
```

### If an error occurred or the service is not starting, execute the following code
```shell
sudo systemctl daemon-reload
```

### Configure MongoDB to start at reboot
```shell
sudo systemctl enable mongod
```

## Validate MongoDB installation
```shell
mongo
```

## Show Databases
```shell
show dbs
```

## Use/Create Database
```shell
use (name of db)
```

## To show collections
```shell
show collections
```

## To show all data in database collection
```shell
db.getCollection("collection name").find()
```

## To drop collection
```shell
db.(collection name).drop()
```

## Make Mongo available to the network, edit the "/etc/mongod.conf" file and change the bindIp to “0.0.0.0”
```shell
#network interfaces
net:
    port: 27017
    bindIp: 0.0.0.0
```

### Reload mongodb instance
```shell
sudo systemctl restart mongod
```

# Uninstall Mongodb
### Stop MongoDB service
```shell
sudo service mongod stop
```

### Uninstall MongoDB package
```shell
sudo apt-get purge mongodb-org*
```

### Cleanup MongoDB directory
```shell
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
```