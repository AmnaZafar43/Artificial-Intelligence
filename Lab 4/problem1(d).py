#represent the graph using an adjacency list, where each node has a list of its neighbouring nodes.
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []

        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def are_connected(self, node1, node2):
        #we check if node1 is in adjacency list
        if node1 in self.adjacency_list:
            return node2 in self.adjacency_list[node1]
        return False

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

print(graph.are_connected(1, 2))  
print(graph.are_connected(1, 3))  
