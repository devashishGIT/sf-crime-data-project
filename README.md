# sf-crime-data-project
In this project, a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and we will provide statistical analyses of the data using Apache Spark Structured Streaming. 

Q1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Answer: Using property processedRowsPerSecond we can manipulate the processing speed of data ingestion on spark. It can help in increasing the throughput.

Q2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Answer: In order to increase the value for processedRowsPerSecond , I tried follwowing parameters independently one after another : 
      
      spark.sql.shuffle.partitions
      spark.streaming.kafka.maxRatePerPartition
      spark.default.parallelism
      
 
