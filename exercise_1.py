def replace_last(numbers):
    if len(numbers) <= 1:
        return numbers

    last_item = numbers[-1]

    other_numbers = numbers[:-1]

    return [last_item] + other_numbers

# Testing the function
print(replace_last([2, 3, 4, 1]))
print(replace_last([1, 2, 3, 4]))
print(replace_last([1]))
print(replace_last([]))