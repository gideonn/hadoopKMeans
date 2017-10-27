#!/bin/bash

num_itr=0
while :
do
if [ ! -f 'stopIteration' ]; then
    echo "Not converged yet. Current Iteration #: $num_itr"
    let "num_itr++"
    hdfs dfs -rm -r test/output; hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input ./cho.txt -output test/output
    else
        echo "Converged after $num_itr iterations! Stopping iteration"
        break
fi
done