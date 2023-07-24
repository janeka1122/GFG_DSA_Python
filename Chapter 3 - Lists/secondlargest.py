# Multiple Traversing of list (2 for loops)

def secondlargest(arr):
    max = arr[0]
    smax = -1
    for i in arr:
        if i>max:
            #smax = max
            max = i 
        
    for j in arr:
        if j>smax and j!=max:
            smax = j
        
    return smax

# Single Traversing of list (1 for loop)
def secondlargest_shortcut(arr):
    lar = arr[1]
    slar = arr[0]

    # Corner Case
    if len(arr)<=1:
        return slar

    for i in range(2,len(arr)):
        if arr[i]>lar:
            slar = lar
            lar = arr[i]
        elif arr[i]<lar and arr[i]>slar:
            slar = arr[i]
        else:
            continue

    return slar

print(secondlargest([-0.1,0,-10,5,10,20,12,10,20]))
print(secondlargest_shortcut([-0.1,0,-10,5,10,20,12,10,20]))