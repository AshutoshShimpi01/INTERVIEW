
That's a great next step\! Here are 20 intermediate Python string coding questions specifically tailored for a **Data Engineer** role, focusing on common tasks like data cleaning, parsing complex formats, and working with delimited/structured data.

## 🛠️ Intermediate String Questions for Data Engineers

-----

### 1\. Extract Numeric IDs (Regex)

**Q:** Use a regular expression to extract all 4-digit numeric IDs from a string containing mixed data.
**A:**

```python
import re
def extract_ids(text):
    # Matches exactly four digits (\d{4})
    return re.findall(r'\b\d{4}\b', text)

# Example:
# data = "Order 1023 processed at 15:30. Error code 99. User 4567 submitted it."
# print(extract_ids(data))  # Output: ['1023', '4567']
```

### 2\. Parse Custom Delimited Data

**Q:** Parse a string where fields are separated by a pipe (`|`) and clean the whitespace from each field before returning a list of cleaned fields.
**A:**

```python
def parse_and_clean(data_string):
    fields = data_string.split('|')
    return [field.strip() for field in fields]

# Example:
# data = " product_id | price | quantity "
# print(parse_and_clean(data))  # Output: ['product_id', 'price', 'quantity']
```

### 3\. Validate Email Format (Simple Regex)

**Q:** Write a function to check if a string appears to be a valid basic email address format (e.g., `name@domain.com`).
**A:**

```python
import re
def is_valid_email(email):
    # Simple check: chars@chars.chars (not comprehensive, but good for intermediate)
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Example:
# print(is_valid_email("test@example.com")) # Output: True
# print(is_valid_email("test@example"))     # Output: False
```

### 4\. Normalize Case and Punctuation

**Q:** Write a function to convert a string to lowercase and remove all non-alphanumeric characters (used for consistent text matching).
**A:**

```python
import re
def normalize_text(text):
    text = text.lower()
    # Replace non-alphanumeric characters (and spaces) with an empty string
    return re.sub(r'[^a-z0-9\s]', '', text)

# Example:
# print(normalize_text("Product A-101 (New)!")) # Output: product a101 new
```

### 5\. Simple URL Slug Generation

**Q:** Convert a string title into a URL-friendly slug: lowercase, replace spaces with hyphens, and remove non-alphanumeric characters.
**A:**

```python
import re
def create_slug(title):
    title = title.lower()
    # Replace non-alphanumeric/non-space characters with nothing
    title = re.sub(r'[^a-z0-9\s-]', '', title)
    # Replace spaces with a single hyphen
    title = re.sub(r'\s+', '-', title).strip('-')
    return title

# Example:
# print(create_slug("Python Data Engineering 101")) # Output: python-data-engineering-101
```

-----

## 🏗️ Complex Data Structures

### 6\. JSON String Field Extraction

**Q:** Given a list of JSON strings, extract the value of a specific field (e.g., `"user_id"`) from each, handling potential missing keys gracefully (return `None` or a default).
**A:**

```python
import json
def extract_json_field(json_list, field_name):
    results = []
    for json_str in json_list:
        try:
            data = json.loads(json_str)
            results.append(data.get(field_name))
        except json.JSONDecodeError:
            results.append(None) # Handle invalid JSON
    return results

# Example:
# data = ['{"id": 1, "user_id": 100}', '{"id": 2}', 'invalid json']
# print(extract_json_field(data, "user_id")) # Output: [100, None, None]
```

### 7\. Fixed-Width Parsing

**Q:** Parse a fixed-width string using a list of column widths.
**A:**

```python
def parse_fixed_width(line, widths):
    start = 0
    fields = []
    for width in widths:
        field = line[start:start + width].strip()
        fields.append(field)
        start += width
    return fields

# Example:
# line = "ABC   1000USD"
# print(parse_fixed_width(line, [3, 4, 3])) # Output: ['ABC', '100', 'USD']
```

### 8\. Sanitizing SQL Input

**Q:** Escape single quotes in a string to prevent basic SQL injection when constructing a query string.
**A:**

```python
def sanitize_sql_input(user_input):
    # Replaces ' with ''
    return user_input.replace("'", "''")

# Example:
# comment = "O'Malley's purchase"
# print(sanitize_sql_input(comment)) # Output: O''Malley''s purchase
```

### 9\. Check CSV Quoting Consistency

**Q:** Given a string representing a single CSV row, check if the number of opening double quotes (`"`) matches the number of closing double quotes.
**A:**

```python
def check_csv_quotes(row):
    open_quotes = row.count('"')
    # For simplicity, assume valid quoting means an even number of quotes
    return open_quotes % 2 == 0

# Example:
# print(check_csv_quotes('a,"b,c",d')) # Output: True (2 quotes)
# print(check_csv_quotes('a,"b,c,d'))  # Output: False (1 quote)
```

### 10\. Split camelCase String

**Q:** Split a `camelCase` string into separate words (e.g., `userId` -\> `user id`).
**A:**

```python
import re
def split_camel_case(s):
    # Find all places where a lowercase letter is followed by an uppercase letter
    # Insert a space at those positions
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s).lower()

# Example:
# print(split_camel_case("CustomerIDField")) # Output: customer id field
```

