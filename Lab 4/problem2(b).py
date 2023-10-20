def DFS(graph, start, goal):
    # Initialize a stack for DFS
    stack = [start]
    visited = {}
    visited[start] = None  
    while stack:
        current_node = stack.pop()
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = visited[current_node]
            return path[::-1] 
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Mark the neighbor as visited and push it onto the stack
                stack.append(neighbor)
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

result = DFS(graph, start_node, goal_node)
print(result)
