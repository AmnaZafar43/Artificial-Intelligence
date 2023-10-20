class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.adjacent_nodes = {}
        self.g_cost = float('inf')
        self.parent = None

    def add_neighbor(self, neighbor, cost):
        self.adjacent_nodes[neighbor] = cost

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, heuristic):
        self.nodes[name] = Node(name, heuristic)

    def add_edge(self, node1, node2, cost):
        self.nodes[node1].add_neighbor(node2, cost)
        self.nodes[node2].add_neighbor(node1, cost)

def astar(graph, start, goal):
    open_set = []
    closed_set = set()
    start_node = graph.nodes[start]
    start_node.g_cost = 0
    open_set.append((start_node.g_cost + start_node.heuristic, start_node))

    while open_set:
        open_set.sort()  # Sort the open set by f(n) = g(n) + h(n)
        _, current_node = open_set.pop(0)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return list(reversed(path))
        closed_set.add(current_node.name)
        for neighbor_name, cost in current_node.adjacent_nodes.items():
            neighbor = graph.nodes[neighbor_name]
            if neighbor_name in closed_set:
                continue
            tentative_g_cost = current_node.g_cost + cost
            if tentative_g_cost < neighbor.g_cost:
                neighbor.parent = current_node
                neighbor.g_cost = tentative_g_cost
                f_score = tentative_g_cost + neighbor.heuristic
                open_set.append((f_score, neighbor))
    return None


my_graph = Graph()
#adding nodes
my_graph.add_node("A",heuristic=10)
my_graph.add_node("B",heuristic=8)
my_graph.add_node("C",heuristic=5)
my_graph.add_node("D",heuristic=7)
my_graph.add_node("E",heuristic=3)
my_graph.add_node("F",heuristic=6)
my_graph.add_node("G",heuristic=5)
my_graph.add_node("H",heuristic=3)
my_graph.add_node("I",heuristic=1)
my_graph.add_node("J",heuristic=0)
#adding edges
my_graph.add_edge("A", "B",cost=6)
my_graph.add_edge("A", "F",cost=3)
my_graph.add_edge("B", "A",cost=6)
my_graph.add_edge("B", "D",cost=2)
my_graph.add_edge("B", "C",cost=3)
my_graph.add_edge("C", "B",cost=3)
my_graph.add_edge("C", "D",cost=1)
my_graph.add_edge("C", "E",cost=5)
my_graph.add_edge("D", "B",cost=2)
my_graph.add_edge("D", "C",cost=1)
my_graph.add_edge("D", "E",cost=8)
my_graph.add_edge("E", "D",cost=8)
my_graph.add_edge("E", "J",cost=5)
my_graph.add_edge("E", "I",cost=5)
my_graph.add_edge("F", "A",cost=3)
my_graph.add_edge("F", "G",cost=1)
my_graph.add_edge("F", "H",cost=7)
my_graph.add_edge("G", "F",cost=1)
my_graph.add_edge("G", "I",cost=3)
my_graph.add_edge("H", "F",cost=7)
my_graph.add_edge("H", "I",cost=2)
my_graph.add_edge("I", "G",cost=3)
my_graph.add_edge("I", "H",cost=2)
my_graph.add_edge("I", "J",cost=3)
my_graph.add_edge("I", "E",cost=5)
my_graph.add_edge("J", "I",cost=3)
my_graph.add_edge("J", "E",cost=5)

#print graph
def print_graph(graph):
    print("Graph:")
    for node_name, node in graph.nodes.items():
        print(f"Node: {node_name}, Heuristic: {node.heuristic}")
        for neighbor, cost in node.adjacent_nodes.items():
            print(f"  -> Neighbor: {neighbor}, Cost: {cost}")
    print("\n")
start_node = 'A'
goal_node = 'J'
#print path
path = astar(my_graph, start_node, goal_node)
if path:
        print(f"Shortest Path from {start_node} to {goal_node}: {path}")
else:
        print(f"No path found from {start_node} to {goal_node}")