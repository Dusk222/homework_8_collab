def remove_all_after(numbers, n):
    if not numbers:
        
        return numbers
    
    if n in numbers:

        index = numbers.index(n)
        return numbers[:index + 1]
    
    else:
        return numbers