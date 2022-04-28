# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:

	def __init__(self):
		
		self.visual = []
	def addEdge(self, a, b):
		temp = [a, b]
		self.visual.append(temp)
	
	def visualize(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G)
		plt.show()

def show_path(edges):
	G = GraphVisualization()
	if(len(edges[0])==3):
		for s,t,w in edges:
			G.addEdge(s,t)
		return G
	else:
		for s,t in edges:
			G.addEdge(s,t)
		return G
