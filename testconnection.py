import cx_Oracle
#import db_config
import os
import pandas as pd
import json
from flask_cors import CORS,cross_origin
from flask import Flask, request,jsonify
from flask import Flask, request, abort
from datetime import datetime

app = Flask(__name__)
CORS(app)
os.environ['TNS_ADMIN'] = '/Users/kx/instant/network/admin'
print(os.environ['TNS_ADMIN'])
conf = cx_Oracle.connect('ADMIN','1Q2w3e4r5t6y',"dtb_high")
#query = 'SELECT * from customer'
#data_train = pd.read_sql(query, con=conf)


def search_id(fname,lname):
     query= conf.cursor()
     select = query.execute("SELECT cust_id  FROM ADMIN.customer WHERE firstname ='"+fname+"' AND lastname = '"+lname+"'")
     q = select.fetchone()
     c = 0
     query.close()
     for i in q:
      c = c+1
     if(c == 0):
      return -1;
     else:
      return q[0]



def create_booking(customer_id , room_count ,service_id ,book_date):
     query2  = conf.cursor()
     max_id = conf.cursor()
     max_id.execute("SELECT MAX(booking_id) FROM ADMIN.booking")
     m_id = (max_id.fetchone())[0]+1
     query2.execute("INSERT INTO ADMIN.BOOKING (  BOOKING_ID,PAYMENT_ID,CUST_ID,ROOM_COUNT,BOOK__DATE,REVIEW_ID,SERVICE_TYPE) VALUES("+str(m_id)+",null,"+str(customer_id)+","+str(room_count)+",to_date('"+str(book_date)+"','DD/MM/YY'),"+"null,"+str(service_id)+")")
     #query2.execute("INSERT INTO ADMIN.BOOKING (  BOOKING_ID,PAYMENT_ID,CUST_ID,ROOM_COUNT,BOOK__DATE,REVIEW_ID,SERVICE_TYPE) VALUES("+str(8)+",null,"+str(1)+","+str(2)+",to_date('11/01/2024','DD/MM/YY'),"+"null,"+str(15)+")")
     conf.commit()
     max_id.close()
     query2.close()
     return m_id


def create_new_user(fname,lname,gender,age,tel,email):
     query = conf.cursor()
     query2 =conf.cursor()
     max_user_id = -1
     statement = "SELECT MAX(cust_id) FROM ADMIN.CUSTOMER"
     query.execute(statement)
     max_user_id = query.fetchone()
     pay_id = max_user_id[0]
     #print(max_user_id[0])
     statement = "INSERT INTO ADMIN.CUSTOMER (CUST_ID,FIRSTNAME,LASTNAME,GENDER,AGE,TELEPHONE,EMAIL) VALUES ("+str(pay_id+1)+",'"+fname+"','"+lname+"','"+gender+"','"+str(age)+"','"+tel+"','"+email+"')"
     print(statement)
     query2.execute(statement)
     conf.commit()
     query.close()
     query2.close()
     return max_user_id[0]+1 



def create_bookroom(booking_id,cin,cout,person,room_id):
     query2=conf.cursor()
     max_id=conf.cursor()
     max_id.execute("SELECT MAX(book_room_id) FROM ADMIN.book_room")
     book_room_id  = (max_id.fetchone())[0]+1
     statement = ("INSERT INTO ADMIN.BOOK_ROOM ( BOOK_ROOM_ID,C_IN,C_OUT,PERSON_AMOUNT,ROOM_ID,BOOKING_ID) VALUES("+str(book_room_id)+",to_date('"+str(cin)+"','DD/MM/YY')"+",to_date('"+str(cout)+"','DD/MM/YY'),"+str(person)+","+str(room_id)+","+str(booking_id)+")")
     print(statement)
     query2.execute(statement)
     query2.close()
     max_id.close()
     conf.commit()
     


