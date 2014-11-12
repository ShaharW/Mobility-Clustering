'''
Created on Sep 9, 2014

@author: user
'''

import sys
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy, time, LCSS

start = time.time()
path ='C:\Users\user\workspace'
data = numpy.loadtxt(path+"\Sunday-clean.csv",delimiter = ',')
length, width = data.shape
width *= 1.0
dist = numpy.zeros((length,length))

for i in xrange(length):
    print i
    for j in xrange(i+1):
        dist[i,j] = 1-LCSS.lcs(data[i,:],data[j,:])/width
        dist[j,i] = dist[i,j]

numpy.savetxt('LCSS_distMat-Sunday.txt', dist)

end = time.time()
print "calculation time is %s seconds " %str(int(end-start))
