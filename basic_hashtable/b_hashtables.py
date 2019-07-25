# '''
# Basic hash table key/value pair
# '''


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        pass


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string):
    hash = 5381

    for i in string:
        hash = (((hash << 5) + hash) + ord(i)) & 0xFFFFFFFF
    return hash
# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''


def hash_table_insert(hash_table, key, value):
    key_hash = hash(key)
    key_value = Pair(key, value)

    # to get the index you need take the has modulus by the size(capcity)
    index = key_hash % hash_table.capacity
    # we want to check if the storage is not None
    if hash_table.storage[index] is not None:
        # If the key matches the key in the storage
        if key == hash_table.storage[index].key:
            # Then we want to know that it's a collision
            print(f'Collision found with {key}')
        else:
            # Otherwise we can take the value and set it to our storage value
            hash_table.storage[index].value = value
    else:
        # if storage is none then set the store to the value pair
        hash_table.storage[index] = key_value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # same here we want to get the hashed key
    key_hash = hash(key)
    # Take the hash key and modulus with size(capacity) to get the index
    index = key_hash % hash_table.capacity
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
    key_hash = hash(key)
    # Take the hash key and modulus with size(capacity) to get the index
    index = key_hash % hash_table.capacity
    # Take the index of the storage and verify if its set to None
    if hash_table.storage[index] is not None:
        # if it not none then check if the key is = to the storage key
        if hash_table.storage[index].key == key:
            # if it is = to storage key return the value in storage
            return hash_table.storage[index].value

    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
