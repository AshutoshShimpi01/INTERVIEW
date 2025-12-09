

| Aspect             | inferSchema=True        | schema(mySchema)        |
| ------------------ | ----------------------- | ----------------------- |
| Who decides types? | Spark guesses from data | YOU define exactly      |
| File scans         | 2 scans (infer + read)  | 1 scan (just read)      |
| Performance        | ❌ SLOWER                | ✅ FASTER                |
| Reliability        | ❌ Can guess wrong       | ✅ Always correct        |
| Production use     | ❌ Never                 | ✅ Always                |
| Code               | Simple                  | Needs schema definition |
