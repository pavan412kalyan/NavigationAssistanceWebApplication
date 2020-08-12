import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return "HEllo"

if __name__ == '__main__':
	# run!
	app.run()









# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 

class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printSolution(self, dist): 
		print("Vertex tDistance from Source")
		for node in range(self.V): 
			print (node,"t",dist[node]) 

	# A utility function to find the vertex with 
	# minimum distance value, from the set of vertices 
	# not yet included in shortest path tree 
	def minDistance(self, dist, sptSet): 

		# Initilaize minimum distance for next node 
		min = sys.maxint 

		# Search not nearest vertex not in the 
		# shortest path tree 
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 

		return min_index 

	# Funtion that implements Dijkstra's single source 
	# shortest path algorithm for a graph represented 
	# using adjacency matrix representation 
	def dijkstra(self, src): 
        
        

		dist = [sys.maxint] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 

			# Pick the minimum distance vertex from 
			# the set of vertices not yet processed. 
			# u is always equal to src in first iteration 
			u = self.minDistance(dist, sptSet) 

			# Put the minimum distance vertex in the 
			# shotest path tree 
			sptSet[u] = True

			# Update dist value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shotest path tree 
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    
                                       
					dist[v] = dist[u] + self.graph[u][v] 

    self.printSolution(dist) 

# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] 
		]; 

g.dijkstra(0); 

# This code is contributed by Divyanshu Mehta 
    #####################################################
graph12 = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] 
		];    
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
    return self
 
  def add_node(self, value):
    self.nodes.add(value)
    return self
 
  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    return self
 
 
def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}
 
  nodes = set(graph.nodes)
 
  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node
 
    if min_node is None:
      break
 
    nodes.remove(min_node)
    current_weight = visited[min_node]
 
    for edge in graph.edges[min_node]:
      try:
        weight = current_weight + graph.distance[(min_node, edge)]
      except:
        continue
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node
 
  return visited, path

o1 = Graph()
add_node(5)

##################################################
from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    graph = Graph()
#
#    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
#        graph.add_node(node)
#
#    graph.add_edge('A', 'B', 10)
#    graph.add_edge('A', 'C', 20)
#    graph.add_edge('B', 'D', 15)
#    graph.add_edge('C', 'D', 30)
#    graph.add_edge('B', 'E', 50)
#    graph.add_edge('D', 'E', 30)
#    graph.add_edge('E', 'F', 5)
#    graph.add_edge('F', 'G', 2)
#
#    print(shortest_path(graph, 'A', 'G')) # output: (25, ['A', 'B', 'D']) 


###############################################################
stores=['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet','hasthinapuram']
mat=[[    0, 32358, 19813, 21847, 24806, 26519, 25079, 14146, 26548,
        20957, 25149, 34520],
       [30517,     0,  9023,  5808, 10374,  7659, 19841, 14838,  5551,
        15719, 13032,  2350],
       [24709,  9149,     0,  4785,  7722,  9458, 13500,  8497,  9487,
         9378, 10380,  8956],
       [29751,  4973,  4611,     0,  7114,  5781, 16251, 11247,  5811,
        12129,  9772,  4780],
       [22064,  8844,  6218,  4512,     0,  4138, 15342, 10339,  7646,
        11220,  4911,  8651],
       [34340,  7974,  9958,  5051,  4361,     0, 13574, 14130,  4206,
        15011,  5735,  7781],
       [23772, 19672, 13274, 15308, 13379, 15039,     0, 12282, 20010,
         5848, 10349, 19479],
       [13681, 15534,  9136, 11170, 12457, 15843, 12240,     0, 15872,
         6653, 12800, 15341],
       [35606,  5651, 11224,  7383,  8561,  4016, 17394, 16962,     0,
        17843,  9555,  3280],
       [19293, 15192,  8794, 10829, 10280, 15501,  6022,  6682, 15530,
            0,  9797, 14999],
       [24165, 13171, 10544,  8838,  4353,  6013,  8863, 12440, 10020,
        10691,     0, 12978],
       [32495,  2449,  8983,  5692, 10258,  6500, 19725, 14721,  3238,
        15603, 12916,     0]]
       
#xmat=mat
#for i in range(len(stores)) :
#        for j in range(len(xmat)) :
#            if mat[i][j]>10000:
#                 mat[i][j]=0
#                



       
for node in stores:
    graph.add_node(node)

for i in range(len(stores)) :
        x=stores[i]
        for j in range(len(mat)) :
                y=stores[j]
                graph.add_edge(x, y, mat[i][j])

        
    

print(shortest_path(graph, 'Nagole', 'champapet'))



########



















lsd=[['a','f']]
lsd[1].append('s')


li = [[2,6,5],[1,3,7],[5,4,6]]

for x in range(10):
    print (random.randint(0,787))


##########################################################################


import numpy
numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])

data_items=[]
import random

for i in range(len(c)):
    print(c[i][2])   
    data_items.append([ c[i][2],
                       random.randint(0,150)*random.randint(0,7),random.randint(0,102)*random.randint(0,7),random.randint(0,142)*random.randint(0,7),
                       random.randint(0,102)*random.randint(0,7),random.randint(0,102)*random.randint(0,7),random.randint(0,12)*random.randint(0,7),
                       random.randint(0,102)*random.randint(0,7),random.randint(0,120)*random.randint(0,7),random.randint(0,112)*random.randint(0,7),
                       random.randint(0,102)*random.randint(0,7),random.randint(0,182)*random.randint(0,7),random.randint(0,152)*random.randint(0,7),
                       random.randint(0,102)*random.randint(0,7),random.randint(0,112)*random.randint(0,7),random.randint(0,102)*random.randint(0,7),
                       random.randint(0,152)*random.randint(0,7),random.randint(0,125)*random.randint(0,7),random.randint(0,120)*random.randint(0,7),
                       ])
    
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="pavan",
  passwd="1234"
)
mycursor1.execute("use store")

mycursor1 = mydb.cursor(buffered=True)
mycursor1.execute("SELECT * FROM warehouse_add")
c=mycursor1.fetchall()


mycursor1.execute("SELECT * FROM stores_data_values")



#save_result=myresult
#x=myresult[0][0]
ja=[]
#for i in range(len(myresult)):
    
    
mycursor1.execute("select  A.* from shop_details A where A.id_s in (select B.id_s from stores_data_values B  where item_1 =0 )")
#    myresult = mycursor.fetchall()

mycursor1.execute(" select id_s  from stores_data_values where item_1<10")
     
    
    
    #########################
for i in range(len(stores1)) :
    if stores1[i]=='Ghatkesar' :
        print(i)
   





for i in range(20) :
    print( """
          
    {% if store_values[""" +i """]|int  < x %}
    <tr>
    <td style="color: red;">{{store_values[""" +i """]}}</td>
    </tr>  
        {% else %}
    <tr>
    <td style="color: green;">{{store_values[""" +i """]}}</td>
    </tr>   
    
       {% endif %}
       """)






<script>

function distance(lat1, lon1, lat2, lon2) {
  var p = 0.017453292519943295;    // Math.PI / 180
  var c = Math.cos;
  var a = 0.5 - c((lat2 - lat1) * p)/2 + 
          c(lat1 * p) * c(lat2 * p) * 
          (1 - c((lon2 - lon1) * p))/2;

  return 12742 * Math.asin(Math.sqrt(a)); // 2 * R; R = 6371 km
  
document.getElementById("demo").innerHTML = distance({{store_details[1]}}, {{store_details[1]}},>{{wh[20]}},>{{wh[20]}}); 


}

</script>


