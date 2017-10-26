#!/usr/bin/env bash


hadoop jar /usr/local/Cellar/hadoop/2.7.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/601cse/cho.txt -output /user/601cse/choOutput
