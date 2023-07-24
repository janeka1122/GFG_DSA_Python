list = [1,10,10,10,20,20,40]
search = int(input("Enter the number to be searched: "))
for i in list:
    if i==search:
        print(list.index(search))
        break

