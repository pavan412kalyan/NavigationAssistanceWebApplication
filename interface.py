# -*- coding: utf-8 -*-
#######for importinf the data
import mysql.connector

lat_from_db=[]
lng_from_db=[]
store_db=[]
details_name_forjs_v=[]
mydb = mysql.connector.connect(
  host="localhost",
  user="pavan",
  passwd="1234",
)
mycursor = mydb.cursor()

details_name_forjs_v=[]
mycursor.execute("use store")


mycursor.execute("SELECT * FROM shop_details")


myresult = mycursor.fetchall()
save_result=myresult
#x=myresult[0][0]
for i in range(len(myresult)):
    details_name_forjs_v.append([myresult[i][0],float(myresult[i][1]),float(myresult[i][2]),1])


##details for shops to pass variable for html page
details_shoppsage=[]    
for i in range(len(myresult)):
    details_shoppsage.append([myresult[i][0],float(myresult[i][1]),float(myresult[i][2]),myresult[i][3],myresult[i][4]])    

##################for finding distancces
details_name_forjs=[]        

from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

######
shops_near_me=[] 
    

for i in range(len(details_shoppsage)) :
    v=distance(17.3174049,78.5520232,details_shoppsage[i][1],details_shoppsage[i][2])
    v='%.3f' % v
    shops_near_me.append([details_shoppsage[i][0],details_shoppsage[i][1],details_shoppsage[i][2],details_shoppsage[i][3],details_shoppsage[i][4],float(v)])
shops_near_me.sort(key=lambda x:x[5])

#######this is for json obj in javascript page markers
 
for det in details_name_forjs_v :
    details_name_forjs.append([det[0],det[1],det[2],1])
    
    
   


#details_name_forjs_v





###############################




import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
stores1=['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet','hasthinapuram','kothapet','ramanthapur','banjarahills','pocharamsecunderabad','nadergul']
markers_stores =[['Ghatkesar', 17.445318, 78.68525509999999, 1],
 ['Bnreddy', 17.3137596, 78.561889, 1],
 ['Nagole', 17.3714737, 78.5695016, 1],
 ['lbnagar', 17.3457176, 78.55222959999999, 1],
 ['Dilshuknagar', 17.3687826, 78.5246706, 1],
 ['champapet', 17.3447337, 78.5182911, 1],
 ['Secunderabad', 17.4399295, 78.4982741, 1],
 ['Boduppal', 17.4138552, 78.57834460000001, 1],
 ['meerpet', 17.3227982, 78.5280016, 1],
 ['tarnaka', 17.4283104, 78.5386101, 1],
 ['malakpet', 17.3730927, 78.49003809999999, 1],
 ['hasthinapuram', 17.3174049, 78.5520232, 1],
 ['kothapet', 17.3730192, 78.547636, 1],
 ['ramanthapur', 17.3852774, 78.52775059999999, 1],
 ['banjarahills', 17.4138277, 78.4397584, 1],
 ['pocharamsecunderabad', 17.4420325, 78.6502201, 1],
 ['nadergul', 17.2738816, 78.54866489999999, 1]]


tsp_shops =[] #for variable in function

app = Flask(__name__)
@app.route('/')

@app.route('/home')
def home():
	# serve index template
    return render_template('stores_page.html',store=stores1)


@app.route('/stores')
def stores():
	# serve index template
	
    try :
        return render_template('stores_page.html')
    except  Exception as e :        
            return str(e)

@app.route('/markers')
def markers():
	# serve index template
	return render_template('Markersgoogle.html',markers=json.dumps(details_name_forjs_v),markers2=json.dumps(markers_stores))


