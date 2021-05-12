def merge_two_sorted_array(array1, array2):
    if array1 is None:
        return array2
    if array2 is None:
        return array1

    result = []
    pos1 = 0
    pos2 = 0
    l1 = len(array1)
    l2 = len(array2)
    while True:
        if pos1 >= l1:
            for i in range(pos2, l2):
                result.append(array2[i])
            break

        if pos2 >= l2:
            for i in range(pos1, l1):
                result.append(array1[i])
            break

        if array1[pos1] <= array2[pos2]:
            result.append(array1[pos1])
            pos1 = pos1 + 1
        else:
            result.append(array2[pos2])
            pos2 = pos2 + 1

    return result


def main():
    print(str(merge_two_sorted_array([5, 6, 12], [2, 3, 8])))


main()

