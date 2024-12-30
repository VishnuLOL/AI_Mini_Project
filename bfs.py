from collections import deque
from adjancy_matrix_gen import return_matrix

def bi_dir_bfs(src, dest, adjacency_matrix, size):
    # Initialize forward and backward search queues and visited sets
    forward_queue = deque([src])
    backward_queue = deque([dest])
    
    forward_visited = {src: None}  # Node -> Parent for forward search
    backward_visited = {dest: None}  # Node -> Parent for backward search

    # Helper function to reconstruct the path
    def reconstruct_path(meeting_point):
        # Forward path
        path = []
        current = meeting_point
        while current is not None:
            path.append(current)
            current = forward_visited[current]
        path.reverse()
        
        # Backward path
        current = backward_visited[meeting_point]
        while current is not None:
            path.append(current)
            current = backward_visited[current]
        
        return path

    # Perform the bi-directional BFS
    while forward_queue and backward_queue:
        # Expand forward
        if forward_queue:
            current = forward_queue.popleft()
            for neighbor in range(size):
                if adjacency_matrix[current][neighbor] == 1 and neighbor not in forward_visited:
                    forward_visited[neighbor] = current
                    forward_queue.append(neighbor)
                    # Check for meeting point
                    if neighbor in backward_visited:
                        return reconstruct_path(neighbor)
        
        # Expand backward
        if backward_queue:
            current = backward_queue.popleft()
            for neighbor in range(size):
                if adjacency_matrix[current][neighbor] == 1 and neighbor not in backward_visited:
                    backward_visited[neighbor] = current
                    backward_queue.append(neighbor)
                    # Check for meeting point
                    if neighbor in forward_visited:
                        return reconstruct_path(neighbor)

    # If no path is found
    return []

# Example usage
adjacency_matrix, size = return_matrix()
src = 0  # Example starting point
dest = 399  # Example destination point
obstacles = [5, 6, 7]  # Example obstacles

# Remove obstacles from adjacency matrix
for obstacle in obstacles:
    for i in range(size):
        adjacency_matrix[i][obstacle] = 0
        adjacency_matrix[obstacle][i] = 0

path = bi_dir_bfs(src, dest, adjacency_matrix, size)
print("Path:", path)
