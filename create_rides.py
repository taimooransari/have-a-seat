import random
from pyrebase_init import post_ride

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


def getShortestPath(graph, source, to):
  path = []
  dist = Dijkstra(graph, source)
  node = dist[to][0]
  path.append((node, to))
  while node != source:
    n_node = dist[node][0]
    path.append((n_node, node))
    node = n_node
  return [path[::-1],dist[to][1]]


graph = {'Airport': [('Habib University', 7.5), ('Shahra-e-Faisal', 12)], 'Azizabad': [('Yaseenabad', 1.8), ('Gulshan-e-Iqbal', 7.2), ('Liaquatabad', 4.3)], 'Clifton': [('Shahra-e-Faisal', 17)], 'Defense': [('Shahra-e-Faisal', 14), ('Korangi', 6.2)], 'Federal B Area': [('Gulshan-e-Iqbal', 8.9), ('Yaseenabad', 3.1), ('Liaquatabad', 3.1)], 'Garden East': [('Saddar', 3.1)], 'Garden West': [('Saddar', 2.7)], 'Gulberg': [('Gulshan-e-Iqbal', 4.9), ('Nazimabad', 8), ('Samanabad', 1.8)], 'Gulistan-e-Jauhar': [('Habib University', 2.8), ('Gulshan-e-Jamal', 3.7), ('Gulshan-e-Iqbal', 5), ('Gulzar-e-Hijri', 6), ('Malir Cantt', 13)], 'Gulshan-e-Hadeed': [('Landhi Town', 19)], 'Gulshan-e-Iqbal': [('Gulistan-e-Jauhar', 5), ('Scheme 33', 5.4), ('Rashid Minhas', 3), ('Nazimabad', 9.7), ('North Karachi', 8.3), ('Gulberg', 4.9), ('Samanabad', 6.7), ('Yaseenabad', 6.4), ('Federal B Area', 8.9), ('Azizabad', 7.2)], 'Gulshan-e-Jamal': [('Gulistan-e-Jauhar', 3.7), ('Rashid Minhas', 3.8)], 'Gulzar-e-Hijri': [('Gulistan-e-Jauhar', 6), ('Scheme 33', 0.5), ('Malir Cantt', 13)], 'Habib University': [('Gulistan-e-Jauhar', 2.8), ('Airport', 7.5), ('Pehelwan Goth', 2.9)], 'Kharadar': [('Saddar', 4.7)], 'Korangi': [('Shahra-e-Faisal', 9.6), ('Defense', 6.2)], 'Landhi Town': [('Shahra-e-Faisal', 19), ('Gulshan-e-Hadeed', 19)], 'Liaquatabad': [('Federal B Area', 3.1), ('Azizabad', 4.3)], 'Malir Cantt': [('Shahra-e-Faisal', 20), ('Gulzar-e-Hijri', 13), ('Gulistan-e-Jauhar', 13)], 'Nazimabad': [('Gulshan-e-Iqbal', 9.7), ('Surjani Town', 17), ('Gulberg', 8)], 'North Karachi': [('Gulshan-e-Iqbal', 8.3), ('Surjani Town', 8.3)], 'Pehelwan Goth': [('Habib University', 2.9), ('Scheme 33', 7.7)], 'Rashid Minhas': [('Gulshan-e-Iqbal', 3), ('Gulshan-e-Jamal', 3.8)], 'Saddar': [('Shahra-e-Faisal', 12), ('Garden East', 3.1), ('Garden West', 2.7), ('Kharadar', 4.7)], 'Samanabad': [('Gulshan-e-Iqbal', 6.7), ('Gulberg', 1.8), ('Yaseenabad', 2.8)], 'Scheme 33': [('Pehelwan Goth', 7.7), ('Gulzar-e-Hijri', 0.5), ('Gulshan-e-Iqbal', 5.4)], 'Shahra-e-Faisal': [('Airport', 12), ('Clifton', 17), ('Saddar', 12), ('Defense', 14), ('Korangi', 9.6), ('Landhi Town', 19), ('Malir Cantt', 20)], 'Surjani Town': [('Nazimabad', 17), ('North Karachi', 8.3)], 'Yaseenabad': [('Gulshan-e-Iqbal', 6.4), ('Samanabad', 2.8), ('Federal B Area', 3.1), ('Azizabad', 1.8)]}


def create_ride(user, starting_time, type, point, available_seats,graph = graph):
    ride_info= {}
    code = random.randint(1,99999)
    if type == "incoming":
        path,distance = getShortestPath(graph, point, "Habib University")
        ride_info = {"Host": user['uid'], "Path" : path,'dist':distance ,"Available Seats" : available_seats,
         "Starting Time" : starting_time, "Booked Users" : [user['uid']],'code':code}
    elif type == "outgoing":
        path,distance = getShortestPath(graph, "Habib University", point)
        ride_info = {"Host": user['uid'], "Path" : path,'dist':distance, "Available Seats" : available_seats,
         "Starting Time" : starting_time, "Booked Users" : [user['uid']],'code':code}
    user = post_ride(ride_info,user['uid'])
    return user

