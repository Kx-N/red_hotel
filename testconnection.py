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



@app.route('/search_user_id',methods=['GET'])
def searching():
      arg = request.args.get('user')
      arg2 = str(arg)
      ans = conf.cursor()
      ans.execute("SELECT  firstname FROM customer WHERE ID = "+arg)
      #print(ans.fetchone())
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
       return {}
      else :
       ans.execute("SELECT r.room_id, r.room_type_id, rt.price FROM room r, roomtype rt WHERE NOT EXISTS ( SELECT DISTINCT room_id FROM book_room br WHERE (((to_date(br.c_in,'DD/MM/YY') >= to_date('"+i+"','DD/MM/YY')) AND (to_date(br.c_in,'DD/MM/YY') < to_date('"+o+"','DD/MM/YY'))) OR ((to_date(br.c_out,'DD/MM/YY') > to_date('"+i+"','DD/MM/YY')) AND (to_date(br.c_out,'DD/MM/YY') <= to_date('"+o+"','DD/MM/YY'))) OR (to_date('"+i+"','DD/MM/YY') BETWEEN to_date(br.c_in,'DD/MM/YY') AND to_date(br.c_out,'DD/MM/YY'))) AND r.room_id = br.room_id) AND rt.room_type_id  = r.room_type_id")
       return jsonify(ans.fetchall())
      #return i


if __name__ == "__main__":
  app.run(host='0.0.0.0', port='5000', debug=True)


