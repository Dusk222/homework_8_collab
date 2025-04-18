from exercise_2 import index_power

def test_valid_index():
    assert index_power([1, 2, 3, 4], 2) == 9
    assert index_power([1, 3, 10, 100], 3) == 1000000

def test_index_out_of_bounds():
    assert index_power([1, 2, 3], 3) == -1
    assert index_power([1, 2], 3) == -1

def test_zero_index():
    assert index_power([0, 1], 0) == 1
    assert index_power([5, 6, 7], 0) == 1

def test_negative_index():
    assert index_power([1, 2, 3], -1) == -1
    assert index_power([1, 2, 3], -5) == -1

def test_large_index():
    assert index_power([1, 2, 3, 4, 5], 10) == -1
    assert index_power([10, 20, 30], 5) == -1

def test_single_element_array():
    assert index_power([5], 0) == 1
    assert index_power([10], 1) == -1

def test_power_of_zero():
    assert index_power([0, 1, 2], 0) == 1
    assert index_power([0, 1, 2], 1) == 1