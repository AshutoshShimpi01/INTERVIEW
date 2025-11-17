

Below is the **ultimate Spark vs Pandas syntax cheat sheet** — all commonly used functions in **Data Engineering** with **side-by-side syntax**.

This is the **most complete comparison** you’ll need for interviews or daily work.

---

# 🔥 **Spark vs Pandas — Full Syntax Cheat Sheet**

---

# ✅ 1. **Read Data**

| Task             | **Pandas**                        | **PySpark**                                                 |
| ---------------- | --------------------------------- | ----------------------------------------------------------- |
| Read CSV         | `pd.read_csv("file.csv")`         | `spark.read.csv("file.csv", header=True, inferSchema=True)` |
| Read Parquet     | `pd.read_parquet("file.parquet")` | `spark.read.parquet("file.parquet")`                        |
| Read JSON        | `pd.read_json("file.json")`       | `spark.read.json("file.json")`                              |
| Read with schema | Not required                      | `spark.read.schema(schema).csv(..)`                         |

---

# ✅ 2. **Select Columns**

| Pandas                | Spark                      |
| --------------------- | -------------------------- |
| `df[['col1']]`        | `df.select("col1")`        |
| `df[['col1','col2']]` | `df.select("col1","col2")` |

---

# ✅ 3. **Filter / Where**

| Pandas                                    | Spark                                            |
| ----------------------------------------- | ------------------------------------------------ |
| `df[df['age'] > 30]`                      | `df.filter(df.age > 30)`                         |
| `df[(df.age > 30) & (df.city == 'Pune')]` | `df.filter((df.age > 30) & (df.city == "Pune"))` |

---

# ✅ 4. **Rename Column**

| Pandas                             | Spark                               |
| ---------------------------------- | ----------------------------------- |
| `df.rename(columns={'old':'new'})` | `df.withColumnRenamed("old","new")` |

---

# ✅ 5. **Add / Derived Column**

| Pandas                                  | Spark                                                    |
| --------------------------------------- | -------------------------------------------------------- |
| `df['total'] = df['price'] * df['qty']` | `df = df.withColumn("total", col("price") * col("qty"))` |

---

# ✅ 6. **Drop Column**

| Pandas                     | Spark            |
| -------------------------- | ---------------- |
| `df.drop(['col'], axis=1)` | `df.drop("col")` |

---

# ✅ 7. **GroupBy + Aggregation**

| Pandas                              | Spark                                                     |                                                       |
| ----------------------------------- | --------------------------------------------------------- | ----------------------------------------------------- |
| `df.groupby('city')['sales'].sum()` | `df.groupBy("city").sum("sales")`                         |                                                       |
| Multi-agg                           | `df.groupby('city').agg({'sales':'sum','profit':'mean'})` | `df.groupBy("city").agg(sum("sales"), avg("profit"))` |

---

# ✅ 8. **Sorting**

| Pandas                    | Spark                                      |                                   |
| ------------------------- | ------------------------------------------ | --------------------------------- |
| `df.sort_values('sales')` | `df.orderBy("sales")`                      |                                   |
| Descending                | `df.sort_values('sales', ascending=False)` | `df.orderBy(col("sales").desc())` |

---

# ✅ 9. **Join**

| Pandas                                | Spark                              |                                |
| ------------------------------------- | ---------------------------------- | ------------------------------ |
| `df1.merge(df2, on='id', how='left')` | `df1.join(df2, "id", "left")`      |                                |
| Multi-key                             | `df1.merge(df2, on=['id','city'])` | `df1.join(df2, ['id','city'])` |

---

# ✅ 10. **Null Handling**

| Pandas         | Spark          |
| -------------- | -------------- |
| `df.dropna()`  | `df.dropna()`  |
| `df.fillna(0)` | `df.fillna(0)` |

---

# ✅ 11. **Distinct**

| Pandas                 | Spark                          |
| ---------------------- | ------------------------------ |
| `df['city'].unique()`  | `df.select("city").distinct()` |
| `df.drop_duplicates()` | `df.dropDuplicates()`          |

---

# ✅ 12. **Apply Function**

| Pandas                           | Spark                                |
| -------------------------------- | ------------------------------------ |
| `df['col'].apply(lambda x: x*2)` | `df.withColumn("col", col("col")*2)` |
| `df.apply(lambda row:...)`       | Use UDF (slow) or Pandas UDF         |

---

# ✅ 13. **Describe Statistics**

| Pandas          | Spark           |
| --------------- | --------------- |
| `df.describe()` | `df.describe()` |

---

# ✅ 14. **Pivot / Unpivot (Melt)**

| Pandas                                                         | Spark                                           |
| -------------------------------------------------------------- | ----------------------------------------------- |
| `df.pivot_table(values='sales', index='city', columns='year')` | `df.groupBy("city").pivot("year").sum("sales")` |
| `pd.melt(df, id_vars=['city'])`                                | No direct melt → use `stack()`/SQL              |

---

# ✅ 15. **Window Functions**

| Task    | Pandas                                             | Spark                                                                          |
| ------- | -------------------------------------------------- | ------------------------------------------------------------------------------ |
| Rank    | `df['r'] = df.groupby('city')['sales'].rank()`     | `df.withColumn("r", rank().over(Window.partitionBy("city").orderBy("sales")))` |
| Lag     | `df['lag'] = df.groupby('city')['sales'].shift(1)` | `df.withColumn("lag", lag("sales",1).over(window))`                            |
| Lead    | `shift(-1)`                                        | `lead("sales",1).over(window)`                                                 |
| Rolling | `df['roll'] = df.sales.rolling(3).sum()`           | `df.withColumn("roll", sum("sales").over(window.rowsBetween(-2,0)))`           |

---

# ✅ 16. **Union**

| Pandas                  | Spark            |
| ----------------------- | ---------------- |
| `pd.concat([df1, df2])` | `df1.union(df2)` |

---

# ✅ 17. **Value Counts**

| Pandas                      | Spark                        |
| --------------------------- | ---------------------------- |
| `df['city'].value_counts()` | `df.groupBy("city").count()` |

---

# ✅ 18. **Convert Data Types**

| Pandas                  | Spark                                          |
| ----------------------- | ---------------------------------------------- |
| `df['col'].astype(int)` | `df.withColumn("col", col("col").cast("int"))` |

---

# ✅ 19. **Check Schema**

| Pandas      | Spark              |
| ----------- | ------------------ |
| `df.dtypes` | `df.printSchema()` |

---

# ✅ 20. **Head / Tail**

| Pandas      | Spark                                            |
| ----------- | ------------------------------------------------ |
| `df.head()` | `df.show(5)`                                     |
| `df.tail()` | No direct → use `df.orderBy(desc("col")).show()` |

---

# 🚀 Want a **PDF version** of this cheat sheet?

I can generate and send it to you.
