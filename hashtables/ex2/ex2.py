#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    table = dict()
    answer = [None] * length
    for i in range(length):
        if tickets[i].source not in table:
            table[tickets[i].source] = tickets[i].destination

    answer[0] = table["NONE"]
    for i in range(1,length):
        answer[i] = table[answer[i-1]]

    return answer
