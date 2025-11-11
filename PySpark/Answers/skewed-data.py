
Skewed data
-------------
Skewed data is when the majority of data points are heavily concentrated on one side or around a few keys, making the distribution uneven.

In big data, this causes bottlenecks because one processing unit gets assigned almost all the work.



how tos handle skewed data in wide transformations:

Technique,Goal,How it Works
1. Add Random Salts,Targeted Skew Fix,"Concatenate a random number (salt) to the highly skewed key, temporarily creating many unique keys. 
This forces the records to be spread across many partitions and executors, enabling parallel processing."

2. Increase Partitions,Volume Fix,"Increase the total number of partitions used by the job. This helps if the problem is simply that the data volume is too large for the 
existing partitions, but it is ineffective against true key skew (one key still goes to one partition)."

3. Custom Partitioning,Advanced Skew Fix,"Write a custom function to calculate the partition ID. This allows you to specifically instruct the framework (like Spark) to 
distribute records for a known skewed key across multiple partitions, often by applying salting logic inside the custom partitioner."










There are three primary techniques to handle **skewed data** in PySpark, all aimed at spreading the records of a heavily repeated key across multiple executors for parallel processing.

## 🛠️ Key Skew Handling Techniques

---

### 1. Salting (The Most Effective)

This method forces the records of a single skewed key to be partitioned across many nodes.

* **How it works:** You **add a random number (salt)** to the skewed join/grouping key.
    * **Original Key:** `city_id: 'NYC'` (1 million records)
    * **Salted Key:** `city_id: 'NYC_1'`, `city_id: 'NYC_2'`, ..., `city_id: 'NYC_N'`
* **Result:** The framework (Spark) sees $N$ unique keys instead of one, distributing the load of the originally skewed key evenly across $N$ partitions.

---

### 2. Custom Partitioning

This gives you direct control over how data is routed to partitions.

* **How it works:** You define a **custom Python function** that tells Spark which partition index to use for each record based on its key.
* **Application:** For a non-skewed key, you use the default hash. For a known highly skewed key, your custom function can use a randomizing logic (similar to salting) to assign it to one of many partitions, thereby breaking the bottleneck.

---

### 3. Increasing Partitions

While not a true skew fix, this is a basic, necessary step.

* **How it works:** You increase the overall number of partitions for the job (e.g., using `.repartition()`).
* **Limitation:** It only helps when the **total volume of data is too large** for the current number of partitions. It **does not solve true key skew**, as all records for a single skewed key will still end up in the same partition regardless of how many total partitions exist.
