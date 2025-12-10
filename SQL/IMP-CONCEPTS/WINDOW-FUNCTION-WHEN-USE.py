

These are the most commonly used **Window Functions** in SQL for ranking, navigating, and performing comparative analysis on data. They differ from standard aggregate functions (like `SUM()` or `COUNT()` with `GROUP BY`) because they perform calculations across a defined set of rows **without collapsing or reducing the original number of rows**.

-----

## 🥇 Ranking Functions

These functions assign a sequential or competitive rank to rows within a partition (group). They require an `ORDER BY` clause to define the basis of the ranking.

### 1\. `ROW_NUMBER()`

  * **Function:** Assigns a unique, sequential integer to each row within its partition, starting at 1.
  * **Key Feature:** It treats identical values (ties) as separate, distinct rows.
  * **Use Case:** Ideal for scenarios where you need a unique identifier for ordering, like **deleting duplicate records** (keeping only `ROW_NUMBER() = 1`) or fetching the *first* record of a group.
  * **Syntax Example:**
    ```sql
    ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC)
    ```
    (Assigns a unique rank to employees within each `Department` based on their `Salary`.)

### 2\. `RANK()`

  * **Function:** Assigns a rank to each row within its partition.
  * **Key Feature:** If two or more rows have the same value (a **tie**), they receive the same rank. The rank of the *next* row is then skipped, leading to a gap in the ranking sequence.
  * **Use Case:** Finding the exact placement in a competitive scenario where ties matter (e.g., in a race where two people tie for 1st place, the next person is 3rd).
  * **Example:** If two salaries tie for 2nd place, the ranks will be **1, 2, 2, 4, 5...** (Rank 3 is skipped).

### 3\. `DENSE_RANK()`

  * **Function:** Assigns a rank to each row within its partition.
  * **Key Feature:** If two or more rows have the same value (a **tie**), they receive the same rank. However, there are **no gaps** in the ranking sequence.
  * **Use Case:** Finding the rank without skipping numbers due to ties (e.g., listing medal positions where ties still lead to the next consecutive rank number).
  * **Example:** If two salaries tie for 2nd place, the ranks will be **1, 2, 2, 3, 4...** (Rank 3 is *not* skipped).

-----

## ↔️ Navigation Functions

These functions allow you to retrieve the value of a column from a row preceding or following the current row within the partition, enabling powerful time-series and comparative analysis.

### 4\. `LAG()`

  * **Function:** Retrieves the value of an expression from a **previous** row (lagging behind the current row) in the ordered partition.
  * **Use Case:** Comparing the current value to the value from a previous time period (e.g., comparing this month's sales to **last month's sales**).
  * **Syntax Example:**
    ```sql
    LAG(Sales, 1, 0) OVER (ORDER BY SaleDate)
    ```
    (Returns the `Sales` value from the row **1 position before** the current row. If no previous row exists, it returns the optional default value of `0`.)

### 5\. `LEAD()`

  * **Function:** Retrieves the value of an expression from a **subsequent** row (leading ahead of the current row) in the ordered partition.
  * **Use Case:** Comparing the current value to a future time period or event (e.g., comparing a project's start date to its **next milestone date**).
  * **Syntax Example:**
    ```sql
    LEAD(StockPrice, 7) OVER (ORDER BY TradingDate)
    ```
    (Returns the `StockPrice` from the row **7 positions after** the current row, useful for looking one week ahead.)
