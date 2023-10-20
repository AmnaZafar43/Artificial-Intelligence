class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}
        
    def add_node(self, data):
        if data not in self.nodes:
            new_node = Node(data)
            self.nodes[data] = new_node
        
    def add_edge(self, source, destination):
        if source in self.nodes and destination in self.nodes:
            self.nodes[source].neighbors.append(destination)
    def delete_edge(self, source, destination):
        if source in self.nodes and destination in self.nodes:
            if destination in self.nodes[source].neighbors:
                self.nodes[source].neighbors.remove(destination)

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.nodes[node].neighbors)


my_graph = Graph()
print('Adding nodes to graphs')
my_graph.add_node("A")
my_graph.add_node("B")
my_graph.add_node("C")
my_graph.add_node("D")
print('Adding edges to graphs')
my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "A")
my_graph.add_edge("D", "A")
print('Print Graph')
my_graph.print_graph()

    # Deleting an edge
my_graph.delete_edge("C", "A")
print('Print graph after deleting edge')
    # Printing the graph after deleting an edge
my_graph.print_graph()
