from exercise_5 import reverse_ascending

def test_reverse_ascending():
    # Test Case 1: Example from the problem statement
    input1 = [1, 2, 3, 2, 4, 5, 6, 3]
    expected_output1 = [3, 2, 1, 6, 5, 4, 2, 3]
    assert reverse_ascending(input1) == expected_output1, f"Test Case 1 Failed: Expected {expected_output1}, got {reverse_ascending(input1)}"

    # Test Case 2: Entire list is strictly descending
    input2 = [5, 4, 3, 2, 1]
    expected_output2 = [5, 4, 3, 2, 1]
    assert reverse_ascending(input2) == expected_output2, f"Test Case 2 Failed: Expected {expected_output2}, got {reverse_ascending(input2)}"

    # Test Case 3: All elements are the same
    input3 = [1, 1, 1]
    expected_output3 = [1, 1, 1]
    assert reverse_ascending(input3) == expected_output3, f"Test Case 3 Failed: Expected {expected_output3}, got {reverse_ascending(input3)}"

    # Test Case 4: Empty list
    input4 = []
    expected_output4 = []
    assert reverse_ascending(input4) == expected_output4, f"Test Case 4 Failed: Expected {expected_output4}, got {reverse_ascending(input4)}"

    # Test Case 5: Single element
    input5 = [7]
    expected_output5 = [7]
    assert reverse_ascending(input5) == expected_output5, f"Test Case 5 Failed: Expected {expected_output5}, got {reverse_ascending(input5)}"

    # Test Case 6: Mixed sequence with multiple ascending subsequences
    input6 = [1, 3, 2, 4, 6, 5, 3, 7, 8]
    expected_output6 = [3, 1, 6, 4, 2, 5, 8, 7, 3]
    assert reverse_ascending(input6) == expected_output6, f"Test Case 6 Failed: Expected {expected_output6}, got {reverse_ascending(input6)}"

    print("All test cases passed!")

# Run the test cases
test_reverse_ascending()
