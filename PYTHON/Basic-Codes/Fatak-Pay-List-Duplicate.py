

A = [1,4,2,4,7,3,8,9,7,5]

check = []

for i in A:
    if i not in check:
        check.append(i)
        
print(check)    #  [1, 4, 2, 7, 3, 8, 9, 5]      





BOTH WORKING SAME



A = [1,2,3,2,3,2,4,6,4,7,1]
B = []

for i in A:
    if i not in B:
        B.append(i)
print(B)

#  [1, 2, 3, 4, 6, 7]
