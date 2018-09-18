# Please see instructions.pdf for the description of this problem.
from __future__ import division
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

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
    # YOUR CODE HERE
    if key==None or value==None:
      raise Exception
  
    if (self.item_count/self.array_size)>=self.load_factor:
      self._resize_array()
      #print("resizing")

    index= cs5112_hash1(key)%self.array_size

    if not self.array.get(index):
      self.array.set(index, (key, value))
      self.item_count+=1
      return

    elif self.array.get(index)!='deleted' and self.array.get(index)[0]==key:
      self.array.set(index, (key, value))
      return

    else:
      while self.array.get(index)!='deleted' and self.array.get(index)!= None:

        if self.array.get(index)[0]==key:
          self.array.set(index, (key, value))
          return
        if index== self.array_size-1:
          index=0;
        index+=1;

      self.array.set(index, (key, value))
      self.item_count+=1
      return

      

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    # YOUR CODE HERE
    if key==None:
      raise Exception

    index= cs5112_hash1(key)%self.array_size

    if not self.array.get(index):
      return None

    while self.array.get(index)!= None:

      if self.array.get(index)!='deleted' and self.array.get(index)[0]==key:
        return self.array.get(index)[1]         
      if index== self.array_size-1:
        index=0;
      index+=1;

    return None



  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    # YOUR CODE HERE
    if key==None:
      raise Exception

    index= cs5112_hash1(key)%self.array_size

    if not self.array.get(index):
      return None

    while self.array.get(index)!= None:
      if self.array.get(index)[0]==key:
        val= self.array.get(index)[1]  
        self.array.set(index, 'deleted')
        self.item_count-=1
        return val

      if index== self.array_size-1:
        index=0;
      index+=1;

    return None


  # Returns the number of elements in the hash table.
  def size(self):
    # YOUR CODE HERE
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    # YOUR CODE HERE
    
    ht= HashTable(self.array_size*2, self.load_factor)

    index=0
    while index<self.array_size:

      if self.array.get(index) is None:
        index+=1
        
      else:
        if self.array.get(index)!='deleted':
          key=self.array.get(index)[0]
          value= self.array.get(index)[1]
          ht.insert(key,value)
          index+=1

    self.array_size=ht.array_size
    self.array=ht.array


  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array
