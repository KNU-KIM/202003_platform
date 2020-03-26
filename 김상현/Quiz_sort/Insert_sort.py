def Insert(lst):
    result = [lst[0]]
    for i in range(1, len(lst)):
        for j in range(len(result)):
            if lst[i] < result[len(result)-j-1]:
                if j == len(result)-1:
                    result.insert(0, lst[i])
            elif lst[i] >= result[len(result)-j-1]:
                result.insert(len(result)-j, lst[i])
                break

    return result


print(Insert([9, 4, 3, 1, 12]))

