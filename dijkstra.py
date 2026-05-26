# Problem: Dijkstra's Algorithm
# Difficulty: Intermediate
# Approach: Greedy shortest path using a min-heap (priority queue)
# Time Complexity: O((V + E) log V) with a binary heap
# Space Complexity: O(V + E)
#
# Problem Statement:
# Given a weighted graph represented as an adjacency list, find the
# shortest path from a source node to all other nodes using Dijkstra's
# algorithm. The graph must have non-negative edge weights.

import heapq


def dijkstra(graph, start):
    """
    Finds the shortest distances from the start node to all other nodes
    using Dijkstra's algorithm with a priority queue.

    Args:
        graph: Dictionary representing a weighted adjacency list.
               Format: {node: [(neighbor, weight), ...]}
        start: The source node.

    Returns:
        A tuple (distances, predecessors) where:
        - distances: Dict mapping each node to its shortest distance from start.
        - predecessors: Dict mapping each node to its predecessor on the
          shortest path (used to reconstruct paths).
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    # Min-heap: (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        # Skip if we've already found a shorter path
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, []):
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors


def reconstruct_path(predecessors, start, end):
    """
    Reconstructs the shortest path from start to end using the
    predecessors dictionary.

    Args:
        predecessors: Dict mapping each node to its predecessor.
        start: Source node.
        end: Destination node.

    Returns:
        List representing the path from start to end,
        or an empty list if no path exists.
    """
    path = []
    current = end

    while current is not None:
        path.append(current)
        if current == start:
            break
        current = predecessors.get(current)

    if not path or path[-1] != start:
        return []  # no path exists

    path.reverse()
    return path


# ---- Test Cases ----
if __name__ == "__main__":
    # Example weighted graph:
    #       A --4-- B
    #       |       |
    #       2       1
    #       |       |
    #       C --3-- D --5-- E
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("D", 1)],
        "C": [("A", 2), ("D", 3)],
        "D": [("B", 1), ("C", 3), ("E", 5)],
        "E": [("D", 5)]
    }

    distances, predecessors = dijkstra(graph, "A")

    print("--- Shortest Distances from A ---")
    for node, dist in sorted(distances.items()):
        print(f"  A -> {node}: {dist}")
    # Expected: A->A: 0, A->B: 4, A->C: 2, A->D: 5, A->E: 10

    print("\n--- Shortest Path from A to E ---")
    path = reconstruct_path(predecessors, "A", "E")
    print(f"  Path: {' -> '.join(path)}")    # Expected: A -> B -> D -> E or A -> C -> D -> E
    print(f"  Distance: {distances['E']}")   # Expected: 10

    print("\n--- Shortest Path from A to D ---")
    path = reconstruct_path(predecessors, "A", "D")
    print(f"  Path: {' -> '.join(path)}")    # Expected: A -> B -> D
    print(f"  Distance: {distances['D']}")   # Expected: 5
