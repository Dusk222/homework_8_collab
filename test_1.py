from exercise_1 import replace_last 

def test_replace_last_multiple_items():
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([10, 20, 30]) == [30, 10, 20]

def test_replace_last_single_item():
    assert replace_last([1]) == [1]
    assert replace_last([100]) == [100]

def test_replace_last_empty_list():
    assert replace_last([]) == []

def test_replace_last_edge_cases():
    assert replace_last([5, 6]) == [6, 5]
    assert replace_last(['a', 'b', 'c']) == ['c', 'a', 'b']
    assert replace_last([True, False]) == [False, True]

def test_replace_last_original_unchanged():
    original = [1, 2, 3]
    replaced = replace_last(original)
    assert original == [1, 2, 3]
    assert replaced == [3, 1, 2]