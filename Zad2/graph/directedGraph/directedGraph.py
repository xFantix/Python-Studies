import networkx as nx


class DirectedGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def get_adjacency_matrix(self):
        return nx.to_numpy_matrix(self.graph)

    def get_adjacency_list(self):
        return {str(node): list(self.graph.successors(node)) for node in self.graph.nodes()}

    def get_num_vertices(self):
        return len(self.graph)

    def get_num_edges(self):
        return self.graph.size()

    def get_neighbors(self, vertex):
        return list(self.graph.successors(vertex))

    def get_degree(self, vertex):
        return (self.graph.out_degree(vertex), self.graph.in_degree(vertex))

    def add_vertex(self, vertex):
        self.graph.add_node(vertex)

    def add_edge(self, start_vertex, end_vertex):
        self.graph.add_edge(start_vertex, end_vertex)

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.get_neighbors(vertex):
                    stack.append(neighbor)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.get_neighbors(vertex):
                    queue.append(neighbor)