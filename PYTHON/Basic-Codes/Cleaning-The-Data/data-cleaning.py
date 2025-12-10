

I can certainly provide the 20 data cleaning examples in a clear, formatted structure with the Python code and explanations as requested.

-----

## 🧹 20 Data Cleaning Examples with Python Code

### I. String and Text Cleaning (Examples 1-10)

These examples focus on normalizing common issues in text fields.

#### 1\. Leading/Trailing Whitespace Removal

```python
# The string with extra spaces
value = " Alice "

# Use .strip() to remove leading and trailing whitespace
cleaned_value = value.strip()

print(cleaned_value)
# Output: Alice
```

**Explanation:** The `.strip()` method is the standard Python way to remove any space, tab, or newline character from the beginning and end of a string.

-----

#### 2\. Inconsistent Case Standardization

```python
# Inconsistent data entries
value_1 = "london"
value_2 = "LONDON"

# Use .lower() to standardize to lowercase
cleaned_value_1 = value_1.lower()
cleaned_value_2 = value_2.lower()

print(cleaned_value_1, cleaned_value_2)
# Output: london london
```

**Explanation:** Standardizing case (usually to **lowercase**) is crucial for grouping and matching records accurately (e.g., in a `GROUP BY` clause in SQL or a dictionary lookup in Python).

-----

#### 3\. Removing Specific Punctuation

```python
# String containing unwanted punctuation
value = "Product (XYZ)."

# Use multiple .replace() calls to remove specific characters
cleaned_value = value.replace('.', '').replace('(', '').replace(')', '')

print(cleaned_value)
# Output: Product XYZ
```

**Explanation:** The `.replace(old, new)` method is simple and effective for substituting one character or substring with another (in this case, with an empty string `''`).

-----

#### 4\. Prefix Removal (Mobile Number Example)

```python
# The mobile number string
mobile_number = "+91 7030210200"

# Slice the string starting from index 4 to the end
cleaned_number = mobile_number[4:]

print(cleaned_number)
# Output: 7030210200
```

**Explanation:** String **slicing** (`[start:end]`) is efficient when the prefix (` +91  `) has a known, fixed length (4 characters), allowing you to start the string from index 4.

-----

#### 5\. Suffix Removal

```python
# Data with an unwanted suffix
value = "AnnualReport-2023.pdf"

# Use .removesuffix() (Python 3.9+) to remove the suffix if present
cleaned_value = value.removesuffix(".pdf")

print(cleaned_value)
# Output: AnnualReport-2023
```

**Explanation:** The `.removesuffix()` method is a clean way to remove a trailing substring, improving readability over repeated `if value.endswith(...)` checks.

-----

#### 6\. Condensing Multiple Spaces

```python
# String with erratic spacing
value = "Data  Cleaning is   Important"

# Use .split() and then ' '.join() to condense spaces
cleaned_value = " ".join(value.split())

print(cleaned_value)
# Output: Data Cleaning is Important
```

**Explanation:** The `.split()` method (with no arguments) splits the string by **any** sequence of whitespace. Then, `' '.join()` rejoins the resulting list of words with a **single space** between them.

-----

#### 7\. Handling Non-ASCII Characters

```python
# String with a character that might cause encoding issues
value = "Jap\u00e3o (Japan)"

# Encode to ASCII, ignoring errors, then decode back to a string
cleaned_value = value.encode('ascii', 'ignore').decode()

print(cleaned_value)
# Output: Jap o (Japan)
```

**Explanation:** This forces the string to a basic encoding (ASCII), removing characters outside that range (like `ã`), which is often necessary when dealing with older systems or incompatible files.

-----

#### 8\. Inconsistent Quotes

```python
# String with unwanted surrounding quotes
value = "'Single Quote'"

# Use .strip() to remove the surrounding quotes
cleaned_value = value.strip("'")

print(cleaned_value)
# Output: Single Quote
```

**Explanation:** The `.strip(chars)` method can take specific characters to strip from the beginning and end, effectively cleaning up inconsistent quoting in text fields.

-----

#### 9\. Removing HTML/XML Tags (Simple)

```python
# String containing simple HTML tags
value = "<b>Important</b> Data Point"

# Use .replace() to remove specific tags
cleaned_value = value.replace('<b>', '').replace('</b>', '')

print(cleaned_value)
# Output: Important Data Point
```

**Explanation:** While complex HTML needs libraries like BeautifulSoup, simple, known tags can be efficiently stripped using `.replace()`.

-----

#### 10\. Removing Newline/Tab Characters

```python
# String with embedded formatting characters
value = "Record 1\t\t\nRecord 2"

# Replace tab (\t) and newline (\n) with a space
cleaned_value = value.replace('\t', ' ').replace('\n', ' ')

print(cleaned_value)
# Output: Record 1   Record 2
```

**Explanation:** This is essential when reading data where line breaks or multiple tabs were used incorrectly within a single cell or record.

