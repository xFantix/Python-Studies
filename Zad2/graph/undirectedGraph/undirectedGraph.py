import networkx as nx
from directedGraph.directedGraph import DirectedGraph

class UndirectedGraph(DirectedGraph):
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, vertex1, vertex2):
        self.graph.add_edge(vertex1, vertex2)