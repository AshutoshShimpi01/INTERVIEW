
-- STRING Problem Infos     ( aaabbc ---> a3b2c1 )

from collections import *

st = input('Enter a String : ')
output = ''

counts = Counter(st)

for char, count in counts.items():
    output += char + str(count)
    
print(output)

Enter a String : aaabbc
a3b2c1

------

from collections import Counter

st = input('Enter a string. : ')
output = ''

counts = Counter(st)

for char, count in counts.items():

    output += (char * count) + str(count)
    
print(output). 

# aaa3bb2c1

-----------------------------------------------


-- STRING Problem Impets     ( apple is red ---> Apple Is Red )

st = input('Enter a String : ')

result = ' '.join([
    
    word[0].upper() + word[1::].lower()
    for word in st.split() if word
    
    ])
    
print(result)

Enter a String : apple is red
Apple Is Red


-----------------------------------------------


-- REMOVE DUPLICATES inside List

from collections import *


A = [1,3,2,4,1,5,3,2,5]

output = []

for i in A:
    if i not in output:
        output.append(i)
        
print(output)

#. [1, 3, 2, 4, 5]



-----------------------------------------------


# The mobile number string
mobile_number = "+91 7030210200"

# Use .replace() to substitute "+91 " with an empty string ""
cleaned_number = mobile_number.replace("+91 ", "")

print(cleaned_number) 
# Output: 7030210200

