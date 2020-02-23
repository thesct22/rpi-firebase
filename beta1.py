# RPi
import time
import paho.mqtt.client as mqtt 
def on_connect(client, userdata, flags, rc):
    if rc==0:
       print("Connected with result code " + str(rc))
       print("connected OK")
       client.subscribe("/esp8266/temp1")
    else:
        print("Bad connection Returned code=",rc)

# The callback for when a PUBLISH message is received from the server. 
def on_message(client, userdata, msg): 
   print(msg.topic+" "+str( msg.payload)) 
   # Check if this is a message for the Pi LED. 
   if msg.topic == '/esp8266/temp1': 
       # Look at the message data and perform the appropriate action. 
            print("temperature at 1 is: "+str(msg.payload))
           # Create MQTT client and connect to localhost, i.e. the Raspberry Pi running 
# this script and the MQTT server. 
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 

# Connect to the MQTT server and process messages in a background thread. 
try:
    client.loop_start()
    print("Connecting to broker")
    client.connect('localhost', 1883, 60)     #connect to broker
    while 1:
        time.sleep(1)
    #while not client.connected_flag: #wait in loop
     #   print(".")
    #  time.sleep(1)
    print("in Main Loop")
except KeyboardInterrupt:
    client.loop_stop()    #Stop loop 
    client.disconnect() # disconnect
