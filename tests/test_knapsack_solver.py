import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_cannot_include_any_item():
    """Test when capacity is too small to include any items"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 5
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 0
    assert selected_items == []

def test_can_include_all_items():
    """Test when capacity is larger than total weight"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 100
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 280
    assert set(selected_items) == {0, 1, 2}

def test_float_inputs():
    """Test with float weights and values"""
    weights = [10.5, 20.3, 30.2]
    values = [60.1, 100.2, 120.3]
    capacity = 50.5
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 160.3
    assert set(selected_items) == {0, 1}

def test_invalid_weight_list():
    """Test with invalid weight list"""
    with pytest.raises(ValueError, match="Weights and values must be lists"):
        solve_knapsack("not a list", [1, 2, 3], 50)

def test_mismatched_list_lengths():
    """Test with mismatched weights and values lists"""
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        solve_knapsack([1, 2], [10, 20, 30], 50)

def test_negative_weights():
    """Test with negative weights"""
    with pytest.raises(ValueError, match="Weights must be non-negative numbers"):
        solve_knapsack([-1, 2, 3], [10, 20, 30], 50)

def test_negative_values():
    """Test with negative values"""
    with pytest.raises(ValueError, match="Values must be non-negative numbers"):
        solve_knapsack([1, 2, 3], [-10, 20, 30], 50)

def test_negative_capacity():
    """Test with negative capacity"""
    with pytest.raises(ValueError, match="Capacity must be a non-negative number"):
        solve_knapsack([1, 2, 3], [10, 20, 30], -50)