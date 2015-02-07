'''
Created on Jan 27, 2015

@author: Shahar Weinstock
'''

import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
from scipy import stats

''' This is the main function that measures the average entropy '''
def evaluation(data,labels,seq_size=2):
    #===========================================================================
    # ''' total entropy '''
    # entropy = 0.0
    # x_labels = np.zeros(len(labels))
    # clus = cluster(0,x_labels,data,seq_size)
    # entropy = clus.prop*clus.entropy
    # print "entropy before clustering is - " + str(entropy)
    #===========================================================================
    
    ''' entropy after clustering '''
    entropy = 0.0
    clusters = int(max(labels)+1)
    for i in range(clusters):
        clus = cluster(i,labels,data,seq_size)
        entropy += clus.prop*clus.entropy
    return entropy
        

''' Cluster class '''        
class cluster:
    def __init__(self,number,labels,data,seq_size):
        self.number = number
        self.old_seq_len = data.shape[1]
        self.size = self.get_cluster_size(labels)
        self.prop = self.size/(len(labels)*1.0)
        self.instances = self.get_cluster_data(data,labels)
        self.code = self.instances_to_code(seq_size)
        self.entropy = self.calc_entropy()
        
    def get_cluster_size(self,labels):
        k = max(set(labels))
        return np.histogram(labels,bins=np.arange(k+1))[0][self.number]

    def get_cluster_data(self,data,labels):
        m = data.shape[0]
        j = 0
        cluster_data = np.zeros((self.size,self.old_seq_len))
        for i in range(m):
            if labels[i] == self.number:
                cluster_data[j] = data[i][:]
                j += 1
        return cluster_data
    
    def instances_to_code(self,seq_size):
        if self.size == 0:
            return None
        m = self.size*(self.old_seq_len+1-seq_size)
        splitted_data = np.zeros((m,seq_size))
        code = np.zeros(m)
        row = 0
        for i in range(self.size):
            for j in range(self.old_seq_len+1-seq_size):
                splitted_data[row][:] = self.instances[i][j:j+seq_size]
                row += 1

        for l in range(m):
            for k in range(seq_size):
                code[l] += (10**k)*splitted_data[l][k]
        return code
    
    def calc_entropy(self):
        if self.size == 0:
            return 0
        k = max(set(self.code))
        hist = np.histogram(self.code,bins = np.arange(k+1))[0]
        return stats.entropy(hist,base=2)
