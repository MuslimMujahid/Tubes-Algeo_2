import cv2
import numpy as np
import scipy
import scipy._lib._ccallback_c
from scipy import spatial
import six 
from six.moves import cPickle as pickle
import random
import os

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path,1)
    image = cv2.GaussianBlur(image,(3,3),0)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # g = 45
    # w = 250
    # for x in range(len(image)):
    #     for y in range(len(image[x])):
    #         if image[x][y] < g or image[x][y] > w:
    #             image[x][y] = 0
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


def batch_extractor(images_path, pickled_db_path="features.pck"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ('Extracting features from image %s' % f) 
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

def run():
    images_path = 'images/train/'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    batch_extractor(images_path)

run()