
Here are 20 foundational Python string coding questions, ranging from beginner to intermediate, complete with answers and explanations.

## 🐍 Basic String Manipulation

### 1\. Reverse a String

**Q:** Write a function to reverse a given string.
**A:**

```python
def reverse_string(s):
    return s[::-1]

# Example:
# print(reverse_string("Python"))  # Output: nohtyP
```

### 2\. Check for Palindrome

**Q:** Write a function to check if a given string is a palindrome (reads the same forwards and backwards).
**A:**

```python
def is_palindrome(s):
    # Normalize by converting to lowercase and removing spaces/punctuation if needed
    normalized_s = "".join(filter(str.isalnum, s.lower()))
    return normalized_s == normalized_s[::-1]

# Example:
# print(is_palindrome("madam"))    # Output: True
# print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True
```

### 3\. Count Vowels

**Q:** Write a function to count the number of vowels (a, e, i, o, u) in a string.
**A:**

```python
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# Example:
# print(count_vowels("Hello World"))  # Output: 3
```

### 4\. Remove Whitespace

**Q:** Write a function that removes all whitespace characters (spaces, tabs, newlines) from a string.
**A:**

```python
import re
def remove_whitespace(s):
    return "".join(s.split())
    # Alternative using regex: return re.sub(r'\s+', '', s)

# Example:
# print(remove_whitespace("a b\tc\nd")) # Output: abcd
```

### 5\. Check for Substring

**Q:** Check if a given substring exists within a larger string.
**A:**

```python
def contains_substring(main_string, sub_string):
    return sub_string in main_string
    # Alternative using find: return main_string.find(sub_string) != -1

# Example:
# print(contains_substring("applepie", "pie"))  # Output: True
```

-----

## 🔢 Character and Word Counting

### 6\. Count Character Occurrences

**Q:** Write a function to count the total occurrences of a specific character in a string.
**A:**

```python
def count_char(s, char):
    return s.count(char)

# Example:
# print(count_char("banana", 'a'))  # Output: 3
```

### 7\. Find First Non-Repeating Character

**Q:** Find the first character in a string that does not repeat.
**A:**

```python
from collections import Counter
def first_non_repeating_char(s):
    char_counts = Counter(s)
    for char in s:
        if char_counts[char] == 1:
            return char
    return None # Return None if all characters repeat

# Example:
# print(first_non_repeating_char("swiss")) # Output: w
```

### 8\. Count Words

**Q:** Count the number of words in a string.
**A:**

```python
def count_words(s):
    # Splits by whitespace and counts non-empty parts
    return len(s.split())

# Example:
# print(count_words("Python is fun")) # Output: 3
```

### 9\. Most Frequent Character

**Q:** Find the character that appears most frequently in a string.
**A:**

```python
from collections import Counter
def most_frequent_char(s):
    if not s:
        return None
    return Counter(s).most_common(1)[0][0]

# Example:
# print(most_frequent_char("programming")) # Output: r
```

### 10\. Check Anagrams

**Q:** Write a function to check if two strings are anagrams of each other (contain the same characters with the same frequencies).
**A:**

```python
def are_anagrams(s1, s2):
    # Normalize and compare sorted strings
    return sorted(s1.lower()) == sorted(s2.lower())
    # Alternative: return Counter(s1.lower()) == Counter(s2.lower())

# Example:
# print(are_anagrams("listen", "silent")) # Output: True
```

-----

## 🔀 Transformations and Advanced

### 11\. Capitalize First Letter of Each Word

**Q:** Capitalize the first letter of every word in a sentence.
**A:**

```python
def title_case(s):
    return s.title()

# Example:
# print(title_case("hello world python")) # Output: Hello World Python
```

### 12\. Swap Case

**Q:** Convert all lowercase letters to uppercase and vice versa in a string.
**A:**

```python
def swap_case(s):
    return s.swapcase()

# Example:
# print(swap_case("pYtHoN")) # Output: PyThOn
```

### 13\. Replace Substring

**Q:** Replace all occurrences of an old substring with a new substring.
**A:**

```python
def replace_substring(s, old, new):
    return s.replace(old, new)

# Example:
# print(replace_substring("I like apples", "apples", "bananas")) # Output: I like bananas
```

### 14\. Check for Unique Characters

**Q:** Determine if a string has all unique characters (no repeats).
**A:**

```python
def is_unique(s):
    # The length of the string must equal the length of the set of its characters
    return len(set(s)) == len(s)

# Example:
# print(is_unique("abcde")) # Output: True
# print(is_unique("hello")) # Output: False
```

### 15\. Run-Length Encoding (RLE)

**Q:** Implement a basic Run-Length Encoding (RLE) algorithm for a string (e.g., "AAABBC" -\> "A3B2C1").
**A:**

```python
def run_length_encode(s):
    if not s: return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded.append(s[i-1] + str(count))
            count = 1
    # Append the last character group
    encoded.append(s[-1] + str(count))
    return "".join(encoded)

# Example:
# print(run_length_encode("AAABBCDDDDD")) # Output: A3B2C1D5
```

-----

## 🧩 String Splitting and Joining

### 16\. Split by Delimiter

**Q:** Split a string into a list of substrings using a specific delimiter (e.g., a comma).
**A:**

```python
def split_string(s, delimiter):
    return s.split(delimiter)

# Example:
# print(split_string("red,green,blue", ",")) # Output: ['red', 'green', 'blue']
```

### 17\. Join a List of Strings

**Q:** Combine a list of strings into a single string using a specific separator (e.g., a hyphen).
**A:**

```python
def join_strings(list_of_strings, separator):
    return separator.join(list_of_strings)

# Example:
# print(join_strings(["data", "processing", "py"], "-")) # Output: data-processing-py
```

### 18\. Check if String is Numeric

**Q:** Write a function to check if a string contains only numeric characters.
**A:**

```python
def is_numeric(s):
    return s.isdigit()

# Example:
# print(is_numeric("12345"))  # Output: True
# print(is_numeric("12a34"))  # Output: False
```

### 19\. Trim Leading/Trailing Characters

**Q:** Remove leading and trailing occurrences of a specified character (e.g., `#`) from a string.
**A:**

```python
def trim_chars(s, char):
    return s.strip(char)

# Example:
# print(trim_chars("###Hello###", "#")) # Output: Hello
```

### 20\. Reverse Words in a Sentence

**Q:** Reverse the order of words in a sentence, but keep the words themselves intact.
**A:**

```python
def reverse_words(sentence):
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join them back into a string
    return " ".join(reversed_words)

# Example:
# print(reverse_words("the sky is blue")) # Output: blue is sky the
```
