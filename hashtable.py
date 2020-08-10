class HashTable(object):

    def __init__(self, size):

        # set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        # NOte, we'll only use integer keys for easse of use with the Hash Function

        # Get the has value
        hashvalue = self.hashfunction(key, len(self.slots))

        # if slot is EMPTY
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            # IF KEY ALREADY EXIXTS, REPLACE OLD VALUE
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            # Otherwise, find the next available slot
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                # Get to the next slot
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                # set new key, if None
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                # Otherwise replace old value
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        # the actual hash function
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
