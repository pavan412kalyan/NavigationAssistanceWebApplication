

###################################
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 00:04:18 2019

@author: tejav
"""
key="AIzaSyCgJRCn1QNAxn2jri3c56-imWAQn2EYqc8"
stores=['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet','hasthinapuram','kothapet','ramanthapur','banjarahills','pocharamsecunderabad','nadergul']
#address='meerpet'

locations=[]
location_address=[]
lats_list=[]
longs_list=[]
store_name=[]
store_name_forjs=[]
with_place_id=[]
city_dist=[]
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
        with_place_id.append([lat,long,data['results'][0]['place_id'],address])        
        lats_list.append(lat)
        longs_list.append(long)       
        locations.append([lat,long])
        location_address.append([lat,long,name]) 
        city_dist.append(name)
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
                 distance=data['rows'][0]['elements'][0]['distance']['value']
                 print(data['rows'][0]['elements'][0]['duration']['value'])
                 distancematrix.append(distance)
             elif  data['status'] == 'OVER_QUERY_LIMIT' :
                 print("OVER_QUERY_LIMIT")      
                 
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
#for i in range(len(distancematrix)) :
 #   int_distancematrix.append(float(distancematrix[i].replace("km","")))####possible error if distance is in metrer  could not convert string to float: '1 m'
#for i in range(len(distancematrix)) :
 #   final_matrix.append((math.floor(int_distancematrix[i])))
    

dms=np.reshape(distancematrix, (y,y))
print(dms)
          
dfs_chart = pd.DataFrame(dms, columns=stores, index=stores)
print(dfs_chart) 



################################################################################
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
shortest_path=[]
# Distance callback
def create_distance_callback(dist_matrix):
  # Create a callback to calculate distances between cities.

  def distance_callback(from_node, to_node):
    return int(dist_matrix[from_node][to_node])

  return distance_callback

def main():
    
    
  # Cities
  #city_names = ['Ghatkesar', 'B N Reddy Nagar', 'Nagole', 'LB Nagar', 'DSNR', 'Champapet', 'SC', 'Boduppal', 'Meerpet', 'Tarnaka', 'Malakpet', 'Hastinapuram', 'Kothapet', 'Ramanthapur', 'Banjara Hills', 'Pocharam', 'Nadergul']
  #city_names=stores
  city_names=city_dist
  # Distance matrix
 
  
  
  
  dist_matrix = dms
#  dist_matrix=[[    0, 32358, 19813, 21847, 24806, 36389, 25079, 14146, 36418,
#        20957, 25149, 34520, 20128, 21223, 34173,  5716, 39778],
#       [30517,     0,  9023,  5808, 10374,  7659, 19841, 14838,  5551,
#        15719, 13032,  2350,  8345, 12765, 22147, 31482,  6316],
#       [24709,  9058,     0,  4785,  7722, 10566, 13500,  8497, 10596,
#         9378, 10380,  9565,  3067,  8105, 22594, 25675, 14904],
#       [29751,  4973,  4611,     0,  7114,  5781, 16251, 11247,  5811,
#        12129,  9772,  4780,  5818,  9505, 18887, 30716, 10819],
#       [22064,  8844,  6218,  4512,     0,  4138, 15342, 10339,  7646,
#        11220,  4911,  8651,  2627,  4278, 14026, 19489, 14690],
#       [34340,  7974,  9958,  5051,  4361,     0, 13574, 14130,  4206,
#        15011,  5735,  7781,  6418,  6752, 14948, 35305, 10818],
#       [23772, 20281, 13274, 15308, 13379, 15039,     0, 12282, 19047,
#         5848, 10349, 20088, 13590, 13425,  9614, 21197, 26127],
#       [13681, 16143,  9136, 11170, 12457, 16951, 12240,     0, 16980,
#         6653, 12800, 15950,  9452,  8873, 21334, 11106, 21989],
#       [35606,  5651, 11224,  7383,  8561,  4016, 17394, 16962,     0,
#        17843,  9555,  3280,  9920, 10951, 27579, 36571,  8067],
#       [19293, 15802,  8794, 10829, 10280, 16610,  6022,  6682, 16639,
#            0,  9797, 15608,  9110,  8945, 15116, 16718, 21647],
#       [24165, 13171, 10544,  8838,  4353,  6013,  8863, 12440, 10020,
#        10691,     0, 12978,  6953,  6230, 10237, 21590, 16633],
#       [32495,  2449,  8983,  5692, 10258,  6500, 19725, 14721,  3238,
#        15603, 12916,     0,  8229, 12649, 22031, 33460,  8295],
#       [19437,  8019,  3591,  3686,  4655,  6171, 12715,  7712,  8356,
#         8593,  7313,  7826,     0,  7320, 16428, 16862, 13865],
#       [20308, 12793,  8079,  8460,  3975,  6859, 11377,  8582, 10583,
#         7255,  6187, 12600,  6576,     0, 12658, 17732, 18639],
#       [32769, 33276, 22271, 18998, 14513, 16173, 10628, 21280, 29141,
#        14845, 11482, 31892, 17113, 12939,     0, 30194, 33357],
#       [ 5483, 32298, 17089, 19123, 22082, 24904, 22355, 11423, 24933,
#        18233, 22426, 34461, 17405, 18499, 31449,     0, 39718],
#       [38908,  6109, 14944, 11729, 16295, 11159, 25762, 20758,  8075,
#        21640, 18953,  8271, 14266, 18686, 32675, 39873,     0]]
# 

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
      print ("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
      # Display the solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
      route_number = 0
      index = routing.Start(route_number) # Index of the variable for the starting node.
      route = ''
      while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
        shortest_path.append(city_names[routing.IndexToNode(index)])###list for solution

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

shortest_path.append(shortest_path[0])

  
  
  
 #Ghatkesar -> Nagole -> lbnagar -> Bnreddy -> meerpet -> champapet -> Dilshuknagar -> 
 #malakpet -> Secunderabad -> tarnaka -> Boduppal -> Ghatkesar
  
  
######################################################
 
 #this is for ordering the lats and long in the order of shotest path;;;;

##
Z=[[17.445318, 78.68525509999999, 'Ghatkesar'],
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

#answer=['Ghatkesar' , 'Nagole' , 'kothapet','lbnagar' , 'Bnreddy' ,'hasthinapuram', 'meerpet' , 'champapet' , 'Dilshuknagar' , 'malakpet' , 'Secunderabad' , 'tarnaka' , 'Boduppal' , 'Ghatkesar']
#Y[10][2]

#####*****Check Z and  answer spellinfs if any errors

Z=location_address
answer=shortest_path
ordered_lats=[]
ordered_longs=[]
ordered_lats_long=[]
ordered_lats_long_with_names=[]
for x in answer :
    for i in range(0,len(Z)) :
        if Z[i][2]==x :
            print(x)
            ordered_lats.append(Z[i][0])
            ordered_longs.append(Z[i][1])
            ordered_lats_long.append([Z[i][0],Z[i][1]])
            ordered_lats_long_with_names.append([Z[i][0],Z[i][1],x])

            


        
        
    
    













###################################################


#######################################################

# TO DRAW PLOT ON MAP
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#answer=['Ghatkesar' , 'Nagole' , 'lbnagar' , 'Bnreddy' ,'hasthinapuram', 'meerpet' , 'champapet' , 'Dilshuknagar' , 'malakpet' , 'Secunderabad' , 'tarnaka' , 'Boduppal' , 'Ghatkesar']
#stores=['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet','hasthinapuram']
answer=shortest_path
data_for_graph = np.array([[17.445318, 78.68525509999999],
 [17.3137596, 78.561889],
 [17.3714737, 78.5695016],
 [17.3457176, 78.55222959999999],
 [17.3687826, 78.5246706],
 [17.3447337, 78.5182911],
 [17.4399295, 78.4982741],
 [17.4138552, 78.57834460000001],
 [17.3227982, 78.5280016],
 [17.4283104, 78.5386101],
 [17.3730927, 78.49003809999999]])
#ordered_lats_long_with_names[2]
data_for_graph=np.array(ordered_lats_long)    
plt.plot( data_for_graph[:, 1],data_for_graph[:, 0],color='green',)
plt.scatter( data_for_graph[:, 1],data_for_graph[:, 0],color='green',marker="*",s=120)
plt.title('Path of Stores')






df = pd.DataFrame(dict(lats=data_for_graph[:, 1], longs=data_for_graph[:, 0], label=answer))
ax = df.plot.scatter(x='lats', y='longs', alpha=0.5)
plt.plot( data_for_graph[:, 1],data_for_graph[:, 0],color='green',)

for i, txt in enumerate(df.label):
    ax.annotate(txt, (df.lats.iat[i],df.longs.iat[i]))
plt.show()
plt.title('Path of Stores')









######################################################
import gmplot 
  
latitude_list = [17.445318,
 17.3137596,
 17.3714737,
 17.3457176,
 17.3687826,
 17.3447337,
 17.4399295,
 17.4138552,
 17.3227982,
 17.4283104,
 17.3730927] 
longitude_list = [78.68525509999999,
 78.561889,
 78.5695016,
 78.55222959999999,
 78.5246706,
 78.5182911,
 78.4982741,
 78.57834460000001,
 78.5280016,
 78.5386101,
 78.49003809999999]

latitude_list=ordered_lats
longitude_list=ordered_longs

  
gmap3 = gmplot.GoogleMapPlotter(17.445318, 
                                78.68525509999999,12) 
  
# scatter method of map object  
# scatter points on the google map 
gmap3.scatter( latitude_list, longitude_list, '# FF0000', 
                              size = 40, marker = True ) 
  
# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
  
gmap3.draw( "D:\TSP\map1.html" ) 

import webbrowser
webbrowser.open('D:\TSP\map1.html', new=2)






















































