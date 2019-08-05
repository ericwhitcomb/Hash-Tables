

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):                                                                                                                     
    hash = 5381
    for c in string:
        hash = (( hash << 5) + hash) + ord(c)
    return hash % max
    pass


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    while current_pair is not None and current_pair.key != key:
        current_pair = current_pair.next
    
    if current_pair is None:
        pair = LinkedPair(key, value)
        pair.next = hash_table.storage[index]
        hash_table.storage[index] = pair
    else:
        current_pair.value = value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = current_pair.next
    
    if current_pair is None:
        print ("Warning: key " + str(key) + " not found")
    else:
        last_pair.next = current_pair.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # get the index in the hash table
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    while current_pair is not None and current_pair.key != key:
        current_pair = current_pair.next
    
    if current_pair is None:
        return None
    else:
        return current_pair.value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(16)
    hash_table_insert(ht, "A", "Value for A")
    hash_table_insert(ht, "Q", "Value for Q")
    print(hash_table_retrieve(ht, "A"))
    print(hash_table_retrieve(ht, "Q"))
    hash_table_remove(ht, "A")
    print(hash_table_retrieve(ht, "A"))
    print(hash_table_retrieve(ht, "Q"))

    # ht = HashTable(2)

    # hash_table_insert(ht, "line_1", "Tiny hash table")
    # hash_table_insert(ht, "line_2", "Filled beyond capacity")
    # hash_table_insert(ht, "line_3", "Linked list saves the day!")

    # print(hash_table_retrieve(ht, "line_1"))
    # print(hash_table_retrieve(ht, "line_2"))
    # print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
