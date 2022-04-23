import math
import random
from webbrowser import get
from pyrebase_init import post_ride,get_rides,get_specific_rides





def Dijkstra(graph, source):
  dist = {}
  dist[source] = [source, 0]
  for vertex in graph:
      if vertex != source:
          dist[vertex] = ['-', 1000000000000000000]

  visited = []
  while len(visited) != len(dist):
    min_cost = 1000000000000000000
    for node in dist:
      if node not in visited and dist[node][1] < min_cost:
        min_node = node
        min_cost = dist[node][1]
    visited.append(min_node)
    for neighbor in graph[min_node]:
      cost = dist[min_node][1] + neighbor[1]
      if dist[neighbor[0]][1] > cost:
        dist[neighbor[0]][1] = cost
        dist[neighbor[0]][0] = min_node
  return dist

# print(Dijkstra(G, 'A'))

def getShortestPath(graph, source, to):
  path = []
  dist = Dijkstra(graph, source)
  node = dist[to][0]
  path.append((node, to))
  while node != source:
    n_node = dist[node][0]
    path.append((n_node, node))
    node = n_node
  return path[::-1]





booked = ["A", "B", "C"]
graph = {}

def create_ride(user, starting_time, type, point, available_seats):
    #type can be incoming(coming to Habib) or outgoing(going from Habib)
    ride_info= {}
    path = [1,2,3,4,5,6,7]
    code = random.randint(1,99999)
    if type == "incoming":
        # path = getShortestPath(graph, point, "Habib")
        ride_info = {"Host": user['uid'], "Path" : path, "Available Seats" : available_seats,
         "Starting Time" : starting_time, "Booked Users" : booked,'code':code}
    elif type == "outgoing":
        # path = getShortestPath(graph, "Habib", point)
        ride_info = {"Host": user['uid'], "Path" : path, "Available Seats" : available_seats,
         "Starting Time" : starting_time, "Booked Users" : booked,'code':code}
    user = post_ride(ride_info,user['uid'])
    return user
# user={'contact': '37409', 'dob': 'jaiohf8', 'email': 'vania@gmail.com', 'father': 'imran', 'name': 'vania', 'rides': [1], 'uid': 'Hfnx1gTWrRaJws81fuxEcOx2qeC3'}
# print(create_ride(user,'7:00 PM', 'incoming'))

# print(get_rides())
# a=get_specific_rides([54098])
# print(a[0]['Starting Time'])
