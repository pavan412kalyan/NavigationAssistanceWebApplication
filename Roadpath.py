url4='https://roads.googleapis.com/v1/snapToRoads?path=-35.27801,149.12958|-35.28032,149.12907|-35.28099,149.12929|-35.28144,149.12984|-35.28194,149.13003|-35.28282,149.12956|-35.28302,149.12881|-35.28473,149.12836&interpolate=true&key=AIzaSyB5_l12Osmu8lBSBccXG8X82v56tacOxxE'
#url4='https://roads.googleapis.com/v1/snapToRoads?path=17.3141748, 78.5626575|17.3207396, 78.5604503|17.3211859, 78.56511259999999|17.3330722, 78.56936859999999|17.3378867, 78.569756|17.3370239, 78.5728709|17.3526577, 78.5626621|17.3695532, 78.57376870000002|17.3714801, 78.5695317&interpolate=true&key=AIzaSyB5_l12Osmu8lBSBccXG8X82v56tacOxxE'

road_lats=[]
road_longs=[]
road=[]
import numpy as np
import matplotlib.pyplot as plt
import urllib.request, json 
with urllib.request.urlopen(url4) as url:
    data = json.loads(url.read().decode())    
    for i in range(len(data['snappedPoints'])) :
        road_lats.append(data['snappedPoints'][i]['location']['latitude'])
        road_longs.append(data['snappedPoints'][i]['location']['longitude'])
        road.append([data['snappedPoints'][i]['location']['latitude'],data['snappedPoints'][i]['location']['longitude']])
        
#import requests
#
#link = url4
#f = requests.get(link)
#print(f.text)

   
              
data_for_graph=np.array(road)    
plt.plot( data_for_graph[:, 1],data_for_graph[:, 0],color='green',)
plt.scatter( data_for_graph[:, 1],data_for_graph[:, 0],color='green',marker="*",s=120)
plt.title('Path of Stores')


import gmplot 
  


gmap3 = gmplot.GoogleMapPlotter(-35.27801,149.12958,16) 
latitude_list = road_lats
longitude_list= road_longs

gmap3.scatter( latitude_list, longitude_list, '# FF0000', 
                              size = 40, marker = True ) 
  
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
  
gmap3.draw( "D:\TSP\map1.html" ) 

import webbrowser
webbrowser.open('D:\TSP\map1.html', new=2)
########################################################################

url5="https://maps.googleapis.com/maps/api/directions/json?origin=Bnreddy&destination=Nagole&key=AIzaSyB5_l12Osmu8lBSBccXG8X82v56tacOxxE"
path_lats=[]
path_longs=[]
road_path=[]
lat_1=[]
import numpy as np
import matplotlib.pyplot as plt
import urllib.request, json 
with urllib.request.urlopen(url5) as url:
    data = json.loads(url.read().decode())
    for i in range(len(data['routes'][0]['legs'][0]['steps'])) :
        
        path_lats.append(data['routes'][0]['legs'][0]['steps'][i]['end_location']['lat'])
        path_longs.append(data['routes'][0]['legs'][0]['steps'][i]['end_location']['lng'])
        road_path.append([data['routes'][0]['legs'][0]['steps'][i]['end_location']['lat'],data['routes'][0]['legs'][0]['steps'][i]['end_location']['lng']])

data_for_graph=np.array(road_path)    
plt.plot( data_for_graph[:, 1],data_for_graph[:, 0],color='green',)
plt.scatter( data_for_graph[:, 1],data_for_graph[:, 0],color='green',marker="*",s=120)
plt.title('Path of Stores')




#path=17.3141748, 78.5626575|17.3207396, 78.5604503|17.3211859, 78.56511259999999|17.3330722, 78.56936859999999|17.3378867, 78.569756|17.3370239, 78.5728709|17.3526577, 78.5626621|17.3695532, 78.57376870000002|17.3714801, 78.5695317








