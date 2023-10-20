class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)

    def get_connected_nodes(self, node):
        #we check if node exist in already exist in adjacency list
        if node in self.adjacency_list:
            return self.adjacency_list[node]
        else:
            return []

graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")

connected_nodes = graph.get_connected_nodes("B")
print(connected_nodes) 
