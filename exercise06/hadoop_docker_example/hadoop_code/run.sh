






rm -r out
rm -r sorted_out
rm -r hdfs
mkdir hdfs

hdfs dfs -put inpt.txt hdfs/inpt.txt
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.5.jar \
    -files mapper.py \
    -mapper "python3 mapper.py" \
    -file reducer.py \
    -reducer "python3 reducer.py" \
    -input hdfs/inpt.txt \
    -output out
cat out/part-00000

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.5.jar \
    -files secondmapper.py \
    -mapper "python3 secondmapper.py" \
    -file secondreducer.py \
    -reducer "python3 secondreducer.py" \
    -input out/part-00000 \
    -output sorted_out | awk '{print "\033[0;32m" $0 "\033[0m"}'

#cat sorted_out/part-00000
echo "First 10 lines:"
head -n 10 sorted_out/part-00000
echo "Last 10 lines:"
tail -n 10 sorted_out/part-00000