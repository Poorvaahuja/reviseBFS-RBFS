def steepest_ascent_hill_climb(problem):
    current = problem.initial_state()
    while True:
        neighbors = problem.neighbors(current)
        if not neighbors:
            break
        neighbor = max(neighbors, key = problem.value)
        if problem.value(neighbor) <= problem.value(current):
            break
        current = neighbor
    return current

import random
def stochastic_hill_climb(problem):
    current = problem.initial_state()
    while True:
        neighbors = problem.neighbors(current)
        if not neighbors:
            break
        better_neighbor = [n for n in neighbors if problem.value(n) > problem.value(current)]
        if not better_neighbor:
            break
        current = random.choice(better_neighbor)
    return current

def first_choice_hill_climbing(problem):
    current = problem.initial_state()
    while True:
        neighbors = problem.neighbors(current)
        if not neighbors:
            break
        random.shuffle(neighbors)
        for neighbor in neighbors:
            if problem.value(neighbor) > problem.value(current):
                current = neighbor
        else:
            break
    return current


def random_restart_hill_climbing(problem, max_restarts = 10):
    best_solution = None
    for _ in range(max_restarts):
        solution = steepest_ascent_hill_climb(problem)
        if best_solution is None or problem.value(solution) > problem.value(best_solution):
            best_solution = solution
            
    return best_solution

def local_beam_search(problem, k=3):
    states = [problem.initial_state() for _ in range(k)]
    while True:
        all_neighbors = []
        for state in states:
            all_neighbors.extend(problem.neighbors(state))
        if not all_neighbors:
            break
        states = sorted(all_neighbors, key = problem.value, reverse = True)[:k]
        if all(problem.value(state) == problem.value(states[0]) for state in states):
            break
    return states[0]


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



class RomaniaProblem:
    def __init__(self, initial, goal, graph, heuristic):
        self.initial = initial
        self.goal = goal
        self.graph = graph
        self.heuristic = heuristic

    def initial_state(self):
        return self.initial

    def neighbors(self, state):
        return [neighbor for neighbor, _ in self.graph[state]]

    def value(self, state):
        return -self.heuristic(state, self.goal)

problem_instance = RomaniaProblem('Arad', 'Bucharest', graph, heuristic)

print(steepest_ascent_hill_climb(problem_instance))
print(stochastic_hill_climb(problem_instance))
print(first_choice_hill_climbing(problem_instance))
print(random_restart_hill_climbing(problem_instance))
print(local_beam_search(problem_instance))