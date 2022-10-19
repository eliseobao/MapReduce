#!/bin/bash

# Delete data if already exists
hdfs dfs -test -e exercise_1 && hdfs dfs -rm -r exercise_1

# Delete output directory if already exists
hdfs dfs -test -e exercise_1_output && hdfs dfs -rm -r exercise_1_output
rm -rf exercise_1_output

# Place exercise_1 in the distributed file system
hdfs dfs -put /data/exercise_1

# Check that exercise_1 is in the distributed file system
# hdfs dfs -ls

## Run MapReduce job
/usr/bin/hadoop \
    jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
    -D mapreduce.job.reduces=2 \
    -input exercise_1/ \
    -output exercise_1_output/ \
    -mapper /src/exercise_1/mapper.py \
    -reducer /src/exercise_1/reducer.py

# See content of the output folder
# hdfs dfs -ls exercise_1_output

# Upload output folder:
hdfs dfs -get exercise_1_output

# Combine and print results
cat exercise_1_output/part-* >> exercise_1_results.txt
python src/exercise_1/combiner.py
rm exercise_1_results.txt

echo $'Exercise 1 completed!'