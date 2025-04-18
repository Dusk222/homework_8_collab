def reverse_ascending(items):
    result = []

    if len(items) == 0:
        return result

    sublist = [items[0]]

    i = 1
    while i < len(items):
        if items[i] > items[i - 1]:
            sublist.append(items[i])
        else:
            # reverse the sublist manually
            reversed_sublist = []
            j = len(sublist) - 1
            while j >= 0:
                reversed_sublist.append(sublist[j])
                j = j - 1
            result += reversed_sublist
            sublist = [items[i]]
        i = i + 1

    # handle last sublist
    reversed_sublist = []
    j = len(sublist) - 1
    while j >= 0:
        reversed_sublist.append(sublist[j])
        j = j - 1
    result += reversed_sublist

    return result