@app.route("/shops" , methods=['GET', 'POST'])
def shops():
    index=0
    v=100
    distance_near=100
    items_q="item_1"
    distance_near = request.form.get('distance')
    v_n=20 #error my  distance_near may return none type
    if distance_near is not None:
        v_n=float(distance_near)


    print(distance_near)
    select = request.form.get('warehouse')
    items_q = request.form.get('item')
    if distance_near is  None:
        items_q="item_1"
        
    threshold="0 "  #query value must be in string datatype 
    print(threshold)
    threshold = request.form.get('threshold')
    if threshold is not None:
        threshold=str(threshold)   
    else :
        threshold="0"
        

    print(items_q)

    print(select)
    mycursor.execute("select  A.* from shop_details A where A.id_s in (select B.id_s from stores_data_values B  where "+items_q+"<="+threshold+")")
    myresult = mycursor.fetchall()
    print(len(myresult))
    details_shoppsage=[]    
    for i in range(len(myresult)):
        details_shoppsage.append([myresult[i][0],float(myresult[i][1]),float(myresult[i][2]),myresult[i][3],myresult[i][4]])    


    shops_near_me=[] 
   
    for i in range(len(stores1)) :
        if stores1[i]== select :
            index=i
        

    for i in range(len(details_shoppsage)) :
        v=distance(markers_stores[index][1],markers_stores[index][2],details_shoppsage[i][1],details_shoppsage[i][2])
        v='%.3f' % v
        v=float(v)
        if v < v_n :
            shops_near_me.append([details_shoppsage[i][0],details_shoppsage[i][1],details_shoppsage[i][2],details_shoppsage[i][3],details_shoppsage[i][4],float(v)])
    shops_near_me.sort(key=lambda x:x[5])
    #print(shops_near_me[0])
    global selected_wh
    selected_wh=(markers_stores[index][1],markers_stores[index][2])
    
    global tsp_shops#set global to reflect the changes in /travel function
    tsp_shops=shops_near_me    
    return render_template('shops_details.html',shops=shops_near_me,warehouse=stores1,from_wh=stores1[index])
    
    
@app.route('/travel')
def travel():
    dis=[]
    #import tsp
    import numpy as np

    print(tsp_shops)
    shops_near_me=tsp_shops
    mat_size=len(shops_near_me)
#####################
    cit_ids=[]
    cit_ids_only=[]
    for i in range(len(shops_near_me)) :
        cit_ids_only.append(shops_near_me[i][4])
        cit_ids.append([shops_near_me[i][0],shops_near_me[i][4],shops_near_me[i][1],shops_near_me[i][2]])
#######################
    
    #tsp
    for i in range(len(shops_near_me)) :
        
        print(i)
        for j in range(len(shops_near_me)) :
            m=distance(shops_near_me[i][1],shops_near_me[i][2],shops_near_me[j][1],shops_near_me[j][2])
            #print(m*1000)
            dis.append(m*1000)
            #print(dis)
    print(len(dis))
    dm_shops=np.reshape(dis, (len(shops_near_me),len(shops_near_me)))
    print(dm_shops)
    print(len(dm_shops))
#    r = range(len(dm_shops))
## Dictionary of distance
#    dist = {(i, j): dm_shops[i][j] for i in r for j in r}
#    print(tsp.tsp(r, dist)) 
    ########################################
        
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
      city_names=cit_ids_only
      # Distance matrix
     
      
      
      
      dist_matrix = dm_shops
    
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

    print(len(shortest_path))     
    
    Z=cit_ids
    answer_shop=shortest_path
    ordered_lats_shop=[]
    ordered_longs_shop=[]
    ordered_lats_long_shop=[]
    ordered_lats_long_with_names_shop=[]
    for x in answer_shop :        
        for i in range(0,len(Z)) :
                if Z[i][1]==x :
                    print(x)
                    ordered_lats_shop.append(Z[i][2])
                    ordered_longs_shop.append(Z[i][3])
                    ordered_lats_long_shop.append([Z[i][2],Z[i][3]])
                    ordered_lats_long_with_names_shop.append([Z[i][2],Z[i][3],Z[i][0]])
                    
    
    details_name_forjs_shop=[]#javascript map varriable    
    for det in Z :
        details_name_forjs_shop.append([det[2],det[3],det[0],1])
    ####
    
    
    
    
    import gmplot                
    latitude_list=ordered_lats_shop
    longitude_list=ordered_longs_shop
    
      
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
      
    gmap3.draw( "templates/tsp_stores.html" ) 
    
    import webbrowser
    #webbrowser.open("templates/tsp_stores.html", new=2)
    #return render_template("tsp_stores.html")
    return render_template("travellingtsp.html",lats_lng=ordered_lats_long_shop)   

#############################################################end of travel route

