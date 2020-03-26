def selection(lst):
    for i in range(len(lst)):
        j=i
        min_index = i
        while j < len(lst):
            if lst[j] <= lst[min_index]:
                min_index = j
            j += 1
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


print(selection([9, 4, 3, 1, 12]))