import pytest
import sys
import os

# Ensure src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bellman_ford import bellman_ford

def test_basic_shortest_path():
    """Test a simple graph with positive weights"""
    graph = [
        (0, 1, 4),  # from 0 to 1, weight 4
        (0, 2, 3),  # from 0 to 2, weight 3
        (1, 2, 1),  # from 1 to 2, weight 1
        (1, 3, 2),  # from 1 to 3, weight 2
        (2, 3, 5)   # from 2 to 3, weight 5
    ]
    num_vertices = 4
    source = 0
    
    result = bellman_ford(graph, source, num_vertices)
    
    assert result is not None
    assert result[0] == 0    # distance to source is 0
    assert result[1] == 4    # distance to vertex 1
    assert result[2] == 3    # distance to vertex 2
    assert result[3] == 6    # distance to vertex 3

def test_negative_weights():
    """Test a graph with negative weights (but no negative cycles)"""
    graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (3, 2, 5)
    ]
    num_vertices = 4
    source = 0
    
    result = bellman_ford(graph, source, num_vertices)
    
    assert result is not None
    assert result[0] == 0
    assert result[1] == -1
    assert result[2] == 2
    assert result[3] == 1

def test_negative_cycle_detection():
    """Test detection of negative weight cycles"""
    graph = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 0, -2)  # Creates a negative cycle
    ]
    num_vertices = 3
    source = 0
    
    result = bellman_ford(graph, source, num_vertices)
    
    assert result is None

def test_invalid_source_vertex():
    """Test handling of invalid source vertex"""
    graph = [
        (0, 1, 4),
        (0, 2, 3)
    ]
    num_vertices = 3
    
    with pytest.raises(ValueError):
        bellman_ford(graph, -1, num_vertices)
    
    with pytest.raises(ValueError):
        bellman_ford(graph, 3, num_vertices)

def test_disconnected_graph():
    """Test a graph with unreachable vertices"""
    graph = [
        (0, 1, 4),
        (0, 2, 3)
    ]
    num_vertices = 4
    source = 0
    
    result = bellman_ford(graph, source, num_vertices)
    
    assert result is not None
    assert result[0] == 0
    assert result[1] == 4
    assert result[2] == 3
    assert result[3] == float('inf')

def test_empty_graph():
    """Test an empty graph"""
    graph = []
    num_vertices = 1
    source = 0
    
    result = bellman_ford(graph, source, num_vertices)
    
    assert result is not None
    assert result[0] == 0
    assert len(result) == 1