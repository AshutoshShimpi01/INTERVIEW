from collections import *

st = str(input('Enter a string : '))

result = ' '.join([
    word[0].upper() + word[1::].lower()
    for word in st.split() if word
    ])
    
print(st)
print(result)


st = input("Enter a string: ")

# Capitalize only the first character of the string
result = st.capitalize()

print(st)
print(result)


