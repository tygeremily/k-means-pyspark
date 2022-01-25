### Describe what the cluster center for the largest cluster when k = 10 indicates about the scanners in this group.
The largest cluster is Cluster 1, 34402, and based on the output for this cluster the scanners "total_lifetime" are the strongest in this cluster by over 700. However, 828.755 is the lowest value for total lifetime across all 10 clusters and "num_ports_scanned" and "avg_lifetime" are also the smallest values across all clusters. The only value in this cluster compared to all other clusters that is the largest is "avg_pkt_size".

### Describe what the cluster center for the second largest cluster when k = 10 indicates about the scanners in this group. 
Cluster 8 is the second largest, 2023 and the cluster center indicates the scanners in this group have the second smallest value for "num_ports_scanned", and the Cluster 1, the largest cluster, has the smallest value. This cluster shows me it is following the pattern of Cluster 1 where the second smallest values across all clusters are "num_ports_scanned", "avg_lifetime" and "total_lifetime"; and the second largest "avg_pkt_size" across all clusters. This pattern is probably correlated to the size of the cluster.

### Compare the cost of the results of k = 10 and k = 30.
Cost for k = 30 is 13,614,992,603 and cost for k = 10 is 153,474,484,645. k=30 is smaller than k=10, and we want cost to be low, in this case it seems high for both models partially because the dataset has a wide range of distribution across features. So when the wide range is clustered, there can still be a wide distribution.

### Compare the top two clusters generated when k = 30 with the top two clusters generated when k = 10. 
The top 2 clusters for k = 10 is Cluster 1 (34402) and Cluster 8 (2023) and the top 2 for k = 30 is Cluster 14 (16140) and Cluster 1 (8134). The first thing I noticed was that the pattern I observed across the features for k=10 was not true for k=30. Additionally, the distribution of the size of each cluster for k=10 was better distributed than k=30 with higher numbers for the largest cluster and more sizes of 1 and 3.
