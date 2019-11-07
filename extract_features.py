import cv2
import numpy as np
import scipy
import scipy._lib._ccallback_c
from scipy import spatial
import six 
from six.moves import cPickle as pickle
import random
import os

def GaussianBlur(img):
    img = cv2.GaussianBlur(img,(7,7),0)
    return img

def FaceRecognizion(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")
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
    
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        # alg = cv2.ORB_create()
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(img)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(img, kps)
        # Flatten all of them in one big vector - our feature vector

        if dsc is None:
            dsc = np.zeros(32)

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
        print (f'Extracting features from image {f}',end=" ") 
        img = read_image(f)
        
        if img is None:
            print('--- Error ---')
            continue

        name = f.split('/')[-1]
        result[name] = extract_features(img)
        # print(result[name].shape)
        print('--- Extracting success ---')
        
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

def run():
    images_path = 'images/train/'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    batch_extractor(images_path)

run()