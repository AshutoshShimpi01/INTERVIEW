

Here is the **BEST and MOST PRACTICAL cheat-sheet** of *“If the question says this → Use this window function”*.
This will help you instantly identify the correct window function in ANY interview question.

---

# 🚀 **Window Function Cheat-Sheet (Pattern → Function)**

### ✔ WHAT the question is asking

### ✔ Which window function to use

### ✔ SIMPLE memory tricks

---

# ✅ **1. Compare Current Row With Previous Row**

**Keywords in question:**

* "consecutive"
* "previous row"
* "compare with earlier"
* "continuity"
* "streak"

➡️ **Use: `LAG()`**

**Example:**
Find consecutive repeated words → **LAG(word)**

---

# ✅ **2. Compare Current Row With Next Row**

**Keywords in question:**

* "next row"
* "look ahead"

➡️ **Use: `LEAD()`**

**Example:**
Find next purchase date for each user → **LEAD(date)**

---

# ✅ **3. Rank Rows**

**Keywords in question:**

* "rank"
* "1st, 2nd, 3rd"
* "top N per group"
* "highest salary per department"

➡️ **Use: `RANK()` or `DENSE_RANK()`**

**Example:**
Top 3 salaries → **DENSE_RANK() OVER()**

---

# ✅ **4. Unique Rank Without Skipping Numbers**

**Keywords:**

* "no gaps in ranking"
* “continuous ranking”

➡️ **Use: `DENSE_RANK()`**

---

# ✅ **5. Row Number (1,2,3…)**

**Keywords:**

* "pick first record"
* "latest record"
* "deduplicate rows"

➡️ **Use: `ROW_NUMBER()`**

---

# ✅ **6. Running Total / Cumulative Sum**

**Keywords:**

* "running total"
* "cumulative"
* "till date"
* "progressive sum"

➡️ **Use: `SUM() OVER (ORDER BY ...)`**

---

# ✅ **7. Moving Average / Rolling Window**

**Keywords:**

* "moving average"
* "rolling 7 days"
* "previous N rows"

➡️ **Use: `ROWS BETWEEN`**

Example:

```sql
AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
```

---

# ✅ **8. Find First or Last Value in a Group**

**Keywords:**

* "first value"
* "last value"
* "earliest" / "latest"

➡️ **Use: `FIRST_VALUE()` / `LAST_VALUE()`**

*(With window frame!)*

---

# ✅ **9. Find the Difference Between Rows**

**Keywords:**

* "difference"
* "gap"
* "change"
* "delta"

➡️ **Use: `LAG()` with arithmetic**

Example:

```sql
amount - LAG(amount) OVER (...)
```

---

# ✅ **10. Group Rows Into Consecutive Blocks**

**Keywords:**

* "consecutive days"
* "continuous sequence"
* "streak"
* "group consecutive values"

➡️ **Use: `LAG()` + `SUM()` trick**

---

# ✅ **11. Percentile, N-tile, Percent Ranking**

**Keywords:**

* "percentile"
* "quartile"
* "decile"
* "top 20%"

➡️ **Use:**

* `NTILE()`
* `PERCENT_RANK()`
* `CUME_DIST()`

---

# ✅ **12. Find First Time Something Occurred**

**Keywords:**

* "first occurrence"
* "first purchase"
* "first login"

➡️ **Use: `ROW_NUMBER()`** (filter row_number = 1)

---

# ✅ **13. Find Last Time Something Occurred**

**Keywords:**

* "last occurrence"
* "latest timestamp"
* "most recent"

➡️ **Use: `ROW_NUMBER()` with descending date`**

---

# ✅ **14. Window Partitioning**

**Keywords:**

* "per department"
* "for each user"
* "per category"

➡️ **Use: `PARTITION BY` with ANY window function**

---

# 🚀 **Ultra-Short Memory Chart**

| Question Asks             | Use This Function                    |
| ------------------------- | ------------------------------------ |
| Compare with previous     | **LAG**                              |
| Compare with next         | **LEAD**                             |
| Detect consecutive values | **LAG**                              |
| Rank rows                 | **RANK / DENSE_RANK**                |
| Remove duplicates         | **ROW_NUMBER**                       |
| Running totals            | **SUM OVER**                         |
| Moving averages           | **ROWS BETWEEN**                     |
| First / Last value        | **FIRST_VALUE / LAST_VALUE**         |
| Calculate differences     | **LAG**                              |
| Percentile ranking        | **NTILE / CUME_DIST / PERCENT_RANK** |
| Group consecutive blocks  | **LAG + SUM**                        |

---

If you want, I can give you:

🔥 20 real interview questions based on this cheat-sheet
🔥 Hard consecutive-days problems
🔥 Window function practice set using your own sample tables

Just tell me!
