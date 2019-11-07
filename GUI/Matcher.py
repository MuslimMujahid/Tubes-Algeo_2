import cv2
import numpy as np
import scipy
import scipy._lib._ccallback_c
from scipy import spatial
import six
from six.moves import cPickle as pickle
import random
import os
import matplotlib.pyplot as plt

def FaceRecognition(img):
    face_cascade = cv2.CascadeClassifier("../data/haarcascade_frontalface_alt.xml")
    faces = face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5);

    for x,y,w,h in faces:
        if ( (h-y)*(w*x) > 2500 ):
            img = img[y:y+h,x:x+w];
    return img;

# Feature extractor
def extract_features(img, vector_size=32):
    img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    img = FaceRecognition(img)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    try:
        alg = cv2.KAZE_create()
        kps = alg.detect(img)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        kps, dsc = alg.compute(img,kps)
        dsc = dsc.flatten()
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])

    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc

class Matcher(object):
    def __init__(self, pickled_db_path="../features.pck"):
        with open(pickled_db_path,'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            ns = k.split('-')
            self.size = ns[1].split('x')
            self.names.append(ns[0])
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        v = vector.reshape(1,-1)
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)

    def edist(self, vector):
        # Menggunakan jarak euclidean
        vd = []
        for i in range(len(self.matrix)):
            dq = 0
            for j in range(len(vector)):
                dq += (self.matrix[i][j] - vector[j])**2
            vd.append(dq**.5)
        v = np.array(vd)
        return v.reshape(-1)

    def match(self, image_path, alg, topn=6):
        img = read_image(image_path)
        features = extract_features(img)
        if (alg == "Cosine Similarity"):
            img_distances = self.cos_cdist(features)
        elif (alg =="Distance Euclidean"):
            img_distances = self.edist(features)
        # getting top 6 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()
        return nearest_img_paths, img_distances[nearest_ids].tolist()

def run(sample_path, train_path, alg, count):
    files = [os.path.join(train_path, p) for p in sorted(os.listdir(train_path))]
    # getting 3 random images
    # sample = random.sample(files, 3)
    ma = Matcher('../features.pck')

    names, match = ma.match(sample_path, alg, topn=count)

    return names, match

    # s = sample[0]
    # names, match = ma.match(s, 10)
    # return sample,names, match

    # for s in sample:
    #     names, match = ma.match(s, topn=3)
    #     for i in range(3):
    #         # we got cosine distance, less cosine distance between vectors
    #         # more they similar, thus we subtruct it from 1 to get match value
    #         print('Match %s' % (1-match[i]))
    #         picture = Picture(source = os.path.join(images_path, names[i]))
