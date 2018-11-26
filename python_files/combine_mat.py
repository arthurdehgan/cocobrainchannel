from scipy.io import loadmat, savemat
import os
import sys
import numpy as np


PATH = 'data/'
if not PATH.endswith('/'):
    PATH += '/'
SUB = sys.argv[1]

data = []
for file in os.listdir(PATH):
    if SUB in file and file.endswith('.mat') and 'raw' in file and not 'pred' in file:
        data.append(loadmat(PATH + file)['raw'])
        os.remove(PATH + file)

data = np.concatenate(data)
filename = PATH + SUB + '_all.mat'
savemat(filename, {'data': data})
