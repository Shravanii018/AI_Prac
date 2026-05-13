import heapq

# ---------- A* Algorithm ----------
def a_star(graph, heuristic, start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    g = {start: 0}
    parent = {start: None}

    closed_list = set()

    while open_list:

        f, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current:
                path.append(current)
                current = parent[current]

            return path[::-1]

        closed_list.add(current)

        for neighbor, cost in graph[current].items():

            if neighbor in closed_list:
                continue

            new_cost = g[current] + cost

            if neighbor not in g or new_cost < g[neighbor]:

                g[neighbor] = new_cost

                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))

                parent[neighbor] = current

    return None


# ---------- Graph Input ----------
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):

    node = input(f"\nEnter node {i+1}: ")

    neighbors = {}

    m = int(input(f"Enter number of neighbors of {node}: "))

    for j in range(m):

        neighbor = input("Enter neighbor: ")

        cost = int(input("Enter cost: "))

        neighbors[neighbor] = cost

    graph[node] = neighbors


# ---------- Heuristic Input ----------
heuristic = {}

print("\nEnter heuristic values:")

for node in graph:
    heuristic[node] = int(input(f"h({node}) = "))


# ---------- Start & Goal ----------
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")


# ---------- Output ----------
path = a_star(graph, heuristic, start, goal)

if path:
    print("\nShortest Path:", " -> ".join(path))
else:
    print("No path found")