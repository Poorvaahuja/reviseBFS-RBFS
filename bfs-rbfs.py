import heapq
def best_first_search(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (h(start, goal), start))
    came_from = {}
    visited = set()
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        visited.add(current)
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(open_list, (h(neighbor, goal), neighbor))
                came_from[neighbor] = current
                
        return None
    
graph = {'Arad' : [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)], 
         'Zerind' : [('Oradea', 71),('Arad', 75)],
         'Sibiu' : [('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Oradea', 151)],
         'Oradea' : [('Zerind', 71), ('Sibiu', 151)], 
         'Timisoara' : [('Arad', 118), ('Lugoj', 111)], 
         'Lugoj' : [('Timisoara', 111), ('Mehadia', 70)], 
         'Mehadia' : [('Lugoj', 70),('Drobeta', 75)], 
         'Drobeta' : [('Mehadia', 75), ('Craiova', 120)],
         'Craiova' : [('Drobeta', 120),('Rimnicu Vilcea', 146)], 
         'Rimnicu Vilcea' : [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)], 
         'Pitesti' : [('Rimnicu Vilcea', 97), ('Bucharest', 101)], 
         'Bucharest' : [('Giurgiu', 90), ('Pitesti', 101), ('Fagaras', 211)], 
         'Fagaras' : [('Bucharest', 211), ('Sibiu', 99)],
         'Giurgiu' : ('Bucharest', 90)
}
def heuristic(node, goal):
    distances = {'Arad' : 366, 'Bucharest' : 0, 'Craiova' : 160, 'Drobeta' : 242, 'Eforie' : 161, 'Fagaras' : 176, 'Giurgiu' : 77, 'Hirsova' : 151, 'Iasi' : 226, 'Lugoj' : 244, 'Mehadia' : 241, 'Neamt' : 234, 'Oradea' : 380, 'Pitesti' : 100, 'Rimnicu Vilcea' : 193, 'Sibiu' : 253, 'Timisoara' : 329, 'Urziceni' : 80, 'Vaslui' : 199, 'Zerind' : 374}
    return distances[node]

print(best_first_search(graph, 'Arad', 'Bucharest', heuristic))

def rbfs(graph, node, goal, f_limit, h):
    def search(path, g, bound):
        node = path[-1]
        f = g+h(node, goal)
        if f > bound:
            return f
        if node == goal:
            return path
        min_bound = float('inf')
        for neighbor, cost in graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                t = search(path, g+cost, bound)
                if isinstance(t, list):
                    return t
                if t < min_bound:
                    min_bound = t
                path.pop()
                
        return min_bound
    path = [node]
    bound = h(node, goal)
    while True:
        t = search(path, 0, bound)
        if isinstance(t, list):
            return t
        if t == float('inf'):
            return None
        bound = t
        
print("RBFS: "(rbfs(graph, 'Arad', 'Bucharest', float('inf'), heuristic)))