-----

## 🧩 Regex and Data Cleanup

### 11\. Remove HTML Tags

**Q:** Use regex to strip simple HTML tags (e.g., `<b>`, `<p>`) from a string.
**A:**

```python
import re
def strip_html_tags(html_string):
    # Non-greedy match for anything between < and >
    return re.sub(r'<[^>]*?>', '', html_string)

# Example:
# html = "<b>Hello</b>, <a href='#'>world</a>!"
# print(strip_html_tags(html)) # Output: Hello, world!
```

### 12\. Count Tag Occurrences

**Q:** Count the number of times a specific HTML tag (e.g., `<p>`) appears in a string.
**A:**

```python
import re
def count_tag(html_string, tag):
    # Finds <tag>, </tag>, or <tag ...>
    pattern = rf'<{re.escape(tag)}\b[^>]*?>'
    return len(re.findall(pattern, html_string, re.IGNORECASE))

# Example:
# html = "<p>para 1</p><P style=''>para 2</P>"
# print(count_tag(html, "p")) # Output: 2
```

### 13\. Replace Multiple Separators

**Q:** Replace sequences of multiple spaces or tabs with a single space.
**A:**

```python
import re
def single_space(text):
    # Matches one or more whitespace characters (\s+) and replaces with one space
    return re.sub(r'\s+', ' ', text).strip()

# Example:
# print(single_space("Data   Engineering\t is cool")) # Output: Data Engineering is cool
```

### 14\. Convert Bytes to Human-Readable Format

**Q:** Write a function to convert a raw number of bytes into a human-readable string (KB, MB, GB).
**A:**

```python
def bytes_to_human(bytes_val):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    if bytes_val == 0:
        return "0 B"
    # Calculate the unit index (0 for B, 1 for KB, etc.)
    import math
    i = int(math.floor(math.log(bytes_val, 1024)))
    p = math.pow(1024, i)
    s = round(bytes_val / p, 2)
    return f"{s} {units[i]}"

# Example:
# print(bytes_to_human(1048576))  # Output: 1.0 MB
```

### 15\. Simple Date Format Standardizer

**Q:** Use regex to replace inconsistent date separators (hyphens or slashes) with a common separator (e.g., forward slash) in a `DD-MM-YYYY` or `DD/MM/YYYY` format.
**A:**

```python
import re
def standardize_date(date_str):
    # Matches a digit, followed by - or /, followed by digits
    # Only replaces if the original format looks like a date
    return re.sub(r'([0-9]{2})[/-]([0-9]{2})[/-]([0-9]{4})', r'\1/\2/\3', date_str)

# Example:
# print(standardize_date("25-12-2023")) # Output: 25/12/2023
# print(standardize_date("01/01/2024")) # Output: 01/01/2024
```

-----

## 🗃️ Utility and Final Checks

### 16\. Count Word Frequency (Case-Insensitive)

**Q:** Count the frequency of every word in a string, ensuring the counting is case-insensitive.
**A:**

```python
from collections import Counter
import re

def word_frequency(text):
    # Clean up non-alphanumeric characters and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# Example:
# print(word_frequency("Data is data. The data is King."))
# Output: Counter({'data': 3, 'is': 2, 'the': 1, 'king': 1})
```

### 17\. Truncate with Ellipsis

**Q:** Truncate a string to a maximum length (e.g., 50 characters) and append an ellipsis (`...`) if truncation occurs.
**A:**

```python
def truncate_string(s, max_len):
    if len(s) > max_len:
        return s[:max_len - 3] + "..."
    return s

# Example:
# print(truncate_string("A long description..." * 3, 20)) # Output: A long description...
```

### 18\. Check if String is Valid Integer

**Q:** Write a function that accurately checks if a string represents a valid integer (including positive, negative, and zero).
**A:**

```python
def is_integer(s):
    # Strips leading/trailing whitespace and checks if it's a digit or starts with - and is a digit
    s = s.strip()
    return s.isdigit() or (s.startswith('-') and s[1:].isdigit())

# Example:
# print(is_integer("-123"))   # Output: True
# print(is_integer("123.0"))  # Output: False
```

### 19\. Simple CSV Row to Dictionary

**Q:** Convert a comma-separated row string and a list of headers into a dictionary.
**A:**

```python
def csv_row_to_dict(row_string, headers):
    values = [v.strip() for v in row_string.split(',')]
    if len(values) != len(headers):
        return {"error": "Mismatched counts"}
    return dict(zip(headers, values))

# Example:
# headers = ["name", "age", "city"]
# row = "Alice, 30, New York"
# print(csv_row_to_dict(row, headers))
# Output: {'name': 'Alice', 'age': '30', 'city': 'New York'}
```

### 20\. Simple String Interpolation

**Q:** Write a function that takes a template string with placeholders (e.g., `{name}`) and a dictionary, and returns the formatted string.
**A:**

```python
def interpolate_template(template, data_dict):
    return template.format(**data_dict)

# Example:
# template = "The user {user} completed {tasks} tasks."
# data = {"user": "Bob", "tasks": 5}
# print(interpolate_template(template, data))
# Output: The user Bob completed 5 tasks.
```
