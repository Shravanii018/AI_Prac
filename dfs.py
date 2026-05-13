# ---------- Create Graph ----------
graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):

    node = input(f"\nEnter vertex {i+1}: ")

    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()

    graph[node] = neighbors


# ---------- DFS ----------
visited = set()

def dfs(node):

    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:

            dfs(neighbor)


# ---------- Start ----------
start = input("\nEnter starting node: ")

print("\nDFS Traversal:")

dfs(start)