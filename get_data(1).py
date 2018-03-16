import urllib2
import json
def main():
	CHANNEL_ID="431254"
	READ_API_KEY="CHYUAS6YQ96COFUO"
	conn=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID,READ_API_KEY))
	response=conn.read()
	status=int(conn.getcode())
	print "HTTP status = %d"%status
	data=json.loads(response)
	for x in data:
		print("%s : %s"%(x,data[x]))
		print("\n")
	conn.close()
if __name__=='__main__':
	main()
