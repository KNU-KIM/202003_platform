def Quick(lst):
    if len(lst) <= 1:
        return lst

    g1 = []
    g2 = []
    for i in range(len(lst) - 1):
        if lst[i] >= lst[-1]:
            g2.append(lst[i])
        else:
            g1.append(lst[i])

    result = Quick(g1) + [lst[-1]] + Quick(g2)

    return result


list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(Quick(list))
