import time
import sys
import urllib2
import random
from firebase import firebase

firebase= firebase.FirebaseApplication('https://air-conditioning-12b11.firebaseio.com/')
f=0
while 1:
	f=(f+1)%4
	ab=random.randrange(20,35,1)
	ac=random.randrange(20,35,1)
	ad=random.randrange(20,35,1)
	ae=random.randrange(20,35,1)
	af=random.randrange(20,35,1)
	ag=random.randrange(20,35,1)
	ah=random.randrange(20,35,1)
	ai=random.randrange(20,35,1)
	result = firebase.put('https://air-conditioning-12b11.firebaseio.com/','temp', {'temp1':str(ab),'temp2':str(ac),'temp3':str(ad),'temp4':str(ae),'temp5':str(af),'temp6':str(ag),'temp7':str(ah),'temp8':str(ai)})
	time.sleep(0.5)
	if(f==3):
            print(ab)
            print(ac)
            print(ad)
            print(ae)
            print(af)
            print(ag)
            print(ah)
            print(ai)
            print("-------------------")