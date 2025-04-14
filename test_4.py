from exercise_4 import chunking_by

def test_chunking_by():
    # Test Case 1: Normal case with chunk size 3
    assert chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]

    # Test Case 2: Chunk size 1
    assert chunking_by([3, 4, 5], 1) == [[3], [4], [5]]

    # Test Case 3: Empty list should return empty list
    assert chunking_by([], 3) == []

    # Test Case 4: Chunk size larger than list length
    assert chunking_by([1, 2], 5) == [[1, 2]]

    # Test Case 5: Chunk size equal to list length
    assert chunking_by([1, 2, 3, 4], 4) == [[1, 2, 3, 4]]

    # Test Case 6: Chunk size 0 (edge case, but as per problem statement, last chunk can be smaller, but size is positive)
    assert chunking_by([1, 2, 3], 0) == []

    print("All test cases passed!")

if __name__ == "__main__":
    test_chunking_by()