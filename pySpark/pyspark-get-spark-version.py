from pyspark import SparkConf, SparkContext
import os

#os.environ['PYSPARK_PYTHON'] = r'C:\\Users\\Developer\\anaconda3'
#os.environ['PYSPARK_DRIVER_PYTHON'] = r'C:\\Users\\Developer\\anaconda3'

conf = SparkConf().setAppName("Remote-Trial").setMaster("local")

sc = SparkContext(conf=conf)

data = [1,2,3,4,5]
rdd = sc.parallelize(data)
squared = rdd.map(lambda x: x*x).collect()

print(squared)