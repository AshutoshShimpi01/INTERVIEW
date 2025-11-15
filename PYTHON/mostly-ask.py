Here are 30 concise Python interview questions and answers for a Data Engineer role:

***

1. **What are lists, tuples, and sets?**  
Lists are mutable and ordered. Tuples are immutable and ordered. Sets are unordered and store unique elements—good for deduplicating data.[5][6]

List: Ordered, mutable, allows duplicates ([])

Tuple: Ordered, immutable, allows duplicates (())

Set: Unordered, mutable, no duplicates (set())

Dictionary: Key-value pairs, unordered, mutable no duplicates({}  Keys must be unique, values can be duplicated)


2. **Remove duplicates from a list?**  
Use `list(set(mylist))` or a set comprehension.

3. **Difference between shallow and deep copy?**  
Shallow copy copies references; deep copy copies objects recursively.

4. **Read large CSV efficiently?**  
Use `pd.read_csv()` with `chunksize` or generators to process in batches.[5]

5. **What is a generator?**  
A function that yields items one at a time, saving memory for large data.

6. **Append vs. extend in lists?**  
`append()` adds a single value; `extend()` adds multiple values from another iterable.

7. **Handle nulls in a dataset?**  
Use pandas' `fillna()` or `dropna()`; replace or remove missing values.

8. **Merge two dicts in Python 3.5+?**  
`{**dict1, **dict2}` or `dict1.update(dict2)`.

9. **Iterate over dictionary pairs?**  
`for k, v in mydict.items(): ...`

10. **What’s a context manager (with statement)?**  
Safely manage resources (like files) using `with open(...) as f:`.

11. **Catch/log exceptions in ETL?**  
Use `try-except`, `logging` module for errors and debugging.[5]

12. **Connect to SQL DB in Python?**  
Use libraries like `pyodbc`, `psycopg2`, or `sqlalchemy`.

13. **Purpose of lambda functions?**  
Anonymous functions for inline mapping/filtering.

14. **List comprehensions?**  
Compact, readable way to build lists: `[x*x for x in mylist]`.

15. **What is pandas?**  
Data analysis library. Use for reading files, cleaning, transforming datasets.

16. **Write pandas DataFrame to DB?**  
`df.to_sql()` in SQLAlchemy or similar connectors.

17. **Parse JSON?**  
Use Python’s `json.loads()` for strings, `json.dumps()` for objects.

18. **os/glob modules in file I/O?**  
`os` for interacting with the filesystem; `glob` for pattern matching filenames.

19. **Logging in a pipeline?**  
Use `import logging`; set up logs to file or console for ETL tracking.

20. **What are decorators?**  
Functions that modify other functions, e.g., for timing, logging, or retries.

21. **map/filter/reduce differences?**  
`map()` applies functions, `filter()` selects items, `reduce()` aggregates items.

22. **Schedule Python scripts?**  
Use Airflow, cron, or task schedulers for automation.

23. **Process streaming data in Python?**  
Use libraries like `PySpark Streaming`, `Kafka-python`, or `socket`.

24. **Read/write data to cloud storage?**  
Use GCP's `google-cloud-storage` or AWS `boto3` libraries.[5]

25. **API rate limits/retries?**  
Use `requests` with retry/backoff logic (e.g., `time.sleep()` or `tenacity`).

26. **Multiprocessing in ETL?**  
`multiprocessing` library for parallel data tasks, speeding up computation.

27. **Parse timestamps/dates?**  
Use `datetime.strptime()` or pandas' `pd.to_datetime()`.

28. **Modules vs. packages?**  
Modules: single Python files; packages: folders with multiple modules and `__init__.py`.

29. **Use environment variables/config files?**  
Use `os.environ` or Python’s `configparser` for secret/config handling.

30. **Reusable/testable pipeline code?**  
Write functions/classes, keep code modular, add unit tests.

***

Let me know if you want code examples or explanations for any specific question!

[1](https://www.datacamp.com/blog/top-21-data-engineering-interview-questions-and-answers)
[2](https://www.interviewbit.com/python-interview-questions/)
[3](https://www.interviewquery.com/p/data-engineer-python-questions)
[4](https://www.youtube.com/watch?v=AQX7Mjb1stI)
[5](https://www.foundit.in/career-advice/data-engineer-interview-questions-and-answers/)
[6](https://www.geeksforgeeks.org/python/python-interview-questions/)
[7](https://www.reddit.com/r/dataengineering/comments/1fxpx2d/python_questions_for_data_engineer/)
