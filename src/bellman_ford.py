from typing import List, Tuple, Dict, Optional

def bellman_ford(graph: List[Tuple[int, int, int]], source: int, num_vertices: int) -> Optional[Dict[int, float]]:
    """
    Implement the Bellman-Ford algorithm to find shortest paths from a source vertex.
    
    Args:
        graph (List[Tuple[int, int, int]]): List of edges, where each edge is (from, to, weight)
        source (int): Source vertex to start from
        num_vertices (int): Total number of vertices in the graph
    
    Returns:
        Optional[Dict[int, float]]: Dictionary of shortest distances from source, 
        or None if negative cycle is detected
    
    Raises:
        ValueError: If source vertex is invalid or graph is improperly formatted
    """
    # Validate input
    if source < 0 or source >= num_vertices:
        raise ValueError("Invalid source vertex")
    
    # Initialize distances
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    
    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        
        # If no updates, we can stop early
        if not updated:
            break
    
    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected
    
    # Convert to dictionary for easier access
    return {i: dist for i, dist in enumerate(distances)}