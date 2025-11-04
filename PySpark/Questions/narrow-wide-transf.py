


Here’s how you can formulate scenario-based interview questions about **when to use narrow vs. wide transformations in PySpark** (with answers and examples):

***

### **Interview Question:**
**Scenario:**  
You are optimizing a PySpark job on Dataproc that processes a large dataset.  
- **When would you prefer to use a narrow transformation? Give examples.**  
- **When is a wide transformation necessary? Give examples.**  
- **What are the practical impacts of choosing one over the other in a distributed environment like Dataproc?**

***

### **Sample Answer:**

- **Narrow transformations** (like `map`, `filter`, `withColumn`, `select`) are preferred when each output partition depends only on a single input partition.  
  - **Example:** If you need to clean up or modify every row individually (e.g., adding 10% to every price, or removing rows with null values), you should use a narrow transformation because these do not cause data to move (shuffle) between partitions. This keeps Spark jobs highly efficient and fast to execute.[1][5]
- **Wide transformations** (like `groupBy`, `join`, `distinct`, `reduceByKey`, `orderBy`) are necessary when you need to combine, aggregate, or rearrange data across partitions.  
  - **Example:** If you must count sales by region or join your sales data with an external lookup DataFrame, you need a wide transformation. These actions require shuffling data between nodes, which is more resource-intensive and can slow down your job.[5][6][7][1]
- **Practical impact:**  
  - Narrow transformations minimize shuffling—meaning less network traffic, lower memory use, and better runtime performance, making them the best choice for simple or stepwise manipulations.
  - Wide transformations can introduce significant network and disk I/O overhead. While necessary for aggregations or joins, they should be minimized and optimized through techniques like partitioning or filter-pushdown whenever possible.

***

**Follow-Up Example:**  
*“Suppose you’re running ETL for millions of user transactions: you would first filter invalid rows (narrow), add calculated columns (narrow), and only do grouping or joining in the final stages (wide) to minimize the impact from data shuffling.”*

***

If you’d like more scenario questions around transformations, physical plan optimization, or Spark shuffling, just ask!

[1](https://www.c-sharpcorner.com/article/narrow-vs-wide-transformations-in-pyspark/)
[2](https://www.geeksforgeeks.org/data-engineering/wide-and-narrow-dependencies-in-apache-spark/)
[3](https://www.linkedin.com/pulse/wide-vs-narrow-transformations-sparkdistributed-compute-don-hilborn)
[4](https://www.youtube.com/watch?v=a_gaUIZdkEQ)
[5](https://bigdataperformance.substack.com/p/understanding-wide-vs-narrow-transformations)
[6](https://www.garageeducation.org/docs/apache-spark/21-transformations-narrow-vs-wide/)
[7](https://stackoverflow.com/questions/77156805/wide-and-narrow-transformations-in-spark)
