# RPi
import time
import paho.mqtt.client as mqtt
import sys
from firebase import firebase

firebase= firebase.FirebaseApplication('https://air-conditioning-12b11.firebaseio.com/')
global ab
global ac
global ad
def on_connect(client, userdata, flags, rc):
    if rc==0:
       print("Connected with result code " + str(rc))
       print("connected OK")
       for i in range(1,4):
           client.subscribe("/esp8266/temp"+str(i))
    else:
        print("Bad connection Returned code=",rc)
# The callback for when a PUBLISH message is received from the server. 
def on_message(client, userdata, msg): 
    print(msg.topic+" "+str( msg.payload)) 
   # Check if this is a message for the Pi LED. 
    if msg.topic == '/esp8266/temp2': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 2 is: "+str(msg.payload))
        global ac
        ac=int(msg.payload)
        print ac
    if msg.topic == '/esp8266/temp3': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 3 is: "+str(msg.payload))
        global ad
        ad=int(msg.payload)
        print ad
    if msg.topic == '/esp8266/temp1': 
       # Look at the message data and perform the appropriate action. 
        print("temperature at 1 is: "+str(msg.payload))
        global ab
        ab=int(msg.payload)
        print ab
           # Create MQTT client and connect to localhost, i.e. the Raspberry Pi running 
# this script and the MQTT server. 
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
ab=0
ac=0
ad=0
# Connect to the MQTT server and process messages in a background thread. 
try:
    client.loop_start()
    print("Connecting to broker")
    client.connect('localhost', 1883, 60)     #connect to broker
    print("in Main Loop")
    while 1:
        # Sending the data to thingspeak
        global ab
        global ac
        global ad
        result = firebase.post('https://air-conditioning-12b11.firebaseio.com/', {'temp1':str(ab),'temp2':str(ac),'temp3':str(ad),'temp4':str(ae),'temp5':str(af),'temp6':str(ag),'temp7':str(ah),'temp8':str(ai)})
        time.sleep(2)
    
except KeyboardInterrupt:
    client.loop_stop()    #Stop loop 
    client.disconnect() # disconnect

