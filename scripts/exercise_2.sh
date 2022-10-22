#!/bin/bash

# Delete data if already exists
hdfs dfs -test -e exercise_2 && hdfs dfs -rm -r exercise_2

# Delete output directory if already exists
hdfs dfs -test -e exercise_2_output && hdfs dfs -rm -r exercise_2_output
rm -rf exercise_2_output

# Place exercise_2 in the distributed file system
hdfs dfs -put /data/exercise_2

# Check that exercise_2 is in the distributed file system
# hdfs dfs -ls

# Run MapReduce job
/usr/bin/hadoop \
    jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
    -D mapreduce.job.reduces=2 \
    -input exercise_2/ \
    -output exercise_2_output/ \
    -mapper /src/exercise_2/mapper.py \
    -reducer /src/exercise_2/reducer.py

# See content of the output folder
# hdfs dfs -ls exercise_2_output

# Upload output folder:
hdfs dfs -get exercise_2_output

# Combine and print results
cat exercise_2_output/part-* >> exercise_2_results.txt
python src/exercise_2/combiner.py
rm exercise_2_results.txt

echo $'Exercise 2 completed!'