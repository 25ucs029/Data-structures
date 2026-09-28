from collections import deque


# BFS Traversal
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    traversal = []

    while queue:
        user = queue.popleft()
        traversal.append(user)

        for friend in graph[user]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)

    return traversal


# DFS Traversal
def dfs(graph, start):
    visited = set()
    stack = [start]

    traversal = []

    while stack:
        user = stack.pop()

        if user not in visited:
            visited.add(user)
            traversal.append(user)

            # Reverse order because stack follows LIFO
            for friend in reversed(graph[user]):
                if friend not in visited:
                    stack.append(friend)

    return traversal


# Number of users
n = int(input("Enter no. of users: "))

# Create social network
graph = {i: [] for i in range(n + 1)}

# Number of friendships
m = int(input("Enter no. of friendships: "))

print("Enter the friendships:")

for i in range(m):
    u, v = map(int, input().split())

    # Undirected graph
    graph[u].append(v)
    graph[v].append(u)


# Sort friends so traversal order is consistent
for user in graph:
    graph[user].sort()


# Display social network
print("\nSocial Network:")

for user in graph:
    print(user, "->", graph[user])


# Find friends of a particular user
friend_user = int(input("\nEnter user to find friends: "))

if friend_user in graph:
    print("Friends of user", friend_user, ":", graph[friend_user])
else:
    print("User not found.")


# Starting user for BFS and DFS
start = int(input("Enter starting user for BFS and DFS: "))

if start not in graph:
    print("Invalid starting user.")
else:
    # BFS
    bfs_result = bfs(graph, start)

    print("\nBFS Traversal:")
    print(" ".join(map(str, bfs_result)))

    # DFS
    dfs_result = dfs(graph, start)

    print("\nDFS Traversal:")
    print(" ".join(map(str, dfs_result)))
