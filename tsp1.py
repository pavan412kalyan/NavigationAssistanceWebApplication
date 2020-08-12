# -*- coding: utf-8 -*
#ocation" : {
#               "lat" : 17.271333,
#              "lng" : 78.538321
# "location" : {
    #           "lat" : 17.254301,
     #          "lng" : 78.680767
      #      },
#key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8
      #https://developers.google.com/maps/documentation/embed/guide
      
#https://stackoverflow.com/questions/3059044/google-maps-js-api-v3-simple-multiple-marker-example      

url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=17.271333, 78.538321&destinations=17.254301,78.680767&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
url2="https://maps.googleapis.com/maps/api/geocode/json?&address=ramojifilcity&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8 "     
 #   url=https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key=YOUR_API_KEY
 #https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8
 #https://maps.googleapis.com/maps/api/timezone/json?location=38.908133,-77.047119&timestamp=1458000000&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8

#https://developers.google.com/maps/documentation/javascript/markers
 
 ###########################################################################
url2="https://maps.googleapis.com/maps/api/geocode/json?&address=Bnreddy&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8 "     

import urllib.request, json 
with urllib.request.urlopen(url2) as url:
    
    
    data = json.loads(url.read().decode())
    test = json.dumps([s['geometry']['location'] for s in data['results']], indent=3)
    print(test)
   # print(data['results'].['geometry'])
   
    for s in data['results']:
        print(s['geometry']['location']['lat'])
        
 ############ ########################################################
url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=17.271333,78.538321&destinations=17.254301,78.680767&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
origins="17.271333,78.538321"
#origins="17.253301,28.490765"
destinations="17.254301,78.680767"

#for i in len(details) :
    
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

                
         
      
################################################     
my_dict = {
    "key 1": "value 1",
    "key 2": "value 2"
}
my_dict["key 1"]

store1={  "lat" : 17.254301,
    "lng" : 78.680767
    }
########################################################################

warehouse_address=[
  
   {  "store" :1,
     "lat" : 17.254301,
    "lng" : 78.680363
    } , 
  {  "store" :2,
     "lat" : 17.154301,
    "lng" : 78.480764
    }  ,
  {  "store" :3,
     "lat" : 17.254301,
    "lng" : 78.480765
    } ,
 
  
]

origins="17.271333,78.538321"

for i in range(len(warehouse_address)) :
    print("***************")
    print(warehouse_address[i]["store"])
    print(warehouse_address[i]["lat"])
    print(warehouse_address[i]["lng"])
    #print(str(warehouse_address[i]["lat"]) +","+ str(warehouse_address[i]["lng"]))
    destinations=str(warehouse_address[i]["lat"]) +","+ str(warehouse_address[i]["lng"])
    #print(destinations)
    
    url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+origins+"&destinations="+destinations+"&key=AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
    
    import urllib.request, json 
    with urllib.request.urlopen(url1) as url: 
        
        
        data = json.loads(url.read().decode())    
        if data['rows'][0]['elements'][0]["status"] == "OK" :
                                
            print(data['rows'][0]['elements'][0]['distance']['text'])
            print(data['rows'][0]['elements'][0]['duration']['text'])
            print("***************")

        elif  data['rows'][0]['elements'][0]["status"] == "ZERO_RESULTS" :
            
            print("No routes found")
            print("***************")

            
        


        
    
     
        
       

        
  
   
    






#####################################
       

    
    
    