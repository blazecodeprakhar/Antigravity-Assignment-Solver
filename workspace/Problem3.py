import heapq

def a_star_search(graph, heuristics, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristics[start], 0, start, [start]))
    visited = {}
    
    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        
        if current in visited and visited[current] <= g_score:
            continue
        visited[current] = g_score
        
        if current == goal:
            return path, g_score
            
        for neighbor, weight in graph.get(current, []):
            new_g = g_score + weight
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
            
    return None, float('inf')

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 10)],
    'C': [('E', 3), ('F', 8)],
    'D': [('G', 11)],
    'E': [('G', 4)],
    'F': [('G', 5)],
    'G': []
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 4,
    'G': 0
}

start_node = 'A'
goal_node = 'G'
path, total_cost = a_star_search(graph, heuristics, start_node, goal_node)

print("A* Search Algorithm (Node A to Node G)")
print("=" * 45)
print(f"Start Node         : {start_node}")
print(f"Goal Node          : {goal_node}")
print(f"Shortest Path Found: {' -> '.join(path)}")
print(f"Total Path Cost    : {total_cost}")
