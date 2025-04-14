def chunking_by(numbers, chunk):
    new_list = []
    if not isinstance(chunk, int):
        return "invalid size"
    elif chunk <= 0:
        return []

    for i in range(0, len(numbers), chunk):
        chunks = numbers[i:i + chunk]
        new_list.append(chunks)
    return new_list

call = chunking_by([1,2,3,4,5,6,7], 3)
print(call)