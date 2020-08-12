# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 00:04:18 2019

@author: tejav
"""
key="AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
stores=['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet','hasthinapuram']
#address='meerpet'
locations=[]
location_address=[]
lats_list=[]
longs_list=[]
store_name=[]
store_name_forjs=[]

for address in stores :
    url2="https://maps.googleapis.com/maps/api/geocode/json?&address="+address+"&key="+key     
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
         url1="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="+origins+"&destinations="+destinations+"&key="+key

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
    int_distancematrix.append(float(distancematrix[i].replace("km","")))####possible error if distance is in metrer  could not convert string to float: '1 m'
for i in range(len(distancematrix)) :
    final_matrix.append((math.floor(int_distancematrix[i])))
    

dms=np.reshape(final_matrix, (y,y))
print(dms)
          
dfs_chart = pd.DataFrame(dms, columns=stores, index=stores)
print(dfs_chart) 



################################################################################
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Distance callback
shortest_path=[]
def create_distance_callback(dist_matrix):
  # Create a callback to calculate distances between cities.

  def distance_callback(from_node, to_node):
    return int(dist_matrix[from_node][to_node])

  return distance_callback

def main():
    
  # Cities
  #city_names = ['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet']
  city_names=stores
  # Distance matrix
 
  
  
  
  dist_matrix = dms
  dist_matrix1 =[
       [ 0, 32, 19, 21, 24, 26, 25, 14, 26, 21, 25],
       [30,  0,  9,  5, 10,  7, 19, 14,  5, 15, 13],
       [24,  9,  0,  4,  7,  9, 13,  8,  9,  9, 10],
       [29,  5,  4,  0,  7,  5, 16, 11,  5, 12,  9],
       [22,  8,  6,  4,  0,  4, 15, 10,  7, 11,  4],
       [34,  8, 10,  5,  4,  0, 13, 14,  4, 15,  5],
       [23, 19, 13, 15, 13, 15,  0, 12, 20,  5, 10],
       [13, 15,  9, 11, 12, 15, 12,  0, 15,  6, 12],
       [35,  5, 11,  7,  8,  4, 17, 17,  0, 17,  9],
       [19, 15,  8, 10, 10, 15,  6,  6, 15,  0,  9],
       [24, 13, 10,  8,  4,  6,  8, 12, 10, 10,  0]]
  
 

  tsp_size = len(city_names)
  num_routes = 1
  depot = 0

  # Create routing model
  if tsp_size > 0:
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    # Create the distance callback.
    dist_callback = create_distance_callback(dist_matrix)
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
      # Solution distance.
      print ("Total distance: " + str(assignment.ObjectiveValue()) + " units\n")
      # Display the solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
      route_number = 0
      index = routing.Start(route_number) # Index of the variable for the starting node.
      route = ''
      while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
        shortest_path.append(city_names[routing.IndexToNode(index)])
        route += str(city_names[routing.IndexToNode(index)]) + ' --> '
        index = assignment.Value(routing.NextVar(index))


      route += str(city_names[routing.IndexToNode(index)])
      print ("Route:\n\n" + route)
    else:
      print ('No solution found.')
  else:
    print ('Specify an instance greater than 0.')

if __name__ == '__main__':
  main()
  
  
 #Ghatkesar -> Nagole -> lbnagar -> Bnreddy -> meerpet -> champapet -> Dilshuknagar -> 
 #malakpet -> Secunderabad -> tarnaka -> Boduppal -> Ghatkesar
  
  




























