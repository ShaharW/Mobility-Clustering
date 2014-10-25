'''
Created on Sep 9, 2014

@author: user
'''

def lcs(a, b):
    lengths = [[0 for j in xrange(len(b)+1)] for i in xrange(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    return lengths[len(a)][len(b)]
