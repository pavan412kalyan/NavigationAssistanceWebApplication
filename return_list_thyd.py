# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Distance callback
def create_distance_callback(dist_matrix):
  # Create a callback to calculate distances between cities.

  def distance_callback(from_node, to_node):
    return int(dist_matrix[from_node][to_node])

  return distance_callback

def main():
  # Cities
  city_names = ['Ghatkesar','Bnreddy','Nagole','lbnagar','Dilshuknagar','champapet','Secunderabad','Boduppal','meerpet','tarnaka','malakpet']

  # Distance matrix
 
  
  
  
  
  dist_matrix =[
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
      print ("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
      # Display the solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
      route_number = 0
      index = routing.Start(route_number) # Index of the variable for the starting node.
      route = ''
      while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
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
  
  
