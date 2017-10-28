#!/bin/bash

num_itr=0

rm -f stopIteration

echo "Enter the input filename"
read inputFile
echo "Copying file to HDFS now..."
hdfs dfs -put $inputFile .
echo "Copied input file to HDFS"

echo "Output will be present in test/output in HDFS"

while :
do
if [ ! -f 'stopIteration' ]; then
    echo "--------------------------------------------------------"
    echo "Not converged yet. Current Iteration #: $num_itr"
    echo "--------------------------------------------------------"
    let "num_itr++"
    hdfs dfs -rm -r test/output; hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input $inputFile -output test/output
    else
        echo "--------------------------------------------------------"
        echo "Converged after $num_itr iterations! Stopping iteration"
        echo "Classification Result (Cluster: GeneIDs):"
        echo "--------------------------------------------------------"
        cat clusterResults.txt
        echo "--------------------------------------------------------"

        break
fi
done