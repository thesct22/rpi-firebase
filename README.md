# rpi-firebase

All the codes run on a Raspberry Pi

beta1.py and beta2.py connects the Pi to an MQTT client sending temperature data and displays the resulting data.

beta3.py collects data from 3 MQTT data publishers and sends data to a ThingSpeak channel

beta4.py collects 1 temperature data, generates 7 random data and sends all 8 to ThingSpeak.

beta5.py  and beta7.py sends 8 random generated temperature data to ThingSpeak.

beta6.py connects to 8 MQTT data publishers and sends the data to ThingSpeak.

beta8.py sends 8 random generated temperature data to Firebase Real-time Database.

beta9.py connects to 8 MQTT data publishers and sends the data to Firebase.

simple.py receives 8 vent-size data from a ThingSpeak channel and displays it.
