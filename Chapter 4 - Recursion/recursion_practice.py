def fun(n):
    if n==0:
        return 
    print(n)
    fun(n-1)
    print(n)

#print(3)

def fun2(m):
    if m==0:
        return
    fun2(m-1)
    print(m)
    fun2(m-1)

print('The second function has output like this: ',fun2(3))
print("-------------------------------------------------------------------")

# Functions returns log of number
def fun3(o):
    if o<=1:
        return 0
    else:
        return 1+fun3(o/2) 

print("The 3rd function has an output like this: ", fun3(32))

print("---------------------------------------------------------")

# Prints binary output of a number
def fun4(p):
    if p==0:
        return 
    fun4(p//2)
    print(p%2)

print(fun4(16))

# Priting 1 to n using recursion

def numbers(a):
    if a==0:
        return 0
    numbers(a-1)
    print(a,end="-")

print("The printed numbers is: ",numbers(8))

