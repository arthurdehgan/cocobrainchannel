from sklearn.linear_model import LogisticRegression as LR, LinearRegression, BayesianRidge, TheilSenRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.ensemble import AdaBoostClassifier as ADB
from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit
from scipy.io import loadmat, savemat
import numpy as np
import os
import sys
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore")


PATH = 'data/'
if not PATH.endswith('/'):
    PATH += '/'
subject = sys.argv[1]
test = sys.argv[2]
dataf = []
labels = []

classes = test.split('_')
classe1 = classes[0] 
classe0 = classes[1] 
filetype = 'gamma'
if len(sys.argv)>4: 
    filetype = sys.argv[4]

for file in os.listdir(PATH):
    suffix = "".join(file.split('_')[1:]).split('.')[0]
    if file.startswith(subject) and suffix in classe0 + classe1: 
        print("file loaded : " + file)
        dat = loadmat(PATH + file)[filetype]
        print("of size : {}".format(dat.shape))
        if suffix[-1:] in classe0:
            data = dat
            labels += [0] * len(data)
        elif suffix[-1:] in classe1:
            data = dat
            labels += [1] * len(data)
        dataf.append(data)

dataf = np.concatenate(dataf, axis=0)

clf = ADB()
cv = StratifiedShuffleSplit(n_splits=10)
scores = cross_val_score(cv=cv,
                         estimator=clf,
                         X=dataf,
                         y=labels,
                         n_jobs=-2)

print("Decoding score in cross-val {:.2f}%".format(np.mean(scores)*100))
clf.fit(dataf, labels)
joblib.dump(clf, PATH + subject + '_' + test + '_clf.pkl') 

