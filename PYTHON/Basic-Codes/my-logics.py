

from collections import *

st = input('Enter a string. : ')

if st :
    print(st[0].upper() + st[1::])

o/t :
Enter a string. : hello
Hello



st = input('Enter a string. : ')

# Use .title() to capitalize the first letter of each word
output = st.title()

print(output)

Enter a string. : hello bro
Hello Bro
