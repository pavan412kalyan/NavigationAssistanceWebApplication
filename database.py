# -*- coding: utf-8 -*-

print(warehouse_address)

import webbrowser
webbrowser.open('openmaps.html', new=2)





#####################################################
#Linear Distance 
from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...    


distance(17.3174049,78.5520232,17.3446619,78.5284294)

######################################################

import psycopg2
import gmplot

# Connect to the database
db_conn = psycopg2.connect("dbname='database_name' host='host_address' user='username' password='your_password'")

#Set the cursor
cur = db_conn.cursor()

# Execute the database query. I am fetching business locations in a particular zip.
cur.execute("select latitude, longitude from business where postal_code='89109';")

# Fetch all the data returned by the database query as a list
lat_long = cur.fetchall()

# Initialize two empty lists to hold the latitude and longitude values
latitude = []
longitude = [] 

# Transform the the fetched latitude and longitude data into two separate lists
for i in range(len(lat_long)):
	latitude.append(lat_long[i][0])
	longitude.append(lat_long[i][1])

# Initialize the map to the first location in the list
gmap = gmplot.GoogleMapPlotter(latitude[0],longitude[0])

# Draw the points on the map. I created my own marker for '#FF66666'. 
# You can use other markers from the available list of markers. 
# Another option is to place your own marker in the folder - 
# /usr/local/lib/python3.5/dist-packages/gmplot/markers/
gmap.scatter(latitude, longitude, '#FF6666', edge_width=10)

# Write the map in an HTML file
gmap.draw('map.html')

# Close the cursor and the database connection 
cur.close()
db_conn.close()



#########################################################################
#http://www.convertcsv.com/csv-to-sql.htm
import mysql.connector

lat_from_db=[]
lng_from_db=[]
store_db=[]
mydb = mysql.connector.connect(
  host="localhost",
  user="pavan",
  passwd="1234"
)

mycursor = mydb.cursor()
mycursor.execute("use store")

mycursor.execute("SELECT * FROM store_adds")

myresult = mycursor.fetchall()
x=myresult[0][0]
#x=myresult[0][0]
for i in range(len(myresult)):
    lat_from_db.append(float(myresult[i][0]))
    lng_from_db.append(float(myresult[i][1]))
    store_db.append(myresult[i][2])
   
print(float(lat_from_db[0]))
print(lng_from_db)

       
import mysql.connector

lat_from_db=[]
lng_from_db=[]
store_db=[]
mydb = mysql.connector.connect(
  host="localhost",
  user="pavan",
  passwd="1234"
)

mycursor = mydb.cursor()
mycursor.execute("use store")

mycursor.execute("")


















