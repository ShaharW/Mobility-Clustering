'''
Created on Nov 20, 2014
@author: Shahar Weinstock

Connectivity internal validity measure for clustering analysis as presented in Handl & Knowls 2005

Input - Clustering labels, Distance matrix
'''

def Conn(labels,distanceMat,knn=10):
    not_match = 0.0
    for index,label in enumerate(labels):                                      # run over all objects and labels
        dist = sorted(distanceMat[index][:])                                   # sort the list of distances for the object
        for i in range(1,knn+1):             # run on the knn of the object (skip the first distance from the object itself)
            if label <> labels[list(distanceMat[index][:]).index(dist[i])]:    # if the objects are not from the same label
                not_match += 1.0/knn                                           # add 1/knn to the count
    return (1-not_match/len(labels))                                           # return the average connectivity of all objects