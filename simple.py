import urllib2,json
def main():
    conn = urllib2.urlopen("https://api.thingspeak.com/channels/860734/feeds/last.json?api_key=YUROCSUB7HDJUJT1&results=2")

    response = conn.read()
    print ("http status code=%s" % (conn.getcode()))
    data=json.loads(response)
    print (data['field1'])
    print (data['field2'])
    print (data['field3'])
    print (data['field4'])
    print (data['field5'])
    print (data['field6'])
    print (data['field7'])
    print (data['field8'])
    conn.close()



if __name__ == '__main__':
    main()
