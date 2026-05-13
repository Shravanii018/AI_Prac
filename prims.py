# ---------- Prim's Algorithm ----------

def prims(graph, start):

    visited = [start]

    total_cost = 0

    mst_path = []

    print("\nEdges in Minimum Spanning Tree:\n")

    while len(visited) < len(graph):

        minimum = 999

        a = b = None

        # Check visited vertices
        for i in visited:

            # Check neighbors
            for j in graph[i]:

                # Find minimum edge
                if j not in visited and graph[i][j] < minimum:

                    minimum = graph[i][j]

                    a = i
                    b = j

        print(a, "-", b, "=", minimum)

        mst_path.append(f"{a}-{b}")

        total_cost += minimum

        visited.append(b)

    print("\nMinimum Spanning Tree Path:")

    print(" -> ".join(mst_path))

    print("\nTotal Cost =", total_cost)


# ---------- Graph Input ----------

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):

    node = input(f"\nEnter vertex {i+1}: ")

    neighbors = {}

    m = int(input(f"Enter number of neighbors of {node}: "))

    for j in range(m):

        neighbor = input("Enter neighbor: ")

        weight = int(input("Enter weight: "))

        neighbors[neighbor] = weight

    graph[node] = neighbors


# ---------- Start Vertex ----------

start = input("\nEnter starting vertex: ")


# ---------- Output ----------

prims(graph, start)