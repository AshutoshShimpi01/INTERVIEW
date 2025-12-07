

We have use Airflow for scheduling the DataProc Jobs which creating the tables on bigQuery from different layers


There is data Architect Team on client side they will taking care of this process 
There are Different Bucket in GCS like we put different files in different buckets
So I am taking care of DataProc jobs and that files

— How you Schedule jobs ? Daily , Weekly   ?

So Table creation is daily, like we have to get incremental data daily on the basis of file requirements for that date.
And the reports are weekly, monthly and as per the client requirements.

— What is the size of data ?

The data differentiate is like wifi, routers data & bandwidth data
So the files are in TB’s, there are millions of rows we are taking care. 






— How you handle that date, like which optimization technique you are using ?


For handling those data, we are created a partitions on different tables on bigQuery.
Like if the data is coming for this day, we are checking for data for that day only & storing that data into our tables not the historical data which is stored for previous week or month
Also we are using different clusters based on the regions in which wifi routers data Is coming from.

Like using different partitioning & clustering we are optimising the tables and perform the loading into tables.  
(Here Partitioning happens daily)



— How stages created in PySpark
Like number of actions present in our spark jobs

When we write a simple code that submitted to the driver
So what driver dose
There is a concept of DAG here in graph here are multiple nodes
Here basically driver divides the code in different different jobs
So  here each jobs run parelly 
So here transformation happens like narrow & wide when there is  filter, select, map operation perform then narrow transformation happen coz there is no shuffling needed.
And when join, groupBy happens there is wide coz Here data is shuffled.
& whenever wide is happen then 1 by 1 stages is created.



— Handling Flow failure  ?

AirFlow UI, by checking/monitoring Logs we take action on that 

We have created email operator in the DAG’s using (Airflow).
Like if the data flow(Proc) job is failed because of unavailability of files  then it will  triggers  email to the client (like success and failure task in DAG). then client immediately available the file and we have again retriever the jobs



— How to you handle PySpark jobs failure like exceptions

We run pySPark jobs with the Help of Airflow
Handles exceptions using try, catch, except mechanism 
So we monitor logs on Airflow UI and take action on that



— suppose we using pyspark
and we have 2 large data set 1 is 20 GB and 1 is 22 GB
which join is best here for joining those tables


Using Shuffle Hash Join :-
SHJ is Spark's preferred method for joining two large datasets when they are too big to be broadcast.
* Mechanism: Both tables are shuffled (partitioned) across the cluster based on the join key.
* Execution: Each executor locally builds a hash table from the smaller of the two incoming partitions and probes it with the larger partition to find matches.



— How to handel daat Skewness 
* using random salt keys
*  Re-partitioning -
Repartitioning is telling Spark to completely redistribute the data chunks (partitions) in a DataFrame across the cluster, usually based on a key column (like user_id).
It's used to prepare data for big operations like joins or aggregations, ensuring data is evenly spread out to prevent slow processing on overloaded machines (data skew).


— How to improve the performance when we have joining 2 large tables 
If we partition the data frames on the joining keys(P.K/F.K) then that improve the execution speed & joins.
