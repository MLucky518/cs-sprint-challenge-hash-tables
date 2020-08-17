# Your code here



def finder(files, queries):
    table = dict()
    ans = []

    for el in files:
        if el not in table:
            table[el] = el.split("/")
        else:
            continue

    for key,val in table.items():
        for el in queries:
            if el == val[-1]:
                ans.append(key)
    return ans


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
