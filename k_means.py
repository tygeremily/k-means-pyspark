# -*- coding: utf-8 -*-
"""k-means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZCMglvvPwg2V22xAJmhjKJMjgsel3ulE
"""

import pyspark
import csv

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.sql.functions import col, column
from pyspark.sql.functions import expr
from pyspark.sql.functions import split
from pyspark.sql import Row
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, IndexToString
from pyspark.ml.clustering import KMeans

ss = SparkSession.builder.master("local").appName("FrequentPortSet").getOrCreate()
Scanners_df = ss.read.csv("/storage/home/emt5337/scanners-dataset1-anon.csv", header= True, inferSchema=True )

# use printSchema() to display Scanners_df to see if it is inferred correctly
Scanners_df.printSchema()


# k = 10

# use kmeans to cluster the scanners who scan the top 3 port-sets 
# below i will use k = 10 for input features: num_ports_scanned, avg_lifetime, total_lifetime, _avg_pkt_size
km = KMeans(featuresCol="features", predictionCol="prediction").setK(10).setSeed(123)
km.explainParams() # get info on parameters of KMeans()
va = VectorAssembler().setInputCols(["num_ports_scanned", "avg_lifetime", "total_lifetime", "avg_pkt_size"]).setOutputCol("features")
Scanners_df.printSchema()

data= va.transform(Scanners_df)
data.persist() #returns the features and their types

# fit the data 
kmModel=km.fit(data)
kmModel
#returns KMeans_876facf152e0

predictions = kmModel.transform(data)
predictions.persist().show(3)

#interpret the features of the first cluster 
Cluster1_df=predictions.where(col("prediction")==0)
Cluster1_df.persist().count()
# returns 34402

summary = kmModel.summary
# get the size of each cluster (k=10)
summary.clusterSizes
# returns [34402, 66, 10, 1, 6, 1, 5, 2023, 2, 5]

# calculate the cost of the model 
kmModel.computeCost(data)
# 153474484645

# find the cluster centers
centers = kmModel.clusterCenters()
print("Cluster Centers:")
i=0
for center in centers:
    print("Cluster ", str(i+1), center)
    i = i+1
# returns Cluster Centers:
# Cluster  1 [   1.95750247  123.66807953  828.75507238   63.89789694]
# Cluster  2 [  9.89803030e+02   1.36473191e+02   5.66942591e+05   6.00475613e+01]
# Cluster  3 [  3.35000000e+02   4.88717956e+02   1.01579620e+06   6.30591387e+01]
# Cluster  4 [  8.82000000e+02   4.68035343e+02   2.47637500e+06   6.00000000e+01]
# Cluster  5 [  3.50666667e+02   5.34694252e+02   1.13566783e+06   6.25721338e+01]
# Cluster  6 [  8.82000000e+02   3.61846931e+02   1.89824900e+06   6.00000000e+01]
# Cluster  7 [  3.07400000e+02   4.13538958e+02   7.53811800e+05   6.25134090e+01]
# Cluster  8 [  5.09985171e+00   4.15758561e+02   8.83154721e+03   6.06091191e+01]
# Cluster  9 [  9.35000000e+01   5.45746822e+02   3.02089000e+05   6.00000000e+01]
# Cluster  10 [  3.72000000e+01   5.95986273e+02   1.33023000e+05   6.00000000e+01]



# k = 30 

# change the value of k 
km30 = KMeans(featuresCol="features", predictionCol="prediction").setK(30).setSeed(123)
kmModel2=km30.fit(data)

summary2 = kmModel2.summary
summary2

# find the size of each of the 30 clusters
summary2.clusterSizes
# returns [8134, 41, 1, 1, 3, 1, 2, 523, 5, 297, 2, 6, 3, 16140, 
# 1, 1, 5, 2940, 1, 358, 104, 3, 21, 986, 6, 2850, 1, 4066, 3, 16]

# compute the cost of running k = 30
kmModel2.computeCost(data)
# returns 13614992603

# find cluster centers for new value of k 
centers2 = kmModel2.clusterCenters()

print("Cluster Centers:")
i=0
for center in centers2:
    print("Cluster ", str(i+1), center)
    i = i+1
# returns Cluster Centers:
# Cluster  1 [   2.29502762  121.04236539  600.90079804   62.81110245]
# Cluster  2 [  1.01256098e+03   1.26304418e+02   5.61209171e+05   6.00000000e+01]
# Cluster  3 [  3.48000000e+02   5.21447255e+02   1.09243200e+06   6.31905628e+01]
# Cluster  4 [  8.82000000e+02   4.68035343e+02   2.47637500e+06   6.00000000e+01]
# Cluster  5 [  3.37666667e+02   4.80514008e+02   9.99513333e+05   6.31156097e+01]
# Cluster  6 [  8.82000000e+02   3.61846931e+02   1.89824900e+06   6.00000000e+01]
# Cluster  7 [  3.31500000e+02   3.98596781e+02   8.16748500e+05   6.28152986e+01]
# Cluster  8 [  3.58587786e+00   3.46800315e+02   4.81215076e+03   6.12412625e+01]
# Cluster  9 [  3.72000000e+01   5.95986273e+02   1.33023000e+05   6.00000000e+01]
# Cluster  10 [  8.15646259e+00   3.33027735e+02   1.26802619e+04   6.02832102e+01]
# Cluster  11 [  9.35000000e+01   5.45746822e+02   3.02089000e+05   6.00000000e+01]
# Cluster  12 [  3.33000000e+02   5.01668997e+02   1.04280167e+06   6.30473804e+01]
# Cluster  13 [  7.86333333e+02   1.88775759e+02   6.02053667e+05   6.10463492e+01]
# Cluster  14 [  1.6738001   19.49566177  61.82712766  65.91055601]
# Cluster  15 [  3.33000000e+02   5.32676598e+02   1.10850000e+06   6.31931309e+01]
# Cluster  16 [  1.89000000e+02   5.76174645e+02   6.49925000e+05   6.00000000e+01]
# Cluster  17 [  1.01260000e+03   1.22692701e+02   5.41344600e+05   6.00000000e+01]
# Cluster  18 [  1.90753425e+00   2.79692493e+02   2.29978116e+03   6.12390930e+01]
# Cluster  19 [  4.26000000e+02   5.15161620e+02   1.20805400e+06   6.00000000e+01]
# Cluster  20 [  5.71944444e+00   3.50555895e+02   9.92391389e+03   6.04854332e+01]
# Cluster  21 [  8.66346154e+00   4.55771008e+02   1.83098654e+04   6.22254162e+01]
# Cluster  22 [  3.32333333e+02   5.46293347e+02   1.13500700e+06   6.30163697e+01]
# Cluster  23 [  1.18571429e+01   4.91333152e+02   3.16634286e+04   6.55238095e+01]
# Cluster  24 [  3.70964467e+00   4.68181907e+02   6.44486599e+03   6.03238797e+01]
# Cluster  25 [  1.75000000e+01   5.17370421e+02   5.32331667e+04   6.23333333e+01]
# Cluster  26 [  2.26779422e+00   4.55788926e+02   3.24987209e+03   6.14672139e+01]
# Cluster  27 [  3.39000000e+02   4.35623552e+02   9.02612000e+05   6.29602753e+01]
# Cluster  28 [    2.13128079   186.29720239  1351.15098522    61.84689381]
# Cluster  29 [  2.91333333e+02   4.23500408e+02   7.11854000e+05   6.23121493e+01]
# Cluster  30 [  1.01256250e+03   1.29549004e+02   5.77864125e+05   6.00000000e+01]