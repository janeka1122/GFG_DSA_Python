# Slicing a list

l = [1,2,3,4,5]

# Syntax = list/tuple/string[start_index:stop_index:interval]
# Slicing of 1 datatype returns that same data type

# Using slicing to reverse a list

print("The reverse of the list is: ",l[::-1])
print("The complete list is: ",l[:])

l1 = [10,20,30]
l2 = l1[:] # This is different list from l1

t1 = (10,20,30)  #Defining a tuple
t2 = t1[:]
# l1 and l2 are different lists. Since lists are mutable l1 and l2 might have same value but they have different memory locations

s1 = "Chinmay" # Defining a String
s2 = s1[:]

print(l2 in l1)
print (t2 in t1)
print(s2 in s1)

