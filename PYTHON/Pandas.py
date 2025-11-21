

Here are **15 commonly asked Pandas interview questions with clear and simple answers** — perfect for Data Engineer roles.

---

# ✅ **15 Pandas Interview Questions with Answers**

---

## **1. What is Pandas and why is it used?**

**Answer:**
Pandas is a Python library used for **data manipulation and analysis**. It provides two main data structures:

* **Series** (1-D)
* **DataFrame** (2-D)

Used for cleaning, transforming, filtering, joining, and analyzing data.

---

## **2. Difference between Series and DataFrame?**

**Answer:**

* **Series**: One-dimensional labeled array (like one column).
* **DataFrame**: Two-dimensional table with rows and columns.

---

## **3. How do you handle missing values in Pandas?**

**Answer:**

* Fill missing values:

```python
df.fillna(0)
```

* Drop rows with nulls:

```python
df.dropna()
```

* Check nulls:

```python
df.isnull().sum()
```

---

## **4. How do you read and write CSV files in Pandas?**

**Answer:**
**Read:**

```python
df = pd.read_csv("file.csv")
```

**Write:**

```python
df.to_csv("output.csv", index=False)
```

---

## **5. How do you filter rows in Pandas?**

**Answer:**

```python
df[df["age"] > 30]
```

OR using multiple conditions:

```python
df[(df["age"] > 30) & (df["city"] == "Pune")]
```

---

## **6. How do you apply a function to a column?**

**Answer:**

```python
df["salary_after_tax"] = df["salary"].apply(lambda x: x * 0.9)
```

---

## **7. What is the difference between `loc` and `iloc`?**

**Answer:**

* **loc** → label-based indexing

```python
df.loc[2, "name"]
```

* **iloc** → integer/position-based indexing

```python
df.iloc[2, 1]
```

---

## **8. How do you merge two DataFrames?**

**Answer:**

```python
merged = df1.merge(df2, on="id", how="inner")
```

Joins supported: `inner`, `left`, `right`, `outer`.

---

## **9. How do you group data in Pandas?**

**Answer:**

```python
df.groupby("department")["salary"].sum()
```

---

## **10. What is vectorization in Pandas?**

**Answer:**
Vectorization means using Pandas internal optimized C code for operations:

```python
df["bonus"] = df["salary"] * 0.1
```

It avoids Python loops → faster.

---

## **11. How do you get basic statistics of a DataFrame?**

**Answer:**

```python
df.describe()
```

---

## **12. How do you sort a DataFrame?**

**Answer:**

```python
df.sort_values("age", ascending=False)
```

---

## **13. How do you drop a column?**

**Answer:**

```python
df.drop("age", axis=1, inplace=True)
```

---

## **14. How to rename columns?**

**Answer:**

```python
df.rename(columns={"old": "new"}, inplace=True)
```

---

## **15. What is the difference between `append()` and `concat()`?**

**Answer:**

* `append()` → adds rows but **deprecated**.
* `concat()` → preferred method for combining DataFrames.

Example:

```python
pd.concat([df1, df2], axis=0)
```

---

If you want, I can also give:

✅ **15 advanced Pandas questions**
or
✅ **Practice problems with datasets**

Just tell me!















idx = employees_df.groupby('dept_id')['salary'].idxmin()

result_df_rank = employees_df.loc[idx].sort_values('dept_id').reset_index(drop=True)

print("=== Employee with Lowest Salary per Department ===")
print(result_df_rank)



 Explination : -
 ----------------


  This code block uses a highly efficient and common **Pandas technique** to find the entire row corresponding to the minimum value (the lowest salary) within defined groups (departments).

Here is a step-by-step explanation:

-----

## 1\. ⚙️ Step 1: Find the Index of the Minimum Salary (`idx`)

```python
idx = employees_df.groupby('dept_id')['salary'].idxmin()
```

This line identifies the **index label** (row number) of the employee with the minimum salary for each department.

| Part | Function | Purpose |
| :--- | :--- | :--- |
| **`employees_df.groupby('dept_id')`** | **Grouping** | Logically partitions the `employees_df` based on the unique values in the `dept_id` column. |
| **`['salary']`** | **Selection** | Specifies that the calculation should only consider the values in the `salary` column within those groups. |
| **`.idxmin()`** | **Aggregation** | Returns the **index label** (the original row number) where the minimum salary occurs for each department group. |

The variable `idx` now holds a Series of indices that point to the rows of the minimum salary earners.

-----

## 2\. 🎯 Step 2: Retrieve the Full Rows (`result_df_rank`)

```python
result_df_rank = employees_df.loc[idx]
```

This step uses the indices found in Step 1 to extract the complete employee information from the original DataFrame.

  * **`employees_df.loc[...]`**: The **`.loc[]`** accessor is used for **label-based indexing**. By passing the Series of index labels (`idx`) to it, Pandas selects the entire rows—including the `emp_id`, `name`, `dept_id`, and `salary`—whose index labels match those in `idx`.

-----

## 3\. 🧹 Step 3: Format and Clean the Result

```python
.sort_values('dept_id').reset_index(drop=True)

print("=== Employee with Lowest Salary per Department ===")
print(result_df_rank)
```

These final methods ensure the output is clean and well-ordered:

  * **`.sort_values('dept_id')`**: Sorts the resulting DataFrame rows in ascending order based on the **`dept_id`** column for better readability.
  * **`.reset_index(drop=True)`**: Discards the original index labels (which were retained from Step 2) and assigns a new, clean, sequential index starting from 0 (i.e., 0, 1, 2, ...).
  * **`print(...)`**: Displays the final, filtered, and formatted DataFrame.
