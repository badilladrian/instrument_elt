from pyspark.sql import SparkSession

FILE_NAME = "example.csv"

spark = SparkSession.builder \
    .master("local") \
    .appName("py-elt") \
    .getOrCreate()

df = spark.read.csv(FILE_NAME, header=True, inferSchema=True)

# Prints out the HEAD of the given file
df.show()

spark.stop()