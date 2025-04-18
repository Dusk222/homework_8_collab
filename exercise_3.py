def remove_all_after(numbers, n):
    if not numbers:
        return numbers
    
    if n in numbers:
        index = numbers.index(n)
        return numbers[:index + 1]
    else:
        return numbers
    
print(remove_all_after([1, 2, 3, 4, 5], 3))
print(remove_all_after([1, 1, 2, 2, 3, 3], 2))