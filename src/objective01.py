

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
    ### 01:07:11