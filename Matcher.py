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

def GaussianBlur(img):
    img = cv2.GaussianBlur(img,(7,7),0)
    return img

def FaceRecognition(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_alt.xml")
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=6);

    for x,y,w,h in faces:
        if ( (h-y)*(w*x) > 2500 ):
            img = img[y+60:y+h,x+20:x+w-20];
            # img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    return img

def read_image(image_path):
    img = cv2.imread(image_path,cv2.IMREAD_COLOR)
    img = FaceRecognition(img)
    img = GaussianBlur(img)
    return img

# Feature extractor
def extract_features(img, vector_size=32):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    try:
        # alg = cv2.ORB_create()
        alg = cv2.KAZE_create()
        kps = alg.detect(img)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        kps, dsc = alg.compute(img, kps)

        if dsc is None:
            dsc = np.zeros(32)

        dsc = dsc.flatten()
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc

class Matcher(object):
    def __init__(self, pickled_db_path="./features.pck"):
        with open(pickled_db_path,'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        vd = []
        for x in self.matrix:
            if ( not x.any() ):
                vd.append(999)
                continue
            normS = np.linalg.norm(x)
            normT = np.linalg.norm(vector)
            vd.append(1-np.dot(x,vector)/(normS*normT))
        v = np.array(vd)
        return v

    def edist(self, vector):
        # Menggunakan jarak euclidean
        vd = []
        for x in self.matrix:
            if ( not x.any() ):
                vd.append(999)
                continue
            vd.append(np.linalg.norm(x-vector))
        v = np.array(vd)
        return v

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
    # Create Matcher object
    ma = Matcher('./features.pck')

    names, match = ma.match(sample_path, alg, topn=count)

    return names, match
