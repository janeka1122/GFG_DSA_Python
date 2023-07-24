# List is dynamic sized.
'''import numpy as np

f = 25
bi = np.arange(-f, f + 5, 5)
beta = bi.tolist()
print(bi)
print(beta)'''

l = [10,20,30,40,50]
l.append(60)
print(l)
l.insert(0,70)   # Syntax list_name.insert(index, value)
print(l)
print(l.pop(1))  # Removes the value at the given index
print(l)
del l[1],l[4]
print(l)

# Every member list is referenced

'''
Internal Working of list in python. 
In Arrays everything is stored in continuous location. 
Different types of itmes are allowed in Python
Every element in the array is reference. 

The references must be stored in continous locations, however the data may or may not be stored in continous locations. 

List container is a dynamically sized array. It allows us to dynamically insert and delete items. Hence it might allocate extra memory as well. 
Hence insertions can happen faster. 

What are the advanges of list and array. 
1. Random Access - Since items are indexed any value can be called at given point the program. 
                   Therefore if one address is known the address of all items in the array are known. 
                   Set and Dictionaries do not have random access. 
2. Cache Friendlyness - Locality of reference. CPU when they fetch an item they store that data in cache memory. 
                        Continuous refernces ensure that there is a less cache mess. 
                        Such functionality is not there in all the data structures like deck container which are based on linked list (doubly linked lists) 

Disadvantages 
1. Insertions, deletion, and search are slower than other data types. Set is unordered. They are much faster. 
   Insertion and deletion take linear time. This is because all the 
   Search is also linear time if the list is not sorted.  


DYNAMIC SIZING IN LISTS: 

There in an underlying array data structure which stores references of python. When the list becomes bigger more space is alotted.

'''

# Time complexity of append operation
# Item is only appended at the end.
# Same for removing the last item.
# Shirking of the list is also random time





