from exercise_3 import remove_all_after


def test_remove_all_after():
    assert remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    
    assert remove_all_after([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
    
    assert remove_all_after([], 1) == []
    
    assert remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]
    
    assert remove_all_after([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

    assert remove_all_after([1, 2, 3, 4, 5], 1) == [1]

    assert remove_all_after([2, 2, 2, 2], 2) == [2]

    assert remove_all_after([2, 2, 2, 2], 3) == [2, 2, 2, 2]

    large_list = list(range(1000))
    assert len(remove_all_after(large_list, 500)) == 501
    
    print("All Test Have Passed.")

test_remove_all_after()