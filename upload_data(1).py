import urllib2
import json
CHANNEL_ID="431254"
WRITE_API_KEY="UHA1TPBAJBA3OI6K"
base_URL="http://api.thingspeak.com/update?api_key=%s"%(WRITE_API_KEY)
f_id=raw_input("Enter the farmer id :")
p_id=raw_input("enter the product id :")
p_name=raw_input("ENter the product name :")
p_quan=raw_input("ENter the product weight :")
p_price=raw_input("Enter the price :")
conn=urllib2.urlopen(base_URL+"&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s"%(f_id,p_id,p_name,p_quan,p_price))
print "Data uploaded successfully"    
conn.close()
