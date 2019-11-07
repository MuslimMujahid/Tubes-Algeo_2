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

def FaceRecognizion(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("../data/haarcascade_frontalface_alt.xml")
    faces = face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5);

    for x,y,w,h in faces:
        if ( (h-y)*(w*x) > 2500 ):
            img = img[y+60:y+h,x+20:x+w-20];
            # img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    return img

def read_image(image_path):
    img = cv2.imread(image_path,cv2.IMREAD_COLOR)
    img = FaceRecognizion(img)
    img = GaussianBlur(img)
    return img

# Feature extractor
def extract_features(img, vector_size=32):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    orb = cv2.ORB_create()
    kps = orb.detect(img,None)
    kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
    kps, dsc = orb.compute(img,kps)
    
    if dsc is None:
        return None
        
    dsc = dsc.flatten()
    needed_size = (vector_size * 64)
    if dsc.size < needed_size:
        dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)]) 

    return dsc

class Matcher(object):
    
    def __init__(self, pickled_db_path="features.pck"):
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
        v = vector.reshape(1,-1)
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)

    def match(self, image_path, topn=5):
        img = read_image(image_path)
        features = extract_features(img)
        img_distances = self.cos_cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()
        return nearest_img_paths, img_distances[nearest_ids].tolist()

def show_img(path):
    img = cv2.imread(path)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img)
    cv2.imshow(path,img)
    print(img.shape)

def run():
    sample_path = 'images/sample/'
    train_path = 'images/train/'
    sample = [os.path.join(sample_path, p) for p in sorted(os.listdir(sample_path))]
    train = [os.path.join(train_path, p) for p in sorted(os.listdir(train_path))]

    ma = Matcher('features.pck')

    for s in sample:
        print ('Query image ==========================================')
        print('image : %s' % s)
        # show_img(s)
        names, match = ma.match(s, topn=5)
        print ('Result images ========================================')
        for i in range(5):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtruct it from 1 to get match value
            print (f'Match {(1-match[i])} - {names[i]} - {i+1}') 
            show_img(s)
            show_img(os.path.join(train_path, names[i]))
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

run()