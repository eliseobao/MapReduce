#!/bin/bash

# Delete data if already exists
hdfs dfs -test -e exercise_0 && hdfs dfs -rm -r exercise_0

# Delete output directory if already exists
hdfs dfs -test -e exercise_0_output && hdfs dfs -rm -r exercise_0_output
rm -rf exercise_0_output

# Place exercise_0 in the distributed file system
hdfs dfs -put /data/exercise_0

# Check that exercise_0 is in the distributed file system
# hdfs dfs -ls

# Run MapReduce job
/usr/bin/hadoop \
    jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
    -input exercise_0/ \
    -output exercise_0_output/ \
    -mapper /src/exercise_0/mapper.py \
    -reducer /src/exercise_0/reducer.py

# See content of the output folder
# hdfs dfs -ls exercise_0_output

# See output
# hdfs dfs -cat exercise_0_output/part-00000

# See sorted results
hdfs dfs -cat exercise_0_output/part-00000 | sort -k 2 -n

# Upload output folder:
hdfs dfs -get exercise_0_output

echo $'Exercise 0 completed!'