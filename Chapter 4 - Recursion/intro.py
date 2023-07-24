# This module introduces to recursion

# Function is called recursive if the function calls itself

# Caller finishes execution when the called function finishes

def fun1():
    print("fun1 called")

def fun2():
    print("Before fun1")
    fun1()
    print("after fun1")

print("Before fun2")
fun2()
print("After fun2")

# A function is called recursive if the function calls itself directly or indirectly.
# There are 2 types of recursion -
# 1. Direct Recursion
'''
def fun():
    print("YAY!")
    fun()
    # Function calls itself directly
'''
# 2. Indirect recursion
'''
def fun():
    fun2()
def fun2():
    fun()
    # Function is called by a 2nd function
'''

# Simple Recursion Program

def fun():
    print("GFG")
    fun()

fun()

# Never ending loop/function
'''
Since there is a limit on the number of calls in python. That limit is execedded after a certain amount of time
and that is the cause of the error "maximum recursion depth exceeded while calling a Python Object".
The reason for having this error is because when we have a recursive fucntion, it will keep on calling itself
which consumes memory. 

This concept comes from "function call stack" which is used for managing the function call. A stack is used because
function calling happens in a 'last in first out' manner. 
'''

# Writing a program to that takes user input to run a program inputted number of times

def run(x):
    print("GFG")
    x -= 1
    if x<1:
        return
    else:
        run(x)

x = int(input("Please enter the number of times you want to run the program: "))
run(x)

# For recursive program we have to reduce the program into smaller problems
# There are some cases where the problem cannot be divided further and such cases need to be handled explicitly
# Such cases are called base cases
# Base Cases are important because they help handle -
# 1. Exceptions
# 2. Stop the program when such cases are realized.


