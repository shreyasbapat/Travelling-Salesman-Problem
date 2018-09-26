import math

from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
f=open("euc_100", "r")
eu = f.readline().split()[0]
# print (eu)

if eu=="euclidean":
    euclid = True
else:
    euclid = False

n = int(f.readline())

# g = Graph(n)

coordinates = []
for i in range(n):
    x = [f.readline().split()]
    x = [float(i) for i in x[0]]
    coordinates.append(x)
	    
distances = []
for i in range(n):
    x = [f.readline().split()]
    x = [float(i) for i in x[0]]
    distances.append(x)
 


def create_distance_matrix(locations):
# Create the distance matrix.
  return distances
def create_distance_callback(dist_matrix):
  # Create the distance callback.

  def distance_callback(from_node, to_node):
    return int(dist_matrix[from_node][to_node])

  return distance_callback

def main():
  # Create the data.
  locations = create_data_array()
  dist_matrix = create_distance_matrix(locations)
  dist_callback = create_distance_callback(dist_matrix)
  tsp_size = len(locations)
  num_routes = 1
  depot = 0

  # Create routing model.
  if tsp_size > 0:
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
    search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit_ms = 30000
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:

      # Solution cost.
      print "Total distance: " + str(assignment.ObjectiveValue()) + "\n"

      # Inspect solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1.
      route_number = 0
      node = routing.Start(route_number)
      start_node = node
      route = ''

      while not routing.IsEnd(node):
        route += str(node) + ' -> '
        node = assignment.Value(routing.NextVar(node))
      route += '0'
      print "Route:\n\n" + route
    else:
      print 'No solution found.'
  else:
    print 'Specify an instance greater than 0.'
def create_data_array():


	return coordinates

if __name__ == '__main__':
  main()
