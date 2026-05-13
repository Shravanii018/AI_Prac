# ---------- Find Parent ----------
def find(parent, i):

    if parent[i] == i:
        return i

    return find(parent, parent[i])


# ---------- Union ----------
def union(parent, x, y):

    parent[x] = y


# ---------- Kruskal Algorithm ----------
def kruskal(graph, vertices):

    # Sort edges by weight
    graph.sort()

    parent = {}

    # Make each vertex its own parent
    for v in vertices:
        parent[v] = v

    total_cost = 0

    mst_path = []

    edge_count = 0

    print("\nEdges in Minimum Spanning Tree:\n")

    for weight, a, b in graph:

        x = find(parent, a)
        y = find(parent, b)

        # Check cycle
        if x != y:

            print(a, "-", b, "=", weight)

            mst_path.append(f"{a}-{b}")

            total_cost += weight

            union(parent, x, y)

            edge_count += 1

            # MST complete
            if edge_count == len(vertices) - 1:
                break

    print("\nMinimum Spanning Tree Path:")

    print(" -> ".join(mst_path))

    print("\nTotal Cost =", total_cost)


# ---------- Input ----------

graph = []

vertices = set()

n = int(input("Enter number of edges: "))

print("\nEnter edges and weights:\n")

for i in range(n):

    a = input("Enter first vertex: ")

    b = input("Enter second vertex: ")

    weight = int(input("Enter weight: "))

    graph.append([weight, a, b])

    vertices.add(a)
    vertices.add(b)


# ---------- Output ----------

kruskal(graph, vertices)