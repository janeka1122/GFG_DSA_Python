def fact(m):
    if m==0:
        return 1
    return m*fact(m-1)
print(fact(4))

def fibonnaci_sum(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    return fibonnaci_sum(n-1) + fibonnaci_sum(n-2)

print(fibonnaci_sum(4))