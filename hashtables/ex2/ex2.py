#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    current_destination = None

    #There needs to be one algorithm for the first ticket and one for the other tickets, this is the first ticket algorithm
    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        if tickets[i].source == 'NONE':
            current_destination = tickets[i].destination
            route[0] = tickets[i].destination

    #This is the algorithm for the rest of the tickets
    for i in range(1, length):
        next_destination = hash_table_retrieve(hashtable, current_destination)
        route[i] = next_destination
        current_destination = next_destination

    return route

