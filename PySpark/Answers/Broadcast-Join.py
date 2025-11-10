


The Broadcast Join is mostly used for one critical reason: Performance (Speed).

Here is the short, simple explanation:

Why It's Used
The Broadcast Join is the fastest join type in Spark because it avoids the most costly operation: the Data Shuffle.

The Problem: In a normal join, Spark must shuffle (physically move) large portions of both tables across the network to group matching keys together. This network transfer is slow.

The Solution: By using broadcast(), you tell Spark to copy the small table (the dimension table) into the memory of every worker machine.

The Result: The large table doesn't have to move (no shuffle!), as the local copy of the small table is already there for instant lookups. This dramatically reduces network traffic and speeds up the job.

In short: You use it to process massive joins quickly when one of the tables is small enough to fit in memory.







from pyspark.sql.functions import broadcast
# Broadcast join. - (The Broadcast Join is mostly used for one critical reason: Performance (Speed).)

df_joined = employees_df.join(broadcast(departments_df), "dept_id", "inner")

df_joined.select('*').show()

