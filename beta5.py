import time
import sys
import urllib2
import random
# Enter Your API key here
myAPI = '10QFJTA1UGI77J7A' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

while 1:
	ab=random.randrange(20,35,1)
	ac=random.randrange(20,35,1)
	ad=random.randrange(20,35,1)
	ae=random.randrange(20,35,1)
	af=random.randrange(20,35,1)
	ag=random.randrange(20,35,1)
	ah=random.randrange(20,35,1)
	ai=random.randrange(20,35,1)
	conn = urllib2.urlopen(baseURL+'&field1='+str(ab)+'&field2='+str(ac)+'&field3='+str(ad)+'&field4='+str(ae)+'&field5='+str(af)+'&field6='+str(ag)+'&field7='+str(ah)+'&field8='+str(ai))
	print conn.read()
	conn.close()
	time.sleep(10)
