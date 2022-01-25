# k-means-pyspark
Explore performance of clustering algorithm with different values for k. 

## Contents
* k-means.py (Python version 3.8)
* k-means-ananlysis.md

## k-means.py
This Python file uses PySpark on a private dataset I am unable to upload to GitHub.  For this reason, I have included the results returned for most of the code because the results themself do not contain sensitive data. 

First, I apply k-means clustering to the dataset with k = 10.  After applying k-means I look at the number of observations in the first cluster, the size of each of the 10 clusters, the cost of the model, and the 10 cluster centers. 

Next, I repeat the process of applying k-means to the dataset with k = 30 and interpret the features of clustering again, as done when k = 10. 

## k-means-analysis.md
This file contains 4 questions about the results of the 2 clusterings to provide more insight on what the results tell us. 
