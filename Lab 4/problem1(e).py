class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

    def is_valid_path(self, path):
        # we check if there is only one edge or no edge
        if len(path) < 2:
            return False
        for i in range(len(path) - 1):
            node1 = path[i]
            node2 = path[i + 1]
            #we check if node1 is not in graph or node2 is not neighbour of node 1
            if node1 not in self.graph or node2 not in self.graph[node1]:
                return False
        return True


graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")

path1 = ["A", "B", "C", "D"]
path2 = ["A", "B", "D"]

print(graph.is_valid_path(path1)) 
print(graph.is_valid_path(path2))  
