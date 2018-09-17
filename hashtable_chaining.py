# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next(self, node):
     self.next_node = node

    def get_next(self):
        return self.next_node

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# An implementation of a hash table that uses chaining to handle collisions.
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

        # create a new SLL node
        new_node = SLLNode((key, value))  # pass tuple as value
        
        hash_id = cs5112_hash1(key) % self.array_size
        curr_node = self.array.get(hash_id)

        # if hashed array elem is empty, set the elem to the new node
        if not curr_node:
            self.array.set(hash_id, new_node)
            self.item_count += 1
            return  # done, return

        override = False

        # otherwise, loop through linked list until the end
        while curr_node.get_next():  # when the next node is None, you've reached the end

            # if the key in curr node == key passed, override the value
            if curr_node.get_value()[0] == key:
                curr_node.set_value((key, value))
                override = True

            curr_node = curr_node.get_next()

        # if you're not overriding, you're adding the new node to the end
        if not override:
            curr_node.set_next(new_node)
            self.item_count += 1

    # Returns the value associated with `key` in the hash table, or None if no
    # such value is found.
    # Note: `key` may not be None (an exception will be raised)
    def get(self, key):
    
        hash_id = cs5112_hash1(key) % self.array_size
        curr_node = self.array.get(hash_id)

        # if elem is empty, return None right away
        if not curr_node:
            return None

        # loop until the end
        while curr_node:

            node_key, node_value = curr_node.get_value()

            # check if the key in the node is the same as the key passed in
            if key == node_key:  # key in first entry of the tuple
                return node_value
            curr_node = curr_node.get_next()

        return None

    # Removes the `(key, value)` pair matching the given `key` from the map, if it
    # exists. If such a pair exists in the map, the return value will be the value
    # that was removed. If no such value exists, the method will return None.
    # Note: `key` may not be None (an exception will be raised)
    def remove(self, key):
        
        hash_id = cs5112_hash1(key) % self.array_size
        curr_node = self.array.get(hash_id)
        prev_node = None

        # if empty, return None
        if not curr_node:
            return None

        # otherwise, loop until elem is found, and set the prev next node to curr's next node
        while curr_node:

            node_key, node_value = curr_node.get_value()

            if node_key == key:

                # only 1 item, set the elem array to None
                if self.item_count == 1:
                    self.array.set(hash_id, None)
                # otherwise skip the current elem
                else:
                    prev.set_next = curr_node.get_next
            
                self.item_count -= 1

            prev = curr_node
            curr_node = curr_node.get_next()


    # Returns the number of elements in the hash table.
    def size(self):
        return self.item_count

    # Internal helper function for resizing the hash table's array once the ratio
    # of stored mappings to array size exceeds the specified load factor.
    def _resize_array(self):
        # YOUR CODE HERE
        raise NotImplementedError()

    # Internal helper function for accessing the array underlying the hash table.
    def _get_array(self):
        # DO NOT EDIT THIS FUNCTION
        return self.array

ht = HashTable(3, 0.75)
print('array size', ht.array_size)
print('item count', ht.item_count)
ht.insert("fat", "dog")
print('array size', ht.array_size)
print('item count', ht.item_count)
ht.insert("lazy", "cat")
print('array size', ht.array_size)
print('item count', ht.item_count)
ht.insert("dude", "bird")
print('array size', ht.array_size)
print('item count', ht.item_count)

ht.remove('dude')
print('array size', ht.array_size)
print('item count', ht.item_count)
print(ht.get_value('dude'))

# ht.remove('fat')
# print('array size', ht.array_size)
# print('item count', ht.item_count)
