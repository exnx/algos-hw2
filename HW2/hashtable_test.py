# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

for (name, HashTable) in [("linear probing", HashTableProbing), ("chaining", HashTableChaining)]:
    table = HashTable(6, 0.75)
    table.insert("apple", "apple")
    table.insert("ball", "apple")
    table.insert("tall", "apple")
    table.insert("poll", "apple")
    table.insert("boll", "pple")
    #table.insert("fall", "apple")
    if table.get("boll") != "pple":
        print("%s hash table did not return example value"%name)
    table.remove("apple")
    #if table.get("ball") != "apple":
    #   print("%s hash table did not return example value"%name)
    #print (table.size())
    if table.size() != 4:
        print("%s hash table had non-zero size"%name)