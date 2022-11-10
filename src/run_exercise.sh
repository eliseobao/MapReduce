#!/bin/bash

# Delete data if already exists
hdfs dfs -test -e exercise_$1 && hdfs dfs -rm -r exercise_$1

# Delete output directory if already exists
hdfs dfs -test -e exercise_$1_output && hdfs dfs -rm -r exercise_$1_output
rm -rf exercise_$1_output

# Place exercise data in the distributed file system
hdfs dfs -put /data/exercise_$1

# Check that exercise data is in the distributed file system
# hdfs dfs -ls

## Run MapReduce job
/usr/bin/hadoop \
    jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
    -D mapreduce.job.reduces=$2 \
    -input exercise_$1/ \
    -output exercise_$1_output/ \
    -mapper /src/exercise_$1/mapper.py \
    -reducer /src/exercise_$1/reducer.py

# See content of the output folder
# hdfs dfs -ls exercise_$1_output

# Upload output folder:
hdfs dfs -get exercise_$1_output

# Combine and print results
cat exercise_$1_output/part-* >> exercise_$1_results.txt
python src/exercise_$1/combiner.py
rm exercise_$1_results.txt

echo Exercise $1 completed with $2 reduce tasks!