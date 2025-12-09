

| Aspect             | inferSchema=True        | schema(mySchema)        |
| ------------------ | ----------------------- | ----------------------- |
| Who decides types? | Spark guesses from data | YOU define exactly      |
| File scans         | 2 scans (infer + read)  | 1 scan (just read)      |
| Performance        | ❌ SLOWER                | ✅ FASTER                |
| Reliability        | ❌ Can guess wrong       | ✅ Always correct        |
| Production use     | ❌ Never                 | ✅ Always                |
| Code               | Simple                  | Needs schema definition |






# IMPLICIT

data = [('ashu',25),('keshu',20),('shru',22),('yogu',29)]

# NO column names provided = IMPLICIT
df = spark.createDataFrame(data)  # Spark guesses: _1, _2
df.show()



# EXPLICIT

data = [('ashu',25),('keshu',20),('shru',22),('yogu',29)]
column = ['Name','age']  # ← YOU define column names & types

df = spark.createDataFrame(data, column)  # ← Explicit schema
