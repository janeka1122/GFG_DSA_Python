# This is a standard Problem
# Task - Find the average of elements in a list

def average(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    avg = sum/len(arr)
    return avg

arr = [1,2,3]
print(average(arr))

# Seperating Even and Odd
# Segregration is a very standard problem

def segregation(l):
    even_l = []
    odd_l = []
    for i in l:
        if i%2==0:
            even_l.append(i)
        else:
            odd_l.append(i)
    segregated_list = []
    segregated_list.append(even_l)
    segregated_list.append(odd_l)

    return even_l,odd_l               # The arrays become packed into a tuple

l = [10,41,29,14,80]
print(segregation(l))

# Getting smaller Elements
# Function should return all elements that are smaller than a given element

def find_greater_than(arr,x):
    smaller_than_list = []
    for i in arr:
        if i<x:
            smaller_than_list.append(i)
    return smaller_than_list

arr = [8,100,20,40,3,7]
x = 7   # Find all elements that are smaller than the given element
print("The list of elements that are bigger than",x," is: ",find_greater_than(arr,x))

