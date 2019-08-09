#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    hash_table_insert(ht, weights[0], 0)
    index = 1

    while index < length: 
        hash_table_insert(ht, weights[index], index)
        target = limit - weights[index]
        retrieved = hash_table_retrieve(ht, target)
        
        if retrieved:
            if index == 1:
                return (index, 0)                
            elif retrieved > index:
                return (retrieved, index)           
            else:
                return (index, retrieved)   
        index += 1
        
    return None



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
