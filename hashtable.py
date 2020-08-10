class HashTable(object):

    def __init__(self, size):

        # Set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        # Note, we'll only use integer keys for ease of use with the Hash Function

        # Get the hash value
        hash_value = self.hash_function(key, len(self.slots))

        # If Slot is Empty
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:

            # If key already exists, replace old value
            if self.slots[hash_value] == key:
                self.data[hash_value] = data

                # Otherwise, find the next available slot
            else:

                next_slot = self.rehash(hash_value, len(self.slots))

                # Get to the next slot
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                # Set new key, if NONE
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

                # Otherwise replace old value
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        # Remainder Method
        return key % size

    def rehash(self, old_hash, size):
        # For finding next possible positions
        return (old_hash + 1) % size

    def get(self, key):

        # Getting items given a key

        # Set up variables for our search
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.slots[position] is not None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    # Special Methods for use with Python indexing
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable(5)
h[1] = 'One'
h[2] = 'Two'
h[3] = 'Three'

print(h[1])
print(h[2])
print(h[3])