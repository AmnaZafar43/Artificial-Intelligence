import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []
    
    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append((to_node, cost))

def uniform_cost_search(graph, start, goal):
    # Priority queue to store nodes to be explored, sorted by path cost
    priority_queue = [(0, start, [])]  # (cost, node, path)
    
    # Dictionary to keep track of visited nodes and their associated cost
    visited = {}
    
    while priority_queue:
        # Get the node with the lowest cost from the priority queue
        current_cost, current_node, current_path = heapq.heappop(priority_queue)
        
        # If the current node is the goal, return the cost and path
        if current_node == goal:
            return current_cost, current_path + [current_node]
        
        # Skip this node if we have already visited it with a lower cost
        if current_node in visited and visited[current_node] < current_cost:
            continue
        
        # Mark the current node as visited
        visited[current_node] = current_cost
        
        # Explore neighboring nodes
        for neighbor, neighbor_cost in graph.edges[current_node]:
            if neighbor not in visited or visited[neighbor] > current_cost + neighbor_cost:
                heapq.heappush(priority_queue, (current_cost + neighbor_cost, neighbor, current_path + [current_node]))
    
    # If no path is found, return None
    return None


my_graph = Graph()
#adding nodes
my_graph.add_node("A")
my_graph.add_node("B")
my_graph.add_node("C")
my_graph.add_node("D")
my_graph.add_node("E")
my_graph.add_node("F")
my_graph.add_node("G")
my_graph.add_node("H")
my_graph.add_node("I")
my_graph.add_node("J")
#adding edges
my_graph.add_edge("A", "B",cost=6)
my_graph.add_edge("A", "F",cost=3)
my_graph.add_edge("B", "D",cost=2)
my_graph.add_edge("B", "C",cost=3)
my_graph.add_edge("C", "D",cost=1)
my_graph.add_edge("C", "E",cost=5)
my_graph.add_edge("D", "E",cost=8)
my_graph.add_edge("E", "J",cost=5)
my_graph.add_edge("E", "I",cost=5)
my_graph.add_edge("F", "G",cost=1)
my_graph.add_edge("F", "H",cost=7)
my_graph.add_edge("G", "I",cost=3)
my_graph.add_edge("H", "I",cost=2)
my_graph.add_edge("I", "J",cost=3)

start_node = 'A'
goal_node = 'J'
#print path
result = uniform_cost_search(my_graph, start_node, goal_node)
if result is not None:
        cost, path = result
        print(f"Shortest path cost from {start_node} to {goal_node} is {cost}")
        print(f"Shortest path: {' -> '.join(path)}")
else:
        print(f"No path found from {start_node} to {goal_node}")