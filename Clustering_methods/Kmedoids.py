'''
Created on Nov 22, 2014

@author: user
'''
#!/usr/bin/env python

import numpy as np
import random

def Kmedoids(dist, k=3):

    m = dist.shape[0] # number of points
    # Pick k random medoids.
    curr_medoids = np.array([-1]*k)
    while not len(np.unique(curr_medoids)) == k:
        curr_medoids = np.array([random.randint(0, m - 1) for _ in range(k)])
    old_medoids = np.array([-1]*k) # Doesn't matter what we initialize these to.
    new_medoids = np.array([-1]*k)
   
    # Until the medoids stop updating, do the following:
    while not ((old_medoids == curr_medoids).all()):
        # Assign each point to cluster with closest medoid.
        clusters = assign_points_to_clusters(curr_medoids, dist)

        # Update cluster medoids to be lowest cost point. 
        for curr_medoid in curr_medoids:
            cluster = np.where(clusters == curr_medoid)[0]
            new_medoids[curr_medoids == curr_medoid] = compute_new_medoid(cluster, dist)

        old_medoids[:] = curr_medoids[:]
        curr_medoids[:] = new_medoids[:]
    
    sorted_medoids = sorted(list(curr_medoids))

    ret_clusters = list(sorted_medoids.index(clust) for clust in clusters)
    return ret_clusters

def assign_points_to_clusters(medoids, dist):
    dist_to_medoids = dist[:,medoids]
    return medoids[np.argmin(dist_to_medoids, axis=1)]

def compute_new_medoid(cluster, dist):
    mask = np.ones(dist.shape)
    mask[np.ix_(cluster,cluster)] = 0.
    cluster_dist = np.ma.masked_array(data=dist, mask=mask, fill_value=10e9)
    costs = cluster_dist.sum(axis=1)
    return costs.argmin(axis=0, fill_value=10e9)