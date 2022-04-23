#Merge Sort

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2 #mid of the list
        left, right = lst[:mid], lst[mid:] #dividing the list into two halves
        merge_sort(right), merge_sort(left) #sorting the two halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst

#-------------------------------------------------------------------------------------------------------------------------#

#Dijkstra and shortest path algorithm

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
  dist = Dijkstra(G, source)
  node = dist[to][0]
  path.append((node, to))
  while node != source:
    n_node = dist[node][0]
    path.append((n_node, node))
    node = n_node
  return path[::-1]

#----------------------------------------------------------------------------------#

#Dijkstra2 - returns a list of the shortest path and total cost to get there

def dijkstra(graph,start,end):
    G = graph
    Gtemp={}
    for i in G:
        tempdict={}
        for j in G[i]:
            tempdict[j[0]]=j[1]
        Gtemp[i]=tempdict
    graph = Gtemp
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = 1000000000000000000000000
    track_path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node=node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        path_options=graph[min_distance_node].items()
        for child_node, weight in path_options:
             if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node
        unseenNodes.pop(min_distance_node)
    currentNode = end
    while currentNode != start: 
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("Path.is.not reachable") 
            break
    track_path.insert(0,start)
    if shortest_distance[end] != infinity:
        print(track_path)#shortest path
        print(shortest_distance[end])