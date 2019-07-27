

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
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    # if hash_table.count == hash_table.capacity:
    #     hash_table = hash_table_resize(hash_table)

    print(f'The Insert, is in Index {index} has {key}')

    while current_pair is not None and current_pair.key != key:
        current_pair = current_pair.next

    if current_pair is None:
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair

        if new_pair.next is None:
            hash_table.count += 1
    else:
        current_pair.value = value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
   # same here we want to get the hashed key
    index = hash(key,  hash_table.capacity)
    current_pair = hash_table.storage[index]
    prev_pair = None
    # Take the index of the storage and verify if its set to None
    if current_pair is not None:
       # if it not none then check if the key is = to the storage key
        while current_pair is not None and current_pair.key != key:
            prev_pair = current_pair
            current_pair = current_pair.next

        if prev_pair == None and current_pair.key == key:
            hash_table.storage[index] = None
            hash_table.count -= 1
        elif current_pair is None:
            print(f'Error! {key} not found')
        else:
            prev_pair.next = None

    else:
        print(f'Error! {key} not found')

# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    print("I am Running")
    # same here we want to get the hashed key
    index = hash(key,  hash_table.capacity)
    current_pair = hash_table.storage[index]
    print(f'The Retrieve, is in Index {index} has {key}')
    # Take the index of the storage and verify if its set to None
    if current_pair is not None:

        while current_pair is not None and current_pair.key != key:
            current_pair = current_pair.next
        if current_pair == None:
            print(f'Error {key} not found')
        else:
            return current_pair.value

    else:
        print(f'Error {key} not found')

# '''
# Fill this in
# '''


def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)

    for x in range(hash_table.count):
        # new_hash_table.storage[index] = hash_table.storage[index]
        current_pair = hash_table.storage[x]
        while current_pair is not None:
            hash_table_insert(
                new_hash_table, current_pair.key, current_pair.value)
            current_pair = current_pair.next

    return new_hash_table

    new_hash = HashTable(hash_table.capacity * 2)
    for i in range(hash_table.count):
        print(hash_table.storage[i].key)
        temp = hash_table.storage[i]
        index = hash(temp.key, new_hash.capacity)
        new_hash.storage[index] = temp

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
