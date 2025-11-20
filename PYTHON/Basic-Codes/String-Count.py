from collections import *

st = str(input('Enter a string : '))

result = ' '.join([
    word[0].upper() + word[1::].lower()
    for word in st.split() if word
    ])
    
print(st)
print(result)

o/t :
Enter a string : i am ashutosh
I Am Ashutosh

-------------------------

st = input("Enter a string: ")

# Capitalize only the first character of the string
result = st.capitalize()

print(st)
print(result)

o/t:
Enter a string: i am Ashutosh
I am ashutosh
----------------------------

st = input("Enter a string: ")

result = st[0].upper() + st[1:]
print(result)

o/t:
Enter a string: i am ashu
I am ashu

-----------------------------


from collections import *
st = input('Enter string : ')
ch = st.split()
newString = ch[0].upper() + ' '+ ' '.join(ch[1::]).lower()
print(newString)

output:
Enter string : i am ashu
I am ashu
