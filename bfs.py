from collections import deque

# ---------- Create Graph ----------
graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):

    node = input(f"\nEnter vertex {i+1}: ")

    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()

    graph[node] = neighbors


# ---------- BFS ----------
def bfs(start):

    visited = set()

    queue = deque([start])

    visited.add(start)

    while queue:

        current = queue.popleft()

        print(current, end=" ")

        for neighbor in graph[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)


# ---------- Start ----------
start = input("\nEnter starting node: ")

print("\nBFS Traversal:")

bfs(start)