from collections import deque

def BFS(graph, start, goal):
    queue = deque()
    # for visited nodes
    visited = {} 
    queue.append(start)
    #starting node has no parent that's why i initialize it with none
    visited[start] = None

    while queue:
        # Dequeue the next node
        current_node = queue.popleft()  
        if current_node == goal:
            # Return the path from start to goal
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            return path[::-1]  # Reverse the path to get it from start to goal
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Neighbours are visited now and we enqueue them now
                queue.append(neighbor)
                visited[neighbor] = current_node
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
goal_node = 'E'

result = BFS(graph, start_node, goal_node)
print(result)
