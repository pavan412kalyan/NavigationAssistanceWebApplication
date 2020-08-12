# -*- coding: utf-8 -*-

from scipy.spatial import distance_matrix
import pandas as pd
data = [[5, 7], [7, 3]]
ctys = ['Boston', 'Phoenix']
dfs = pd.DataFrame(data, columns=ctys, index=ctys)








############################################
###tlat and Lonf

stores=['']

address='Ghatkesar'
url2="https://maps.googleapis.com/maps/api/geocode/json?&address="+address+"&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8 "     

import urllib.request, json 
with urllib.request.urlopen(url2) as url:
    data = json.loads(url.read().decode())
    print(data['results'][0]['address_components'][0]['short_name'])
    print(data['results'][0]['geometry']['location'])
    print(data['results'][0]['geometry']['location']['lat'])
    print(data['results'][0]['geometry']['location']['lng'])
    
    
    
#####################################################################################
#Multiple Adderess
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# step 1to get location address
stores=['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet']
#address='meerpet'
locations=[]
location_address=[]
lats_list=[]
longs_list=[]
store_name=[]
store_name_forjs=[]

for address in stores :
    url2="https://maps.googleapis.com/maps/api/geocode/json?&address="+address+"&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8 "     
    import urllib.request, json 
    with urllib.request.urlopen(url2) as url:
              
        data = json.loads(url.read().decode())
        print(data['results'][0]['address_components'][0]['short_name'])
        print(data['results'][0]['geometry']['location'])
        name=data['results'][0]['address_components'][0]['short_name']
        lat=data['results'][0]['geometry']['location']['lat']
        long=data['results'][0]['geometry']['location']['lng']
        store_name.append([lat,long,address])
        store_name_forjs.append([address,lat,long,1])

        
        lats_list.append(lat)
        longs_list.append(long)       
        locations.append([lat,long])
        location_address.append([lat,long,name])      
        print(data['results'][0]['geometry']['location']['lat'])
        print(data['results'][0]['geometry']['location']['lng'])
                        
#locations.remove([])    
print(locations) 
print(location_address)   
                    
from scipy.spatial import distance_matrix
import pandas as pd

df = pd.DataFrame(locations, columns=['lat', 'lon'], index=stores)## as a matrix
#######################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Distance Matrix creations 
#% step 2 for calculation of distance

import urllib.request, json 

#url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+origins+"&destinations="+destinations+"&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
distancematrix=[]
for  i in range(len(locations)) :   
     origins=str(locations[i][0]) +"," + str(locations[i][1])
     for j in range(len(locations)):
         
         destinations=str(locations[j][0]) +"," + str(locations[j][1])
         print(origins)
         print(destinations)
         url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+origins+"&destinations="+destinations+"&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"

         with urllib.request.urlopen(url1) as url: 
             
             data = json.loads(url.read().decode())    
             if data['rows'][0]['elements'][0]["status"] == "OK" :
                                             
                 print(data['rows'][0]['elements'][0]['distance']['text'])
                 distance=data['rows'][0]['elements'][0]['distance']['text']
                 print(data['rows'][0]['elements'][0]['duration']['text'])
                 if i==j :
                     distancematrix.append("0")
                
                 else :
                     distancematrix.append(distance)
                                      


                 
                 
                 
             elif  data['rows'][0]['elements'][0]["status"] == "ZERO_RESULTS" :
                 print("No routes found")
 
     print(i)          
                
################                 
import numpy as np
import pandas as pd
import math
print(distancematrix)
y=len(locations)
int_distancematrix=[]####run this to empty
final_matrix=[]
for i in range(len(distancematrix)) :
    int_distancematrix.append(float(distancematrix[i].replace("km","")))
for i in range(len(distancematrix)) :
    final_matrix.append((math.floor(int_distancematrix[i])))
    

dms=np.reshape(final_matrix, (y,y))
print(dms)
          
dfs_chart = pd.DataFrame(dms, columns=stores, index=stores)
print(dfs_chart)         
         

###RUn dms on console and paste in distance matrix of tyhd.py


#################


























































################################template
url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+origins+"&destinations="+destinations+"&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
#print(url1)    
import urllib.request, json 
with urllib.request.urlopen(url1) as url:   
     data = json.loads(url.read().decode())    
     if data['rows'][0]['elements'][0]["status"] == "OK" :
         print(data['rows'][0]['elements'][0]['distance']['text'])
         print(data['rows'][0]['elements'][0]['duration']['text'])
     elif  data['rows'][0]['elements'][0]["status"] == "ZERO_RESULTS" :
                  print("No routes found")

          
    
















    
    