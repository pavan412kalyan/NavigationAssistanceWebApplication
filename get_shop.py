# -*- coding: utf-8 -*-
#https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png
key="AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
my_stores=[[17.445318, 78.68525509999999, 'Ghatkesar'],
 [17.3137596, 78.561889, 'B N Reddy Nagar'],
 [17.3714737, 78.5695016, 'Nagole'],
 [17.3457176, 78.55222959999999, 'LB Nagar'],
 [17.3687826, 78.5246706, 'DSNR'],
 [17.3447337, 78.5182911, 'Champapet'],
 [17.4399295, 78.4982741, 'SC'],
 [17.4138552, 78.57834460000001, 'Boduppal'],
 [17.3227982, 78.5280016, 'Meerpet'],
 [17.4283104, 78.5386101, 'Tarnaka'],
 [17.3730927, 78.49003809999999, 'Malakpet'],
 [17.3174049, 78.5520232, 'Hastinapuram'],
 [17.3730192, 78.547636, 'Kothapet'],
 [17.3852774, 78.52775059999999, 'Ramanthapur'],
 [17.4138277, 78.4397584, 'Banjara Hills'],
 [17.4420325, 78.6502201, 'Pocharam'],
 [17.2738816, 78.54866489999999, 'Nadergul']]

#my_stores=[[17.470531, 78.576907,'ECIL'],[17.450800, 78.534441,Malkajgiri]]
                      

#my_stores=[[17.3852774, 78.52775059999999, 'Ramanthapur'],
# [17.4138277, 78.4397584, 'Banjara Hills'],
# [17.4420325, 78.6502201, 'Pocharam'],
# [17.2738816, 78.54866489999999, 'Nadergul']]

x=0
import numpy as np
details_shops=[]
pages_json=[]
details_shops_set=set()#set to remove duplicate places
for s in my_stores :
    url_shops="https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(s[0])+","+str(s[1])+"&radius=2000&type=store&key="+key 
    import urllib.request, json 
    with urllib.request.urlopen(url_shops) as url:              
        data = json.loads(url.read().decode())
        pages_json.append(data)
        x=0
        
    if data["status"] == "OK" :
        for i in range(len(data['results'])) :
            name_s=data['results'][i]['name']
            print(name_s)
            x=x+1
            print(s[2],x)
            lats_s=data['results'][i]['geometry']['location']['lat']
            lngs_s=data['results'][i]['geometry']['location']['lng']
            vicinity_s=data['results'][i]['vicinity']
            id_s=data['results'][i]['place_id']
            details_shops.append([name_s,lats_s,lngs_s,vicinity_s,id_s])
            details_shops_set.add((name_s,lats_s,lngs_s,vicinity_s,id_s))


details_shops=list(details_shops_set)
    
details_shops_list=[]      
   
for i in range(len(details_shops)) :
        details_shops_list.append(list(details_shops[i]))




###########################################
#import json
#with open('all_340_stores.txt', 'w') as outfile:
#    json.dump(details_shops_list, outfile)

#####################################
import mysql.connector

lat_from_db=[]
lng_from_db=[]
store_db=[]
details_name_forjs_v=[]
mydb = mysql.connector.connect(
  host="localhost",
  user="pavan",
  passwd="1234"
)

mycursor = mydb.cursor()
mycursor.execute("use store")

mycursor.execute("CREATE TABLE IF NOT EXISTS shop_details(name_s  VARCHAR(80) NOT NULL  ,lats_s NUMERIC(17,14) NOT NULL ,lngs_s   NUMERIC(17,14) NOT NULL ,vicinity_s VARCHAR(200) NOT NULL ,id_s VARCHAR(40) NOT NULL PRIMARY KEY);")

insert_stmt = (
  "REPLACE INTO shop_details(name_s,lats_s,lngs_s,vicinity_s,id_s)"
  "VALUES (%s, %s, %s, %s,%s)"
)

for i in range(len(details_shops_list)) :
    print(i)
   
    data = (details_shops_list[i][0],details_shops_list[i][1],details_shops_list[i][2],details_shops_list[i][3],details_shops_list[i][4])  
    print(data)
    mycursor.execute(insert_stmt, data)

print("affected rows = {}".format(mycursor.rowcount))

########################## For retring data from DB

details_name_forjs_v=[]

mycursor.execute("SELECT * FROM shop_details")


myresult = mycursor.fetchall()
save_result=myresult
#x=myresult[0][0]
for i in range(len(myresult)):
    details_name_forjs_v.append([myresult[i][0],float(myresult[i][1]),float(myresult[i][2]),1])
    


details_name_forjs=[]        



######this is for json obj in javascript page markers
 
for det in details_name_forjs_v :
    details_name_forjs.append([det[0],det[1],det[2],1])
    
    



       