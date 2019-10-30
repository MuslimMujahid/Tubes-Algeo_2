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

# Feature extractor
def extract_features(image_path, vector_size=32):
    # image = imread(image_path, mode="RGB")
    image = cv2.imread(image_path,1)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
    
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None

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

    def cdist(self, vector):
        # Menggunakan jarak euclidean
        vd = []
        for i in range(len(self.matrix)):
            dq = 0
            for j in range(len(vector)):
                dq += (self.matrix[i][j] - vector[j])**2
            vd.append(dq**.5)
        v = np.array(vd)
        return v.reshape(-1)

    def match(self, image_path, topn=5):
        features = extract_features(image_path)
        img_distances = self.cdist(features)
        # getting top 5 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()
        nearest_img_paths = self.names[nearest_ids].tolist()
        return nearest_img_paths, img_distances[nearest_ids].tolist()

def show_img(path):
    img = cv2.imread(path)
    cv2.imshow(path,img)

def run():
    sample_path = 'images/sample/'
    train_path = 'images/train/'
    sample = [os.path.join(sample_path, p) for p in sorted(os.listdir(sample_path))]
    train = [os.path.join(train_path, p) for p in sorted(os.listdir(train_path))]

    ma = Matcher('features.pck')

    file = random.sample(sample,10) #ambil 10 foto acak dari sampel
    for s in file:
        print ('Query image ==========================================')
        # show_img(s)
        print('\n' + s + '\n')
        print ('Result images ========================================')
        names, match = ma.match(s, topn=5)
        print()
        for i in range(5):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtruct it from 1 to get match value
            print (names[i], match[i])
            show_img(os.path.join(train_path, names[i]))
        print()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

run()