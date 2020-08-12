# -*- coding: utf-8 -*-
stores=['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet']

Y=[[17.445318, 78.68525509999999, 'Ghatkesar'], [17.3137596, 78.561889, 'B N Reddy Nagar'], 
 [17.3714737, 78.5695016, 'Nagole'], [17.3457176, 78.55222959999999, 'LB Nagar'],
 [17.3687826, 78.5246706, 'DSNR'], [17.3447337, 78.5182911, 'Champapet'],
 [17.4399295, 78.4982741, 'SC'],
 [17.4138552, 78.57834460000001, 'Boduppal'], [17.3227982, 78.5280016, 'Meerpet'],
 [17.4283104, 78.5386101, 'Tarnaka'], [17.3730927, 78.49003809999999, 'Malakpet']]

#############
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



#Ghatkesar -> Nagole -> lbnagar -> Bnreddy -> meerpet -> champapet -> Dilshuknagar -> 
 #malakpet -> Secunderabad -> tarnaka -> Boduppal -> Ghatkesar
answer=['Ghatkesar' , 'Nagole' , 'lbnagar' , 'Bnreddy' ,'hasthinapuram', 'meerpet' , 'champapet' , 'Dilshuknagar' , 'malakpet' , 'Secunderabad' , 'tarnaka' , 'Boduppal' , 'Ghatkesar']
#Y[10][2]
ordered_lats=[]
ordered_longs=[]
for x in answer :
    for i in range(0,len(Z)) :
        if Z[i][2]==x :
            print(x)
            ordered_lats.append(Z[i][0])
            ordered_longs.append(Z[i][1])


        
        
    
    





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
 
 
 for i in range(0,12):
     print(i)





['1 m', '32.4 km', '19.8 km', '21.8 km', '24.8 km', '26.5 km', '25.1 km', '14.1 km', '26.5 km', '21.0 km', '25.1 km', '30.5 km', '1 m', '9.0 km', '5.8 km', '10.4 km', '7.7 km', '19.8 km', '14.8 km', '5.6 km', '15.7 km', '13.0 km', '24.7 km', '9.1 km', '1 m', '4.8 km', '7.7 km', '9.5 km', '13.5 km', '8.5 km', '9.5 km', '9.4 km', '10.4 km', '29.8 km', '5.0 km', '4.6 km', '1 m', '7.1 km', '5.8 km', '16.3 km', '11.2 km', '5.8 km', '12.1 km', '9.8 km', '22.1 km', '8.8 km', '6.2 km', '4.5 km', '1 m', '4.1 km', '15.3 km', '10.3 km', '7.6 km', '11.2 km', '4.9 km', '34.3 km', '8.0 km', '10.0 km', '5.1 km', '4.4 km', '1 m', '13.6 km', '14.1 km', '4.2 km', '15.0 km', '5.7 km', '23.8 km', '19.7 km', '13.3 km', '15.3 km', '13.4 km', '15.0 km', '1 m', '12.3 km', '20.0 km', '5.8 km', '10.3 km', '13.7 km', '15.5 km', '9.1 km', '11.2 km', '12.5 km', '15.8 km', '12.2 km', '1 m', '15.9 km', '6.7 km', '12.8 km', '35.6 km', '5.7 km', '11.2 km', '7.4 km', '8.6 km', '4.0 km', '17.4 km', '17.0 km', '1 m', '17.8 km', '9.6 km', '19.3 km', '15.2 km', '8.8 km', '10.8 km', '10.3 km', '15.5 km', '6.0 km', '6.7 km', '15.5 km', '1 m', '9.8 km', '24.2 km', '13.2 km', '10.5 km', '8.8 km', '4.4 km', '6.0 km', '8.9 km', '12.4 km', '10.0 km', '10.7 km', '1 m']




###################################################


#######################################################

# TO DRAW PLOT ON MAP
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[17.445318, 78.68525509999999],
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
plt.plot(data[:, 0], data[:, 1])
plt.show()


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



#########################################################

################################
# importing pygmaps  --using pygmaps check pygmpaps.py in working folder
import pygmaps 

# list of latitudes 

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
mymap3 = pygmaps.maps(17.3457176, 78.55222959999999,12) 


for i in range(len(latitude_list)): 
	mymap3.addpoint(latitude_list[i], longitude_list[i], "#FFF000") 
	
mymap3.draw('markers.html') 



#################################################################
import psycopg2
import gmplot

gmap = gmplot.GoogleMapPlotter(latitude_list[0],longitude_list[0],12)

gmap.scatter(latitude_list,longitude_list, '#FF6666', edge_width=10)
gmap.draw('testsmap.html')
             


