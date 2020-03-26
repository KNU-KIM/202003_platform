def Merge(lst):
    if len(lst) <= 1:
        return lst

    g1 = Merge(lst[:len(lst) // 2])
    g2 = Merge(lst[len(lst) // 2:])
    result = []
    while len(g1) != 0 and len(g2) != 0:
        if g1[0] <= g2[0]:
            result.append(g1[0])
            g1.remove(g1[0])
        else:
            result.append(g2[0])
            g2.remove(g2[0])
    result += g1 + g2

    return result


list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(Merge(list))
