'''
Created on Oct 30, 2014

@author: user
'''

def cluster_size(cluster,labels):
    size = 0
    for l in labels:
        if l == cluster:
            size += 1
    return size

def intra_cluster_distance(cluster, labels, distanceMat):
    dist = 0.0
    size = cluster_size(cluster,labels)
    for i in range(len(labels)):
        if labels[i] == cluster:
            for j in range(i+1,len(labels)):
                if labels[j] == cluster:
                    dist += distanceMat[i][j]
    if dist == 0:
        print ("The cluster has only one element")
    return dist/((size)*(size-1)*0.5)

def inter_cluster_distance(cluster1, cluster2, labels, distanceMat):
    dist = 0.0
    for i in range(len(labels)):
        if labels[i] == cluster1:
            for j in range(len(labels)):
                if labels[j] == cluster2:
                    dist += distanceMat[i][j]
    return dist/(cluster_size(cluster1,labels)*cluster_size(cluster2,labels))   

def min_inter_distance(k,labels,distanceMat):
    inter_distances = []
    for i in range(k):
            for j in range(i+1,k):
                inter_distances.append(inter_cluster_distance(i, j, labels, distanceMat))
    return min(inter_distances)

def max_intra_distance(k,labels,distanceMat):
    intra_distances = []
    for i in range(k):
            intra_distances.append(intra_cluster_distance(i, labels, distanceMat))
    return max(intra_distances)

def Dunn(labels,distanceMat):
    return min_inter_distance(len(set(labels)),labels,distanceMat)/max_intra_distance(len(set(labels)),labels,distanceMat)

        