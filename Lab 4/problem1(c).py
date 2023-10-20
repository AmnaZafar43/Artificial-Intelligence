#dictionary as adjacency list where node is a key, and value is a list of its neighboring nodes.
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def get_edge(self, node1, node2):
        if node1 in self.graph:
            # Check edge between node1 and node2
            if node2 in self.graph[node1]:
                return (node1, node2)  
        return None  

my_graph = Graph()
my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "D")

edge = my_graph.get_edge("B", "C")
print(edge) 

edge = my_graph.get_edge("A", "D")
print(edge)
