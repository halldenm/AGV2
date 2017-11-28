import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1,y1) = a
    (x2,y2) = b
    return (abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5

def a_star_search(graph, start, goal, reservationList):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    #print(came_from)
    
    while not frontier.empty():
        current = frontier.get()
        #print(current)
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in reservationList:
                new_cost = cost_so_far[current] + graph[current][next]['weight']
                #print(new_cost)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    #print(graph.nodes[goal]['pos'])
                    fitness = new_cost + heuristic(graph.nodes[goal]['pos'], graph.nodes[next]['pos'])
                    frontier.put(next, fitness)
                    came_from[next] = current

    node = goal
    path = [node]
    while node != start:
        path.insert(0,came_from[node])
        node = came_from[node]

    return path, cost_so_far[goal]