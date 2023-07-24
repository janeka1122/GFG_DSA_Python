# Find the sum of digits of a number using recursion

def sum(n):
    if n<10:
        return n
    return sum(n//10) + n%10

    
    

# (sum(253))
print("The sum of digits of number is: ",sum(-123.4))
#print(253%10)
#print(253//10)
