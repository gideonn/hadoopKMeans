#!/usr/bin/bash

hdfs dfs -rm -r test/output; hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input ./cho.txt -output test/output
