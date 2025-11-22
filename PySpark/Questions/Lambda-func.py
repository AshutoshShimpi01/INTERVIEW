

Lambda functions in Python are small, anonymous (nameless) functions defined using the keyword `lambda`. They can take any number of arguments but can only have one expression. The result of this expression is what the function returns.

Here are 10 basic Python lambda function codes, demonstrating their primary use cases.

## 💡 Lambda Function Basics

| Use Case | Standard Function (Def) | Lambda Function | Result |
| :--- | :--- | :--- | :--- |
| **1. Basic Addition** | `def add(x, y): return x + y` | `add = lambda x, y: x + y` | `add(5, 3)` $\rightarrow$ **8** |
| **2. Squaring a Number** | `def sq(x): return x * x` | `square = lambda x: x * x` | `square(4)` $\rightarrow$ **16** |
| **3. Simple Condition** | (More verbose) | `check = lambda x: "Even" if x % 2 == 0 else "Odd"` | `check(7)` $\rightarrow$ **'Odd'** |
| **4. Multiply by Constant** | `def mult(x): return x * 10` | `times_ten = lambda x: x * 10` | `times_ten(2)` $\rightarrow$ **20** |

-----

## 🧩 Lambda with Higher-Order Functions

Lambda functions are most powerful when used as arguments to built-in functions like `map()`, `filter()`, and `sorted()`.

### 5\. `filter()`: Selecting Elements

Use a lambda function to **filter** items from an iterable based on a condition.

**Code:** Find all numbers in a list greater than 10.

```python
numbers = [5, 12, 8, 15, 3]

# Lambda returns True/False for the filter
result = list(filter(lambda x: x > 10, numbers))

# print(result)
# Output: [12, 15]
```

### 6\. `map()`: Applying a Transformation

Use a lambda function to **apply the same operation** to every item in an iterable.

**Code:** Convert all list elements to their string representation.

```python
data = [1, 2, 3.5, True]

# Lambda performs the transformation (str(x))
result = list(map(lambda x: str(x), data))

# print(result)
# Output: ['1', '2', '3.5', 'True']
```

### 7\. `sorted()`: Sorting by a Key

Use a lambda function to define a custom **sorting key** for a list of complex objects (like tuples or dictionaries).

**Code:** Sort a list of tuples by the **second element** (index 1).

```python
pairs = [(1, 5), (3, 2), (2, 8)]

# Lambda specifies the key for sorting (element at index 1)
result = sorted(pairs, key=lambda p: p[1])

# print(result)
# Output: [(3, 2), (1, 5), (2, 8)]
```

### 8\. Sorting Dictionaries by a Value

**Code:** Sort a list of dictionaries by the value of the 'score' key.

```python
data = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]

# Lambda specifies the key for sorting (the 'score' value)
result = sorted(data, key=lambda item: item['score'])

# print(result)
# Output: [{'name': 'B', 'score': 75}, {'name': 'A', 'score': 90}]
```

### 9\. Lambda with Multiple Arguments

Lambda can accept multiple arguments, often used when processing two iterables simultaneously (e.g., with `map` and `zip`).

**Code:** Calculate the sum of corresponding elements from two lists.

```python
list1 = [10, 20, 30]
list2 = [1, 2, 3]

# Lambda takes two arguments (x and y) from the zip object
result = list(map(lambda x, y: x + y, list1, list2))

# print(result)
# Output: [11, 22, 33]
```

### 10\. Lambda with Nested Conditions

Lambda can handle complex conditions using nested ternary operators (though this is often discouraged for readability).

**Code:** Check if a number is positive, negative, or zero.

```python
check_sign = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")

# print(check_sign(10))   # Output: Positive
# print(check_sign(-5))    # Output: Negative
# print(check_sign(0))     # Output: Zero
```
