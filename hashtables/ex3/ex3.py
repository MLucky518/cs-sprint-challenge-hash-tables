def intersection(arrays):
    table = dict()
    for lst in arrays:
        for el in lst:
            if el in table:
                table[el] += 1
            else:
                table[el] = 1
    answer = []
    for key,val in table.items():
        if val == len(arrays):
            answer.append(key)

    return answer


if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))
    print(intersection([[2, 4, 7, 3], [98, 53, 2, 67], [12, 32, 2, 3]]))
