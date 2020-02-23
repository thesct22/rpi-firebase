# RPi
import time
import sys
import urllib2
import json
import random
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=10QFJTA1UGI77J7A'
global ab,ac,ad,ae,af,ag,ah,ai
ab=0
ac=0
ad=0
ae=0
af=0
ag=0
ah=0
ai=0
# Connect to the MQTT server and process messages in a background thread. 
try:
    while 1:
        # Sending the data to thingspeak
        global ab,ac,ad,ae,af,ag,ah,ai
        ae=random.randrange(22,25,1)
        af=random.randrange(22,25,1)
        ag=random.randrange(22,25,1)
        ah=random.randrange(22,25,1)
        ai=random.randrange(22,25,1)
        ab=random.randrange(22,25,1)
        ad=random.randrange(22,25,1)
        ae=random.randrange(22,25,1)
        ac=random.randrange(22,25,1)
        conn = urllib2.urlopen(baseURL+'&field1='+str(ab)+'&field2='+str(ac)+'&field3='+str(ad)+'&field4='+str(ae)+'&field5='+str(af)+'&field6='+str(ag)+'&field7='+str(ah)+'&field8='+str(ai))
        #print conn.read()
        # Closing the connection
        conn.close()
        print("Received message",ab)
        print("Received message",ac)
        print("Received message",ad)
        print("Received message",ae)
        print("Received message",af)
        print("Received message",ag)
        print("Received message",ah)
        print("Received message",ai)
        print("Sending:",ab,", ",ac,", ",ad,", ",ae,", ",af,", ",ag,", ",ah,", ",ai)
        time.sleep(10)
        conn1 = urllib2.urlopen("https://api.thingspeak.com/channels/860734/feeds/last.json?api_key=YUROCSUB7HDJUJT1&results=2")
        response = conn1.read()
        print ("http status code=%s" % (conn.getcode()))
        data=json.loads(response)
        print("Vent values:")
        print (data['field1'])
        print (data['field2'])
        print (data['field3'])
        print (data['field4'])
        print (data['field5'])
        print (data['field6'])
        print (data['field7'])
        print (data['field8'])
        conn1.close()

        
    #while not client.connected_flag: #wait in loop
     #   print(".")
    #  time.sleep(1)
    print("in Main Loop")
except KeyboardInterrupt:
    client.loop_stop()    #Stop loop 
    client.disconnect() # disconnect
