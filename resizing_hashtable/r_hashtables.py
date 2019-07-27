

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
        self.storage = [None] * capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381

    for i in string:
        hash = ((hash << 5) + hash) + ord(i)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_table.count += 1
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    while current_pair is not None and current_pair.key != key:
        current_pair = current_pair.next
    if current_pair is None:
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair
    else:
        current_pair.value = value
    # hash_table.count += 1
# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
   # same here we want to get the hashed key
    index = hash(key,  hash_table.capacity)
    # Take the hash key and modulus with size(capacity) to get the index

    # Take the index of the storage and verify if its set to None
    if hash_table.storage[index] is not None:
        # if the hash storage is not none. Then set it to None
        hash_table.storage[index] = None
    else:
        # If it is none then we can send a message to Say There is not a key in the table
        print(f'{key} is not in the hash table. So it can not be removed')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
       # same here we want to get the hashed key
    index = hash(key,  hash_table.capacity)

    if hash_table.storage[index] is None:
        return None

    return hash_table.storage[index].value
# '''
# Fill this in
# '''


def hash_table_resize(hash_table):
    new_hash = HashTable(hash_table.capacity * 2)

    for i in range(hash_table.capacity):
        print(hash_table.storage[i].key)
        new_hash.storage[i] = hash_table.storage[i]
    return new_hash


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
