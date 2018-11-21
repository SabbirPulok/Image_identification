from sklearn.neural_network import MLPClassifier
#import glob, Image
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib.image as mpimg


from flask import *

from skimage import io


def convertImage(path):
    ar = io.imread(path, as_grey=True)
    return np.reshape(ar, 9025)


clf = pickle.load(open("ml.pickle", "rb"))


def get_predict(f):
    a = convertImage(f)
    result = clf.predict([a])  # out1, out2, out3 ,out4, out5, out6, out7, out8])
    # for i in range(len(result)):
    if result[0][0] == 1:
        return 'Car'
    elif result[0][1] == 1:
        return 'Moon'
    elif result[0][2] == 1:
        return 'Mountain'
    else:
        return 'I can\'t understand ur picture.'
