from flask import Flask,render_template,request
app=Flask(__name__)
import urllib2
import json
import smtplib

Farmer_id_p=[]
Product_id=[]
Product_name=[]
Quantity=[]
Price=[]

# wheat = 31 ----- Rice = 21


Farmer_id=[]
Farmer_name=[]
Address=[]
Pincode=[]
phno=[]

total_product_list=['Wheat','Rice']

control=0

'''
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login("vijayanv31@gmail.com", "kjkszpjlavenjqhesoaymokllaaa")
 
msg = "Demo Mail from SMART FARMER DEVICE on product order confirmation"
server.sendmail("vijayanv31@gmail.com", "veenetha.1997@gmail.com", msg)
server.quit()
'''

@app.route("/")
def main():
	CHANNEL_ID1="431236"
	READ_API_KEY1="1UGLU0A7XXIKI1PC"
	conn1=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID1,READ_API_KEY1))
	response1=conn1.read()
	status1=int(conn1.getcode())
	data1=json.loads(response1)
	total1=int(data1['channel']['last_entry_id'])

	for x in range(0,total1):
		Farmer_id.append(int(data1['feeds'][x]['field1']))
		Farmer_name.append(data1['feeds'][x]['field2'])
		Address.append(data1['feeds'][x]['field3'])
		Pincode.append(data1['feeds'][x]['field4'])
		phno.append(data1['feeds'][x]['field5'])
	CHANNEL_ID="431254"
	READ_API_KEY="CHYUAS6YQ96COFUO"
	conn=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID,READ_API_KEY))
	response=conn.read()
	status=int(conn.getcode())
	data=json.loads(response)
	total=int(data['channel']['last_entry_id'])

	for x in range(0,total):
		Farmer_id_p.append(data['feeds'][x]['field1'])
		Product_id.append(int(data['feeds'][x]['field2']))
		Product_name.append(data['feeds'][x]['field3'])
		Quantity.append(data['feeds'][x]['field4'])
		Price.append(data['feeds'][x]['field5'])

	control=0

	data={
	'farmer_id_p': Farmer_id_p,
	'farmer_id': Farmer_id,
	'farmer_name': Farmer_name,
	'address': Address,
	'pincode': Pincode,
	'phno': phno,
	'product_id': Product_id,
	'product_name': Product_name,
	'quantity': Quantity,
	'price': Price,
	'total': total,
	'control':0
	}
	return render_template("buddy.html",**data)

@app.route("/filter",methods = ['POST', 'GET'])
def main_filter():
	if (request.method=="POST"):
		filters=str(request.form['filter']).lower()
	control=1
	CHANNEL_ID1="431236"
	READ_API_KEY1="1UGLU0A7XXIKI1PC"
	conn1=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID1,READ_API_KEY1))
	response1=conn1.read()
	status1=int(conn1.getcode())
	data1=json.loads(response1)
	total1=int(data1['channel']['last_entry_id'])
	unit_pid=[]
	for x in range(0,total1):
		Farmer_id.append(int(data1['feeds'][x]['field1']))
		Farmer_name.append(data1['feeds'][x]['field2'])
		Address.append(data1['feeds'][x]['field3'])
		Pincode.append(data1['feeds'][x]['field4'])
		phno.append(data1['feeds'][x]['field5'])
	CHANNEL_ID="431254"
	READ_API_KEY="CHYUAS6YQ96COFUO"
	conn=urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"%(CHANNEL_ID,READ_API_KEY))
	response=conn.read()
	status=int(conn.getcode())
	data=json.loads(response)
	total=int(data['channel']['last_entry_id'])

	for x in range(0,total):
		Farmer_id_p.append(data['feeds'][x]['field1'])
		Product_id.append(int(data['feeds'][x]['field2']))
		Product_name.append(data['feeds'][x]['field3'])
		Quantity.append(data['feeds'][x]['field4'])
		Price.append(data['feeds'][x]['field5'])

	data={
	'unit_pid':unit_pid,
	'farmer_id_p': Farmer_id_p,
	'farmer_id': Farmer_id,
	'farmer_name': Farmer_name,
	'address': Address,
	'pincode': Pincode,
	'phno': phno,
	'product_id': Product_id,
	'product_name': Product_name,
	'quantity': Quantity,
	'price': Price,
	'total': total,
	'filters':filters,
	'control':1
	
	}
	return render_template("buddy.html",**data)

@app.route("/login")
def login():
	a={}
	return render_template("login.html",**a)

@app.route("/reg",methods = ['POST','GET'])
def regnow():
	if(request.method=="POST"):
		name=request.form['name']
		email=request.form['email']
		password=request.form['password']
		address=request.form['address']
		phno=request.form['phno']
		pincode=request.form['pincode']
		base_URL="http://api.thingspeak.com/update?api_key=%s"%("VQYWXWXK2AQDIAW9")
		conn=urllib2.urlopen(base_URL+"&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s"%(pincode,name,address,phno,email))
		conn.close()
	a={}
	return render_template("register.html",**a)


@app.route("/getaccess/<fid>/<pid>")
def getaccess(fid,pid):
	id=Farmer_id.index(int(fid))
	fid=Farmer_id[id]
	fname=Farmer_name[id]
	faddr=Address[id]
	fpin=Pincode[id]
	fphno=phno[id]

	p_id=Product_id.index(int(pid))
	pid=Product_id[p_id]
	pname=Product_name[p_id]
	pquan=Quantity[p_id]
	pprice=Price[p_id]

	a={
	'fid':fid,
	'fname':fname,
	'faddr':faddr,
	'fpin':fpin,
	'fphno':fphno,
	'pid':pid,
	'pname':pname,
	'pquan':pquan,
	'pprice':pprice
	}
	return render_template("farmer_confirmation.html",**a)


@app.route("/form")
def form():
	d={}
	return render_template("form.html",**d)
@app.route("/buddy",methods=['POST'])
def reg():
	if request.method=='POST': 
		product=request.form['hmm']
		price=request.form['k']
		c_data={
		'p1':product,
		'p2':price 
		}
		return render_template("index.html",**c_data)
@app.route("/upload/<a1>/<a2>/<a3>")
def upload(a1,a2,a3):
	import urllib2
	import json
	CHANNEL_ID="402974"
	WRITE_API_KEY="1YHFQW0FQ2J8TR66"
	base_URL="http://api.thingspeak.com/update?api_key=%s"%(WRITE_API_KEY)
	p_name=a1
	p_quan=a2
	p_price=a3
	conn=urllib2.urlopen(base_URL+"&field1=%s&field2=%s&field3=%s"%(p_name,p_quan,p_price))
	conn.close()
	return "uploaded successfully"
@app.route("/get/<newname>")  
def getnew(newname):
	myname=newname   
	data_update={
	"change_name": myname 
	}
	return render_template("update.html",**data_update)  

	
if __name__=="__main__":
	app.run(host='127.0.0.1',port=8070,debug=True)    
