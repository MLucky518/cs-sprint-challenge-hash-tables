

def get_indices_of_item_weights(weights, length, limit):
    table = dict()
    for i in range(0, length):
        current = weights[i]
        total = (limit - current)
        if total in table:
            index = table[total]
            return (i, index)
        else:
            table[current] = i
    return None

        # table[weights[i]] = i
        # if limit - weights[i] in table:
        #     if table[weights[i]] == table[limit-weights[i]]:
        #         if table[weights[i]] > table[limit-weights[i]]:
        #             return(table[weights[i]]+1, table[limit-weights[i]])
        #         else:
        #             return(table[limit-weights[i]]+1, table[weights[i]])
        #     else:
        #         if table[weights[i]] > table[limit-weights[i]]:
        #             return(table[weights[i]], table[limit-weights[i]])
        #         else:
        #             return(table[limit-weights[i]], table[weights[i]])



      

lst = [4, 4]

print(get_indices_of_item_weights(lst, 7, 8))




