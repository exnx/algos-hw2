# Please see instructions.pdf for the description of this problem.
from __future__ import division
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

    if key==None or value==None:
      raise Exception

    if (self.item_count/self.array_size)>=self.load_factor:
      self._resize_array()
      

    bucket= cs5112_hash1(key) % self.array_size
    new_node=SLLNode((key, value))
    pointer= self.array.get(bucket)

    if not pointer:
      self.array.set(bucket, new_node)
      self.item_count+=1
      return

    else:

      while pointer.get_next():

        if pointer.get_value()[0]== key:
          pointer.set_value=((key, value))
          return
        pointer=pointer.get_next()

      if pointer.get_value()[0]== key:
          pointer.set_value=((key, value))
          return

      else:
        pointer.set_next(new_node)
        self.item_count+=1
        return
      



  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):

    if key== None:
      raise Exception

    bucket= cs5112_hash1(key) % self.array_size

    if not self.array.get(bucket):
      return None

    pointer= self.array.get(bucket)

    while pointer.get_next():

      if pointer.get_value()[0]== key:
        return pointer.get_value()[1]
      pointer=pointer.get_next()

    if pointer.get_value()[0]== key:
      return pointer.get_value()[1]

    else: 
      return None


  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):

    if key== None:
      raise Exception

    bucket= cs5112_hash1(key) % self.array_size

    if not self.array.get(bucket):
      return None

    pointer= self.array.get(bucket)

    if pointer.get_value()[0]== key:
      val= pointer.get_value()[1]
      self.array.set(bucket, pointer.get_next())
      self.item_count-=1
      return val

    while pointer.get_next():

      if pointer.get_next().get_value()[0]== key:
        val= pointer.get_next().get_value()[1]
        pointer.set_next((pointer.get_next().get_next()))
        self.item_count-=1
        return val

      pointer=pointer.get_next()

    return None


    

  # Returns the number of elements in the hash table.
  def size(self):
    # YOUR CODE HERE
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):

    ht= HashTable(self.array_size*2, self.load_factor)
    index=0

    while index<self.array_size:
      
      if not self.array.get(index):
        index+=1

      else:
        pointer= self.array.get(index)

        while pointer!= None:
          key= pointer.get_value()[0]
          value= pointer.get_value()[1]
          ht.insert(key, value)
          pointer = pointer.get_next()
        index+=1

    self.array_size=ht.array_size
    self.array=ht.array

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array
