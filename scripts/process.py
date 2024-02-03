from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType
import pyspark.pandas as ps
import os

"""
This is an injectable script to the docker strategy.
Most of the time-investment was upon R&D to design 
a full-bateries easy to run strategy that can scale.

This now working-- can be Pythonistic on a feature-brach
"""

# Init vars
FILE_NAME = "example.csv"
START_DATE = "01-Nov-2014"
END_DATE = "30-Nov-2014"

# Converting panda datetime object
START_DATE = ps.to_datetime(START_DATE, format='%d-%b-%Y')
END_DATE = ps.to_datetime(END_DATE, format='%d-%b-%Y')

# Create a spark session
spark = SparkSession.builder \
    .master("local") \
    .appName("py-elt") \
    .getOrCreate()

# Define the schema of the input data
schema = StructType([
    StructField("NAME", StringType(), True),
    StructField("DATE", StringType(), True),
    StructField("VALUE", FloatType(), True)
])

df = spark.read.csv(FILE_NAME,
                    header=True, 
                    schema=schema)
df.cache()                  
psdf = df.pandas_api()      

# Converting the DATE column to a DateType
psdf["DATE"] = ps.to_datetime(psdf["DATE"], format='%d-%b-%Y')

# INSTRUMENT1
ins_1 = psdf[psdf["NAME"] == "INSTRUMENT1"]

# INSTRUMENT2
ins_2 = psdf[(psdf["NAME"] == "INSTRUMENT2") & 
            (psdf["DATE"] >= START_DATE) & 
            (psdf["DATE"] <= END_DATE)]

# INSTRUMENT3
ins_3 = psdf[psdf["NAME"] == "INSTRUMENT3"]

# Calculating the results
ins_1_result = ins_1["VALUE"].mean()
ins_2_result = ins_2["VALUE"].mean()
ins_3_result = ins_3["VALUE"].max()

# Printing the results
print(f"INSTRUMENT1 MEAN: {ins_1_result}")
print(f"INSTRUMENT2 MEAN (NOV 2014): {ins_2_result}")
print(f"INSTRUMENT3 MAX: {ins_3_result}")

# TODO the SQL multiplier has been resolved on the develop branch
# ! Alongside with error handling, logging and other features as calculations classes etc...

# Saving the results
# The use of cat on p*.csv is to merge the partitions into a single file
ins_1.to_csv(path=r'%s/output/instrument1', header=False)
os.system("cat %s/output/instrument1/p*.csv > instrument1.csv")
ins_2.to_csv(path=r'%s/output/instrument2', header=False)
os.system("cat %s/output/instrument2/p*.csv > instrument2.csv")
ins_3.to_csv(path=r'%s/output/instrument3', header=False)
os.system("cat %s/output/instrument3/p*.csv > instrument3.csv")

# stop node
spark.stop()
