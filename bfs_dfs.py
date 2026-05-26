# Problem: BFS and DFS on a Graph
# Difficulty: Intermediate
# Approach: Adjacency list representation with iterative BFS and
#           both iterative and recursive DFS
# Time Complexity: O(V + E) for both BFS and DFS
# Space Complexity: O(V) for the visited set and queue/stack
#
# Problem Statement:
# Given a graph represented as an adjacency list, perform Breadth-First
# Search (BFS) and Depth-First Search (DFS) traversals starting from
# a given source node.

from collections import deque


def bfs(graph, start):
    """
    Performs Breadth-First Search traversal on the graph.
    Explores all neighbors at the current depth before moving deeper.

    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}.
        start: Starting node for traversal.

    Returns:
        List of nodes in BFS traversal order.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs_iterative(graph, start):
    """
    Performs Depth-First Search traversal iteratively using a stack.
    Explores as deep as possible before backtracking.

    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}.
        start: Starting node for traversal.

    Returns:
        List of nodes in DFS traversal order.
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)

            # Add neighbors in reverse order so leftmost is visited first
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def dfs_recursive(graph, start, visited=None):
    """
    Performs Depth-First Search traversal recursively.
    Explores as deep as possible before backtracking.

    Args:
        graph: Dictionary representing adjacency list {node: [neighbors]}.
        start: Starting node for traversal.
        visited: Set of already-visited nodes (used internally).

    Returns:
        List of nodes in DFS traversal order.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# ---- Test Cases ----
if __name__ == "__main__":
    # Example graph:
    #     A --- B
    #     |     |
    #     C --- D --- E
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"]
    }

    print("--- BFS ---")
    print(bfs(graph, "A"))               # Expected: ['A', 'B', 'C', 'D', 'E']

    print("\n--- DFS (Iterative) ---")
    print(dfs_iterative(graph, "A"))     # Expected: ['A', 'B', 'D', 'C', 'E']

    print("\n--- DFS (Recursive) ---")
    print(dfs_recursive(graph, "A"))     # Expected: ['A', 'B', 'D', 'C', 'E']

    # Disconnected graph
    disconnected = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    print("\n--- BFS on disconnected (from node 1) ---")
    print(bfs(disconnected, 1))          # Expected: [1, 2]

    print("\n--- DFS on disconnected (from node 3) ---")
    print(dfs_iterative(disconnected, 3))  # Expected: [3, 4]
