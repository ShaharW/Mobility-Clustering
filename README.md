# Clustering similar users by mobility behaviour

The research objective is to cluster users based on a probabilistic profiling that will represent complex mobility behavior.
One way to do so is to profile the individual's behavior by a Markovian models.
With this model we are able to capture the relationship between different time intervals in the user’s trajectory.
When using a probabilistic profiling, the distance between two users is evaluated as a distance between two distributions.
We used measures from the field of information theory, such as the Kullback-Leibler divergence, applied various clustering methods (K-medoids, Hierarchical clustering, Spectral clustering and DBSCAN) and used internal validation indices in order to find the most suitable clustering to various applications.
The used data is real and based on unique dataset.

### Folders:

 - **Clustering Methods**: algorithm used to cluster the data

 - **Internal_validity_indices**: Dunn index and Connectivity measure implemented by me

 - **Literature_methods**: distance measures from literature review

 - **My_methods**: new distance measures I'm working with