-----

### II. Numerical and Format Cleaning (Examples 11-15)

These examples ensure numerical data is ready for computation.

#### 11\. Removing Currency Symbols

```python
# String representing a monetary value
value = "$150,500.50"

# Remove currency and thousand separators, then convert to float
cleaned_value = float(value.replace('$', '').replace(',', ''))

print(cleaned_value)
# Output: 150500.5
```

**Explanation:** By stripping non-numeric characters first, the `float()` constructor can correctly interpret the string as a numerical value.

-----

#### 12\. Removing Percentage Signs

```python
# String representing a percentage
value = "15.5%"

# Strip the '%' sign and convert to a decimal float
cleaned_value = float(value.strip('%')) / 100

print(cleaned_value)
# Output: 0.155
```

**Explanation:** The data is converted to its true decimal form by removing the `%` and dividing by 100, which is typically required for calculations.

-----

#### 13\. Extracting Numbers from Mixed Text

```python
import re

# String containing both text and a number
value = "There are 25 years old."

# Use regex to find and extract the first sequence of digits
match = re.search(r'\d+', value)
cleaned_value = int(match.group()) if match else None

print(cleaned_value)
# Output: 25
```

**Explanation:** The `re.search(r'\d+', ...)` function finds the first one or more digits (`\d+`), allowing you to isolate the numerical component of the string.

-----

#### 14\. Fixing European Decimal Format

```python
# European number format (comma as decimal, period as thousand separator)
value = "1.500,50"

# Swap period and comma to conform to US/standard format
cleaned_value = float(value.replace('.', '').replace(',', '.'))

print(cleaned_value)
# Output: 1500.5
```

**Explanation:** A two-step replacement is performed: remove the thousand separators (`.`), then change the decimal separator (`  , `) to a period (`.`), allowing `float()` to work correctly.

-----

#### 15\. Converting String Floats to Integers

```python
# String representing a whole number as a float
value = "150.0"

# Convert to float first to handle the decimal, then to integer
cleaned_value = int(float(value))

print(cleaned_value)
# Output: 150
```

**Explanation:** You must convert the string to a `float` first to parse the decimal point, and then converting that `float` to an `int` safely truncates the `.0` part.

-----

### III. Structural and Categorical Cleaning (Examples 16-20)

These examples handle duplicates, missing data, and standardization.

#### 16\. Removing Duplicates (Order Preserved)

```python
# The list with duplicates
data_list = [1, 4, 2, 4, 7, 3, 8, 9, 7, 5]

# Use dict.fromkeys() to leverage the unique, ordered nature of dictionary keys (Python 3.7+)
unique_list = list(dict.fromkeys(data_list))

print(unique_list)
# Output: [1, 4, 2, 7, 3, 8, 9, 5]
```

**Explanation:** This is a Pythonic shortcut. When you create a dictionary from keys, only the first occurrence of each key is kept, and the order is preserved.

-----

#### 17\. Standardizing Missing Values

```python
# List of different missing data representations
missing_data = ["", "N/A", "missing", "data"]

cleaned_list = [
    None if item.lower() in ('', 'n/a', 'missing') else item
    for item in missing_data
]

print(cleaned_list)
# Output: [None, None, None, 'data']
```

**Explanation:** A list comprehension is used to check for common missing value placeholders and replace them with the standard Python missing value: **`None`**.

-----

#### 18\. Categorical Mapping/Standardization

```python
# Inconsistent categorical data
country_data = ["USA", "U.S.A.", "United States", "Canada"]

# Mapping dictionary for inconsistent terms
mapping = {'u.s.a.': 'USA', 'united states': 'USA'}

cleaned_data = [
    mapping.get(item.lower(), item) # Use .get() to return the original item if no map key exists
    for item in country_data
]

print(cleaned_data)
# Output: ['USA', 'USA', 'USA', 'Canada']
```

**Explanation:** A **mapping dictionary** is the most reliable way to enforce consistent spelling for categorical fields.

-----

#### 19\. Converting String Booleans

```python
# Various ways to represent 'True' in data
value = "Y"

# Check if the string is one of the "True" representations
is_true = value.upper() in ('Y', 'YES', 'TRUE', 'T')

print(is_true)
# Output: True
```

**Explanation:** By converting to uppercase and checking against a set of known valid strings, you reliably convert human-entered text into a consistent Python **boolean** (`True` or `False`).

-----

#### 20\. Simple Data Truncation (Limiting Length)

```python
# String that is too long for a database column
long_description = "This description is unnecessarily long and exceeds the 50 character limit..."
max_length = 50

# Truncate the string to the maximum allowed length
truncated_description = long_description[:max_length]

print(truncated_description)
# Output: This description is unnecessarily long and exceed
```

**Explanation:** **Slicing** is used to enforce data quality rules by cutting off any string that exceeds a predefined length, preventing database errors.
