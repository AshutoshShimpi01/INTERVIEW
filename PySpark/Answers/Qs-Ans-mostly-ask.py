

Here are 15 scenario-based PySpark interview questions with concise sample answers, focusing on when and why to use various PySpark transformations and related concepts:

***

1. **When should you use a narrow transformation?**  
   Use narrow transformations (like `map`, `filter`) when each output partition reads only its input partition—ideal for row-wise changes and faster execution due to no shuffling.

2. **When do you need a wide transformation?**  
   Wide transformations (like `groupBy`, `join`) are required when output depends on multiple input partitions, such as aggregating, sorting, or joining—these trigger a shuffle.

3. **How can you minimize data shuffling in a join?**  
   Use broadcast joins when one DataFrame is small, or pre-partition data by join key to localize operations and reduce network transfer.

4. **What decides the number of DataFrame partitions?**  
   Balance between too few partitions (slows parallelism) and too many (overheads, small tasks). Tune partitions based on cluster size and input data volume.

5. **How do you handle skewed data in wide transformations?**  
   Add random salts to keys, increase partitions, or use custom partitioning to spread skewed keys across the cluster evenly.

6. **How can you load evolving schema data robustly?**  
   Use schema inference with `inferSchema=True`, handle schema evolution logic in code, and validate new columns before processing.

7. **When should you cache or persist a DataFrame?**  
   Cache DataFrames reused in multiple actions to avoid recomputation; choose storage level (memory/disk) based on resource availability.

8. **How does Spark handle node failures in a job?**  
   Spark rebuilds the lost partition from lineage (previous steps), ensuring replay and fault tolerance without data loss.

9. **Parquet vs. CSV: When to use each?**  
   Use Parquet for analytics—smaller size, columnar reads, and fast performance; use CSV for compatibility if downstream doesn’t support Parquet.

10. **Why use window functions in PySpark?**  
    For calculations across a moving window of rows (like rolling sums), especially for time-based analytics and grouped aggregations.

11. **Why is data locality important?**  
    Data processed where it’s stored reduces network and I/O overhead, which matters most for large-scale shuffles and wide transforms.

12. **How to handle late-arriving event records?**  
    Use watermarking and allowed lateness features in structured streaming to accommodate and reprocess delayed data correctly.

13. **How do you log and skip corrupt records?**  
    Use try-except inside UDFs or built-in corrupted record options, log issues, and continue processing good data to maintain pipeline robustness.

14. **When is dynamic resource allocation useful?**  
    In variable/burst workloads on Dataproc, Spark can auto-scale executors based on needs, saving costs and improving job performance.

15. **Should you chain narrow transformations before a wide one? Why?**  
    Yes. This filters and reduces data as much as possible before the shuffle, minimizing costly wide transformation overhead.

***

Let me know if you need detailed code examples or explanations for any of these!

[1](https://www.datacamp.com/blog/pyspark-interview-questions)
[2](https://www.interviewbit.com/pyspark-interview-questions/)
[3](https://www.coursera.org/in/articles/pyspark-interview-questions)
[4](https://www.projectpro.io/article/pyspark-interview-questions-and-answers/520)
[5](https://k21academy.com/data-engineering/pyspark-interview-questions/)
[6](https://www.knowledgehut.com/interview-questions/pyspark-interview-questions)
