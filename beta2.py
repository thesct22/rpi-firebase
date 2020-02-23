import paho.mqtt.client as mqtt
import subprocess
import datetime
import time

# Broker data
broker = "192.168.132.164"
broker_port = 1883
timeout_reconnect = 60
broker_topic = "#"  #All topics have to be read

# Topic to send payload
topic = "temp/DHT11data"

def on_connect(client, userdata, flags, rc):
    #print("Connect with result code: " + str(rc))
    if int(str(rc)) == 0:
        print("Conexion establecida")
        print ""
    else:
        print("Error result code: " + str(rc))
    #client.subscribe(broker_topic)

def on_message(client, userdata, msg):
    #print "Message topic: " + msg.topic + ", payload: " + str(msg.payload)
    #if msg.topic == topic:
    if msg.topic == "temp/test":
        if str(msg.payload) != "":
            print "Message on: " + str(datetime.datetime.now()) + " - topic: " + msg.topic + ", payload: " + str(msg.payload)
            #client.publish(topic, 30, qos=0, retain=False)
            client.publish(topic, "Reset...", qos=0, retain=False)
    pass

def on_publish(mosq, obj, mid):
    #print("Publish mid: " + str(mid))
    pass

def on_subscribed(mosq, obj, mid, granted_qos):
    print("Subscribed mid: " + str(mid) + ", qos: " + str(granted_qos))

def on_log(mosq, obj, mid, string):
    #print("Log: " + str(string))
    pass

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribed = on_subscribed
client.on_log = on_log

client.connect(broker, broker_port, timeout_reconnect)
client.subscribe(broker_topic, 0)

print "Cliente conectado " + str(datetime.datetime.now())
print ""

client.loop_start()

while True:
    try:
        client.publish(topic, "Hello world", qos=0, retain=False)
        time.sleep(10)

    except KeyboardInterrupt:
            break

client.disconnect()
print("Desconectado")