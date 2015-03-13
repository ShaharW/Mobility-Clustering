'''
Created on Oct 30, 2014

@author: Shahar Weinstock
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np

def Dunn(labels,distanceMat):
    k = int(max(labels)+1)
    clusters = [cluster(count,labels,distanceMat) for count in xrange(k)]
    return min_inter_distance(k,labels,distanceMat,clusters)/max_intra_distance(k,labels,distanceMat,clusters)

def max_intra_distance(k,labels,distanceMat,clusters):
    intra_distances = []
    for i in range(k):
            intra_distances.append(clusters[i].max_intra)
    return max(intra_distances)

def inter_cluster_distance(cluster1, cluster2, labels, distanceMat):
    dist = 0.0
    if cluster1.size == 0 or cluster2.size == 0:
        return float('Inf')
    for i in cluster1.instances:
        for j in cluster2.instances:
            dist += distanceMat[i][j]
    return dist/(cluster1.size*cluster2.size)   

def min_inter_distance(k,labels,distanceMat,clusters):
    inter_distances = []
    for i in range(k):
        for j in range(i+1,k):
            inter_distances.append(inter_cluster_distance(clusters[i], clusters[j], labels, distanceMat))
    return min(inter_distances)

''' Cluster class '''        
class cluster:
    def __init__(self,number,labels,distanceMat):
        self.number = number
        self.size = self.get_cluster_size(labels)
        self.instances = self.get_cluster_data(labels)
        self.max_intra = self.intra_cluster_distance(labels,distanceMat)
        
    def get_cluster_size(self,labels):
        k = int(max(labels)+1)
        return np.histogram(labels,bins=np.arange(k+1))[0][self.number]
    
    def get_cluster_data(self,labels):
        if self.size == 0:
            return None
        m = len(labels)
        j = 0
        cluster_data = np.zeros((self.size))
        for i in range(m):
            if labels[i] == self.number:
                cluster_data[j] = i
                j += 1
        return cluster_data

    def intra_cluster_distance(self, labels, distanceMat):
        dist = 0.0
        if self.size == 0:
            return 0
        for i in range(self.size):
            for j in range(i+1,self.size):
                dist += distanceMat[self.instances[i]][self.instances[j]]
        return dist/((self.size)*(self.size-1)*0.5)