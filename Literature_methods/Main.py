'''
Created on Oct 26, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import Kmeans, numpy as np

name = '\LCSS_Kmeans'
dist_name = '\LCSS_distMat.txt'
data_name = '\RoutineLocation_int.txt'
path = 'C:\Users\user\workspace\Results' 
if not os.path.exists(path+name):os.makedirs(path+name)

'''***************Load data***************'''
##################################################################
path ='C:\Users\user\workspace'

start = time.time()
dist = np.loadtxt(path+'\Results'+dist_name,delimiter = ' ')  # @UndefinedVariable
data = np.loadtxt(path+data_name,delimiter = ',')  # @UndefinedVariable

end = time.time()
print "load time is %s seconds " %str(int(end-start))
##################################################################

for k in range(2,16):
    labels = Kmeans.Kmeans(dist, data, k)
    np.savetxt(path+'\Results'+name+'\k='+str(k)+'-means.txt', labels)  # @UndefinedVariable
    
