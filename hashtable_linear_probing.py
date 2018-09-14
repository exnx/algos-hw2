# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# An implementation of a hash table that uses probing to handle collisions.
class HashTable:
    def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
        if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
            raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
        self.array_size = initial_size
        self.load_factor = load_factor
        self.item_count = 0
        self.array = FixedSizeArray(initial_size)

    # Inserts the `(key, value)` pair into the hash table, overwriting any value
    # previously associated with `key`.
    # Note: Neither `key` nor `value` may be None (an exception will be raised)
    def insert(self, key, value):
        # check loading factor, if over, resize
        if self.load_factor <= self.item_count / self.array_size:
            self._resize_array()
        
        # hash the key  
        hash_ind = cs5112_hash1(key) % self.array_size

        # loop until an empty index found
        while self.array.get(hash_ind) != None and self.array.get(hash_ind) != 'removed':
            
            # if you hash and get back the key, then update the value
            if self.array.get(hash_ind)[0] == key:  # check the first entry in the tuple
                self.array.set(hash_ind, (key, value))
                
            # check hash of next index
            hash_ind = (hash_ind + 1) % self.array_size
            
        # loop broken, found None elem, so set it    
        self.array.set(hash_ind, (key, value))
        self.item_count += 1

    # Returns the value associated with `key` in the hash table, or None if no
    # such value is found.
    # Note: `key` may not be None (an exception will be raised)
    def get(self, key):

        # hash the key  
        hash_ind = cs5112_hash1(key) % self.array_size

        # loop through non empty cells
        while self.array.get(hash_ind) != None:

            elem = self.array.get(hash_ind) # get the elem

            # if the elem is not removed, check it's key, value
            # else, just continue searching
            if elem != 'removed':

                # if you hash and get back the key
                if elem[0] == key:  # check key in tuple
                    return elem[1]. # second entry is value

            # get hash of next index
            hash_ind = (hash_ind + 1) % self.array_size            

        # if looped through and no match, return None
        return None

    # Removes the `(key, value)` pair matching the given `key` from the map, if it
    # exists. If such a pair exists in the map, the return value will be the value
    # that was removed. If no such value exists, the method will return None.
    # Note: `key` may not be None (an exception will be raised)
    def remove(self, key):

        # hash the key  
        hash_ind = cs5112_hash1(key) % self.array_size

        # loop through non empty cells
        while self.array.get(hash_ind) != None:

            elem = self.array.get(hash_ind)

            # if you hash and get back the key
            if elem[0] == key:  # check the first entry in the tuple
                self.array.set(hash_ind, 'removed')
                self.item_count -= 1  # decrement
                return elem

            # get hash of next index
            hash_ind = (hash_ind + 1) % self.array_size          

        # if looped through and no match, return None
        return None

    # Returns the number of elements in the hash table.
    def size(self):
        return self.item_count

    # Internal helper function for resizing the hash table's array once the ratio
    # of stored mappings to array size exceeds the specified load factor.
    def _resize_array(self):
        
        # make new array
        new_array = FixedSizeArray(self.array_size * 2)
        
        # loop through old array
        for ind in range(self.array_size):
            # if entry is not empty, reinsert it into new array
            if self.array.get(ind) and self.array.get(ind) != 'removed':
                key, value = self.array.get(ind)  # retrieve the elem
                self.insert(key, value)  # reinsert the elem in the new array

        # set orig array to the new array
        self.array = new_array
        self.array_size *= 2

    # Internal helper function for accessing the array underlying the hash table.
    def _get_array(self):
        # DO NOT EDIT THIS METHOD
        return self.array
