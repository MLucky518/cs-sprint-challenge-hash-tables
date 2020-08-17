def has_negatives(a):
    table = dict()
    ans = []

    for el in a:

        if abs(el) not in table:
            table[abs(el)] = 1
        else:
            table[abs(el)] += 1

    for key, val in table.items():
        if val > 1:
            ans.append(key)
    return ans

    # Tests do not check for multiple positive duplicates and would break if duplicates were added
    # NEEDS REFACTORING


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
