Here are 15 scenario-based PySpark interview questions (with a GCP/Dataproc context where relevant) focusing on **Spark transformations, job design, performance, and distributed processing**—including concepts like narrow & wide transformations, shuffling, partitions, etc.

***

### PySpark Scenario-Based Interview Questions

1. **Mapping Data with PySpark**
   - In which data processing scenario would you choose `map` (narrow) over `groupBy` (wide) when cleaning event logs in Dataproc?

2. **Reducing Shuffles**
   - Your PySpark job spends excessive time shuffling during a join. What steps would you take to reduce shuffling, and why does reducing it matter for job performance on Dataproc?

3. **Join Type Selection**
   - When processing two large tables in PySpark, how do you decide whether to use a broadcast join or a regular join, and how does this impact cluster resource usage?

4. **Partition Count Tuning**
   - How do you determine the optimal number of partitions for a PySpark DataFrame on Dataproc? What are the risks if there are too few or too many?

5. **Handling Skewed Data**
   - If you notice one task is taking much longer than others due to data skew in a wide transformation, what practical approaches would you use to fix the issue?

6. **Schema Evolution**
   - If your input data schema (CSV, JSON, etc.) changes daily, what strategies in PySpark or Dataproc can make your jobs robust to evolving schemas?

7. **Caching and Persistence**
   - In an ETL workflow with multiple steps using the same DataFrame, when would you use `cache()` or `persist()`? How do you decide which storage level to use on Dataproc?

8. **Fault Tolerance**
   - How does PySpark achieve fault tolerance during a transformation pipeline in Dataproc? Give an example where this feature prevented data loss.

9. **File Formats**
   - When would you choose to write ETL output as Parquet vs. CSV for downstream analytics, and what impact does this choice have on performance at scale?

10. **Window Operations**
    - Describe a scenario when you would use window functions in PySpark. How do these affect job planning and partitioning?

11. **Data Locality**
    - Why is data locality important for PySpark jobs on Dataproc? How does it impact the efficiency of narrow and wide transformations?

12. **Handling Late Data**
    - How would you handle late-arriving records in a real-time streaming PySpark job? What impact does this have on stateful operations?

13. **Error Handling and Logging**
    - If a row in your input data consistently fails a transformation due to corrupt values, how would you capture and log such errors without failing the entire PySpark job?

14. **Dynamic Resource Allocation**
    - How does enabling dynamic resource allocation in Dataproc help for large batch jobs, and what PySpark configurations support this?

15. **Chaining Transformations**
    - Explain why it’s (or isn’t) efficient to chain multiple narrow transformations before a wide one in your PySpark code. Give an example involving a typical ETL on Dataproc.

***

Let me know if you'd like model answers, detailed explanations, or more focus on a specific kind of Spark/PySpark operation!