def cal_price(roomid,service):
     lis = {}
     query = conf.cursor()
     r ="-1"
     for i in roomid :
      r = r+","+str(i)
     statement = "SELECT rt.price_per_night FROM ADMIN.ROOMTYPE rt , ADMIN.ROOM r WHERE r.room_id IN "+"("+r+")"+" AND rt.room_type_id = r.room_type_id"
     query.execute(statement)
     q = query.fetchall()
     cost = 0
     for i in q :
      cost = cost+int(i[0])
     query.close()
     return cost+(200*service)

     
def create_payment(price,cust_id):
     query  = conf.cursor()
     query.execute("SELECT MAX(payment_id) FROM ADMIN.payment")
     max_payment_id = query.fetchone()
     statement = "INSERT INTO ADMIN.PAYMENT ( PAYMENT_ID,AMOUNT,METHOD,DATEPAY,CUST_ID) VALUES ("+str(max_payment_id[0]+1)+","+str(price)+",null,null,"+str(cust_id)+")"
     #print(statement)
     query.execute(statement)
     conf.commit()
     query.close()
     return max_payment_id[0]+1
     
@app.route('/dummy', methods=['POST'])
def dum():     
     data = request.json
     print(data["roomid"])
     #lis = []
     #for i in data : 
     #lis.append(i)
     #lis.append("https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators#:~:text=0.0%20is%20returned.-,Power,multiplied%20by%20itself%203%20times.")
     return data["roomid"]


@app.route('/search_user_id',methods=['GET'])
def searching():
      arg = request.args.get('user')
      arg2 = str(arg)
      ans = conf.cursor()
      ans.execute("SELECT  firstname FROM customer WHERE ID = "+arg)
      #print(ans.fetchone())
      ans.close()
      return jsonify(ans.fetchone()) 



@app.route('/search_av_room',methods=['POST'])
def avroom():
      data = request.json
      i = data["checkin"]
      i2 = i
      o = data["checkout"]
      o2 = o
      fmt = '%d/%m/%Y %H:%M:%S'
      t = datetime.now()
      ans = conf.cursor()
      #ans.execute(SELECT r.room_id , r.room_type_id , rt.price FROM room as r , roomtype as rt , book_room as br WHERE br. )
      if(datetime.strptime(i2+' 00:00:00', fmt)<datetime.now() or datetime.strptime(o2+' 00:00:00', fmt)<datetime.now()):
       return jsonify({})
      else :
       #ans.execute("SELECT r.room_id, r.room_type_id, rt.price FROM room r, roomtype rt WHERE NOT EXISTS ( SELECT DISTINCT room_id FROM book_room br WHERE (((to_date(br.c_in,'DD/MM/YY') >= to_date('"+i+"','DD/MM/YY')) AND (to_date(br.c_in,'DD/MM/YY') < to_date('"+o+"','DD/MM/YY'))) OR ((to_date(br.c_out,'DD/MM/YY') > to_date('"+i+"','DD/MM/YY')) AND (to_date(br.c_out,'DD/MM/YY') <= to_date('"+o+"','DD/MM/YY'))) OR (to_date('"+i+"','DD/MM/YY') BETWEEN to_date(br.c_in,'DD/MM/YY') AND to_date(br.c_out,'DD/MM/YY'))) AND r.room_id = br.room_id) AND rt.room_type_id  = r.room_type_id")
       ans.execute("SELECT r.room_id, r.room_type_id, rt.price_per_night FROM room r, roomtype rt WHERE NOT EXISTS ( SELECT DISTINCT room_id FROM book_room br WHERE (((to_date(br.c_in,'DD/MM/YY') >= to_date('"+i+"','DD/MM/YY')) AND (to_date(br.c_in,'DD/MM/YY') < to_date('"+o+"','DD/MM/YY'))) OR ((to_date(br.c_out,'DD/MM/YY') > to_date('"+i+"','DD/MM/YY')) AND (to_date(br.c_out,'DD/MM/YY') <= to_date('"+o+"','DD/MM/YY'))) OR (to_date('"+i+"','DD/MM/YY') BETWEEN to_date(br.c_in,'DD/MM/YY') AND to_date(br.c_out,'DD/MM/YY'))) AND r.room_id = br.room_id) AND rt.room_type_id  = r.room_type_id")
       ret = ans.fetchall()
       ans.close()
       return jsonify(ret)
      #return i


