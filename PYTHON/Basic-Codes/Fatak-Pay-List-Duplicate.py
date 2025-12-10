

A = [1,4,2,4,7,3,8,9,7,5]

check = []

item = set()

for i in A:
    if i not in check:
        check.append(i)
        item.add(i)
        
print(check)    #  [1, 4, 2, 7, 3, 8, 9, 5]

