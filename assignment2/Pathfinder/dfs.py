from collections import deque
from node import Node

def dfs(start, end):
    queue = deque([start])
    visited = set()
    came_from = {}
    visit_history = []

    while queue:
        current = queue.pop()
        if current in visited:
            continue

        visited.add(current)
        visit_history.append(current)
        if current == end:
            return reconstruct_path(came_from, current), visit_history

        for neighbor in current.get_neighbors():
            if neighbor not in visited  and neighbor and neighbor.type != 'wall':
                queue.append(neighbor)
                if neighbor not in came_from:
                    came_from[neighbor] = current

    return None  # No path found

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path