@app.route('/prompt_pay',methods=['PUT'])
def pay(): 
     arg = request.args.get('book_id')
     arg2 = str(arg)
     metarg = request.args.get('met')
     metstr = str(metarg)
     query = conf.cursor()
     statement = "SELECT payment_id FROM ADMIN.BOOKING WHERE booking_id = '"+str(arg2)+"'"
     query.execute(statement)
     pay_id  = query.fetchone()
     #print(pay_id[0])
     fmt = '%d/%m/%Y'
     d = datetime.now()
     pay_day = d.strftime(fmt)
     #print(pay_day)
     statement = "UPDATE ADMIN.PAYMENT SET method = '"+str(metstr)+"', datepay  = to_date('"+str(pay_day)+"','DD/MM/YY') WHERE PAYMENT_ID = '"+str(pay_id[0])+"'"
     #print(statement)
     query.execute(statement)
     conf.commit()
     query.close()
     return str("payment successful")
     
      


@app.route('/create_booking',methods=['POST'])
def booking():
     data = request.json
     fname = data["firstname"]
     lname = data["lastname"]
     roomid = data["roomid"]
     query = conf.cursor()
     query.execute("select count(*) FROM ADMIN.customer WHERE firstname ='"+fname+"' AND lastname ='"+lname+"'")
     count_user = query.fetchone()
     #print("id : "+str(check))
     if(count_user[0] > 0):
      check = search_id(fname,lname)
      room_count = 0
      for i in data["roomid"]:
       room_count = room_count+1
      service=0
      service=service+(2**int((data["driver"])))+(2**int(data["massage"]))+(2**int(data["breakfast"]))+(2**int(data["dinner"]))
      book_id = create_booking(check,room_count,service,data["bookdate"])     
      for i in data["roomid"]:
       create_bookroom(book_id,data["checkin"],data["checkout"],data["person"],i)
      price = cal_price(roomid,int(data["driver"])+int(data['massage'])+int(data['breakfast'])+int(data['dinner']))
      payment = create_payment(price,check)
      statement = "UPDATE ADMIN.BOOKING SET payment_id ="+str(payment)+" WHERE BOOKING_ID ="+str(book_id)
      query.execute(statement)
      conf.commit()
      query.close()
      return jsonify(["92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = cash","92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = mastercard","92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = visa","92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = bitcoin"])
     else :
      user = create_new_user(fname,lname,data["gender"],data["age"],data["tel"],data["email"])
      room_count = 0
      for i in data["roomid"]:
       room_count = room_count+1
      service=0
      service=service+(2**int((data["driver"])))+(2**int(data["massage"]))+(2**int(data["breakfast"]))+(2**int(data["dinner"])) 
      book_id = create_booking(user,room_count,service,data["bookdate"]) 
      for i in data["roomid"]:
       create_bookroom(book_id,data["checkin"],data["checkout"],data["person"],i)
      price = cal_price(roomid,int(data["driver"])+int(data['massage'])+int(data['breakfast'])+int(data['dinner']))
      payment = create_payment(price,user)
      statement = "UPDATE ADMIN.BOOKING SET payment_id ="+str(payment)+" WHERE BOOKING_ID ="+str(book_id)
      query.execute(statement)
      conf.commit()
      query.close()
      return jsonify(["92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = cash","92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = mastercard","92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = visa","92.168.1.38:5000/prompt_pay?book_id="+str(book_id)+"&met = bitcoin"])
      #return str(book_id)

if __name__ == "__main__":
  app.run(host='192.168.1.38', port='5000', debug=True)


