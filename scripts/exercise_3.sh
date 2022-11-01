#!/bin/bash

# Delete data if already exists
hdfs dfs -test -e exercise_3 && hdfs dfs -rm -r exercise_3

# Delete output directory if already exists
hdfs dfs -test -e exercise_3_output && hdfs dfs -rm -r exercise_3_output
rm -rf exercise_3_output

# Place exercise_3 in the distributed file system
hdfs dfs -put /data/exercise_3

# Check that exercise_3 is in the distributed file system
# hdfs dfs -ls

# Run MapReduce job
/usr/bin/hadoop \
    jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
    -D mapreduce.job.reduces=2 \
    -input exercise_3/ \
    -output exercise_3_output/ \
    -mapper /src/exercise_3/mapper.py \
    -reducer /src/exercise_3/reducer.py

# See content of the output folder
# hdfs dfs -ls exercise_3_output

# Upload output folder:
hdfs dfs -get exercise_3_output

# Combine and print results
cat exercise_3_output/part-* >> exercise_3_results.txt
python src/exercise_3/combiner.py
rm exercise_3_results.txt

echo $'Exercise 3 completed!'