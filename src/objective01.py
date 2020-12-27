

arr = [12, 23, 45, 1, 4, 7, 67]

# Lookup
def Lookup_item_by_index(array, index):
    """
    To look up an item by index in an array is constant time O(1)
    """
    return array[index]


# Append
def add_item_to_end(array, item):
    """
    Adding an item to an array is constant time O(1)
    """
    array.append(item)

# Insert
def insert_item_at_index(array, index):
    """
    Unless you are inserting an item at the end of the list,
    items must be shifting over to make room for the new information you add to the static array.
    It's like if you had a chain of people stretched out, holding hands, in a line.
    the first person in the line is butted right up against a wall,
    and there is no room on one side of him. If someone wanted to join the end of the line.
    the people already in the line wouldn't have to do anything (O(1)). However,
    if you wanted to join the beginning of the line, every single person would have to move over
    (away from the wall) (O(n))
    """
    
    ### 01:07:11