import gmplot 
gmap3 = gmplot.GoogleMapPlotter(17.3141748,78.5626575,16) 
latitude_list = path_lats
longitude_list= path_longs

gmap3.scatter( latitude_list, longitude_list, '# FF0000', 
                              size = 40, marker = True ) 
  
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
  
gmap3.draw( "D:\TSP\map1.html" ) 

import webbrowser
webbrowser.open('D:\TSP\map1.html', new=2)





###########################################################################
import requests   
url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyB5_l12Osmu8lBSBccXG8X82v56tacOxxE"
data={}  
r = requests.post(url = url,data={}) 
  
data = r.text 
print(data) 







############################################################################################################




###################################
#tsp using package
Z=[[17.445318, 78.68525509999999, 'Ghatkesar'],
 [17.3137596, 78.561889, 'Bnreddy'],
 [17.3714737, 78.5695016, 'Nagole'],
 [17.3457176, 78.55222959999999, 'lbnagar'],
 [17.3687826, 78.5246706, 'Dilshuknagar'],
 [17.3447337, 78.5182911, 'champapet'],
 [17.4399295, 78.4982741, 'Secunderabad'],
 [17.4138552, 78.57834460000001, 'Boduppal'],
 [17.3227982, 78.5280016, 'meerpet'],
 [17.4283104, 78.5386101, 'tarnaka'],
 [17.3730927, 78.49003809999999, 'malakpet'],
 [17.3174049, 78.5520232, 'hasthinapuram']
]

import tsp
t = tsp.tsp([(0,0), (0,1), (1,0), (1,1)])
print(t)  # distance, node index lis

mat =[[    0, 32358, 19813, 21847, 24806, 36389, 25079, 14146, 36418,
        20957, 25149, 34520],
       [30517,     0,  9023,  5808, 10374,  7659, 19841, 14838,  5551,
        15719, 13032,  2350],
       [24709,  9058,     0,  4785,  7722, 10566, 13500,  8497, 10596,
         9378, 10380,  9565],
       [29751,  4973,  4611,     0,  7114,  5781, 16251, 11247,  5811,
        12129,  9772,  4780],
       [22064,  8844,  6218,  4512,     0,  4138, 15342, 10339,  9182,
        11220,  4911,  8651],
       [34340,  7974,  9958,  5051,  4361,     0, 13722, 14130,  4625,
        15011,  5735,  7781],
       [23772, 20281, 13274, 15308, 13379, 15039,     0, 12282, 21118,
         5848, 10349, 20088],
       [13681, 16143,  9136, 11170, 12457, 16951, 12240,     0, 16980,
         6653, 12800, 15950],
       [35606,  5651, 11224,  7383,  8561,  4016, 21965, 16962,     0,
        17843,  9555,  3280],
       [19293, 15802,  8794, 10829, 10280, 16610,  6022,  6682, 16639,
            0,  9797, 15608],
       [24165, 13171, 10544,  8838,  4353,  6013,  9011, 12440, 10439,
        10691,     0, 12978],
       [32495,  2449,  8983,  5692, 10258,  6500, 19725, 14721,  3238,
        15603, 12916,     0]]
  
   # Distance Matrix
r = range(len(mat))
# Dictionary of distance
dist ={(i, j): mat[i][j] for i in r for j in r}
print(tsp.tsp(r, dist))
index= tsp.tsp(r, dist)[1]
store_name_forjs=Z
for_graph=[]
for i in range(len(store_name_forjs)) :
    print(index[i])
    print(store_name_forjs[index[i]][1:3])
    for_graph.append(store_name_forjs[index[i]][0:2])

    

print(tsp.tsp(r, dist))

data_for_graph=np.array(for_graph)    
plt.plot( data_for_graph[:, 1],data_for_graph[:, 0],color='green',)
plt.scatter( data_for_graph[:, 1],data_for_graph[:, 0],color='green',marker="*",s=120)
plt.title('Path of Stores')



######################################