@app.route('/warehouse',methods=['GET', 'POST'])
def warehouse():
    client_id=""
    client_id = request.form.get('client_id')
    print(client_id)
     #error my  distance_near may return none type
    if client_id is not None:
        client_id=str(client_id)        
        mycursor.execute("use store;")
        sql_q="select  A.* from shop_details A where A.id_s in (select B.id_s from stores_data_values B  where id_s ='"+client_id+"')"
        mycursor.execute(sql_q)
        whs = mycursor.fetchone()
        if whs is not None :
            ####Our code for shwoeing details on page...after storevliet is true
            print(myresult[0][4])
            mycursor.execute("select * from stores_data_values where id_s='"+client_id+"'") 
            store_values = mycursor.fetchone()
            ####
            mycursor.execute("SELECT warehouse_add.address,warehouse_values.*,warehouse_add.lats,warehouse_add.lng FROM warehouse_add INNER JOIN warehouse_values ON warehouse_values.id_s = warehouse_add.place_id;")
            wh_values = mycursor.fetchall()#warehouse values
            print(wh_values[0])
            
            
            
            
#            #### for removing a particular warehouse remove it from wh_values
            block = request.form.getlist('block')
            print(block ,"blocked")
            dummy =[]
            dummy=wh_values  
            n=0
            print(len(dummy),"length=====")               

            for d in dummy :
                n=n+1
                print(n,len(dummy),"enter=====")               
                if d[1] in block :
                    wh_values.remove(d)
                    print(d[0],"removed=====")
    
                    
            #wh_values=dummy        
                

            ######
           
#            min_val=10
#            print(store_values[0])#[id,item0,item1,....item17]
#            print(wh_values[0])#[address,ids,item0,item1----item17,lats,lng]
#            for i in range(1,19) :
#                p="required_shops"+str((i-1))
#                p=[]
#                if store_values[i] <= min_val:
#                    for w in wh_values :
#                        if w[i+1] > 10 :
#                           p.append([w[1],store_values[0],w[0],"item_"+str((i-1)),i,w[20],w[21]])
#                            
#                    print(p)     
            min_val=10
            required_shops=[]
#            print(store_values[0])#[id,item0,item1,....item17]
#            print(wh_values[0])#[address,ids,item0,item1----item17,lats,lng]
            for i in range(1,19) :
                if store_values[i] <= min_val:
                    x=[]
                    for w in wh_values :
                        if w[i+1] > 10 :
                              x.append([w[1],store_values[0],w[0],"item_"+str((i-1)),i,w[20],w[21],store_values[i],w[i+1]])
                    required_shops.append(x)        
                
            #print(required_shops[0])       
            
            lats_shop=float(whs[1])
            lngs_shop=float(whs[2])
            solution=[]
            
            for i in range(len(required_shops)) :
                sol=[]
                for j in range(len(required_shops[i])) :
                    dis=distance(lats_shop,lngs_shop,float(required_shops[i][j][5]),float(required_shops[i][j][6]))
                    print(dis)
                    sol.append([dis,required_shops[i][j][0],required_shops[i][j][1],required_shops[i][j][2],required_shops[i][j][3],lats_shop,lngs_shop,float(required_shops[i][j][5]),float(required_shops[i][j][6]),required_shops[i][j][7],required_shops[i][j][8]])

                sol.sort(key=lambda x:x[0])
                solution.append(sol)
            print(solution[0])
    
                
                
        
            
            
            
            ######
                          
            
            return render_template('warehouse_show.html',store_values=store_values,store_details=whs,markers2=json.dumps(markers_stores),stores=markers_stores,wh_values=wh_values,checked=solution)
        else :
            
            return "<h1> CHECK CLIENT IDS</h1>"
        
        


        
    else :
        
        return render_template('store_details_login.html')
            
        
        
        
        
        
    
    return render_template('warehouse_details.html',store=stores1)

    
@app.route('/route_shops/<lats>/<lng>')
def route_shops(lats,lng):
    #print(selected_wh)
#    print(selected_wh)

    #print(lats,lng,1111111111111111111)
    	
    return render_template('embed_map_route.html',o_lats=selected_wh[0],o_lng=selected_wh[1],d_lats=lats,d_lng=lng)

@app.route('/route_warehouse/<o_lats>/<o_lng>/<d_lats>/<d_lng>')
def route_warehouse(o_lats,o_lng,d_lats,d_lng):
    #print(selected_wh)
#    print(selected_wh)

    #print(lats,lng,1111111111111111111)
    return render_template('embed_map_route.html',o_lats=o_lats,o_lng=o_lng,d_lats=d_lats,d_lng=d_lng)




    
if __name__ == '__main__':
	# run!
	app.run(debug=True)

