import time
import sys  
import datetime
import json
import os
import QIoT

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

bridge_client = bridgeclient()


client = QIoT.setup('./res/resourceinfo.json', '/ssl/')

""" 
	Receive data of QIoT Suite Lite.
"""

#Setting Subscribe is use id <QIoT.subscribeofid("ID", client)>
#It will return topic name

def on_connect(client, userdata, flags, rc):
    global topic_LED
    print("Connected with result code "+str(rc))
    topic_LED = QIoT.subscribeofid("LED", client)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client.on_connect = on_connect
client.on_message = on_message


"""
	Send sensor's data to QIoT Suite Lite by Resourcetype.
"""

#It's use "resourcetypename" to sending data.
#QIoT.sendoftype("resourcetypename", value, client)


while True:
	h0 = bridge_client.get("humidity")
	t0 = bridge_client.get("temperature")

	print "Humidity: " + h0
	print "Temperature: " + t0
	
	t = time.time()
	QIoT.sendoftype("Temperature", t0, client)
	QIoT.sendoftype("Humidity", h0, client)
	time.sleep(1)




