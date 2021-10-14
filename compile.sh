#!/bin/bash

python3 data_pagerank.py

echo "Creating folder and upload files"
/usr/lib/hadoop-3.3.0/bin/hdfs dfs -mkdir input
/usr/lib/hadoop-3.3.0/bin/hdfs dfs -put static/corpus/* input

echo "Calculating inverted index"
hadoop jar hadoop-streaming.jar -input input -output output -mapper invertedIndexMapper.py -reducer invertedIndexReducer.py 

echo "Download results"

hadoop jar hadoop-streaming.jar -Dmapred.reduce.tasks=1 -input output -output result -mapper cat -reducer cat

/usr/lib/hadoop-3.3.0/bin/hdfs dfs -get result/part-00000

echo "Creating folder and upload files for pagerank"
/usr/lib/hadoop-3.3.0/bin/hdfs dfs -mkdir input2
/usr/lib/hadoop-3.3.0/bin/hdfs dfs -put pagerank.txt input2

echo "Calculating pagerank"
hadoop jar hadoop-streaming.jar -input input2 -output output2 -mapper pagerankMapper.py -reducer pagerankReducer.py 

echo "Download results"
hadoop jar hadoop-streaming.jar -Dmapred.reduce.tasks=1 -input output2 -output result2 -mapper cat -reducer cat

echo "Calculating pagerank"
hadoop jar hadoop-streaming.jar -input result2/part-00000 -output output3 -mapper rank_map.py 

hadoop jar hadoop-streaming.jar -Dmapred.reduce.tasks=1 -input output3 -output result3 -mapper cat -reducer cat

hadoop fs -mv result3/part-00000 result3/part-00001
/usr/lib/hadoop-3.3.0/bin/hdfs dfs -get result3/part-00001

echo "Starting the server"
python server.py


