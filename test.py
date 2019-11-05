import cv2
import numpy as np
import scipy
import scipy._lib._ccallback_c
from scipy import spatial
import six 
from six.moves import cPickle as pickle
import random
import os
from string import digits

def Billateral(img):
    img = cv2.bilateralFilter(img,9,75,75)
    return img

def Median(img):
    img = cv2.medianBlur(img,5)
    return img

def sharpen(img):
    kernel_sharpening = np.array([[-1,-1,-1], 
                                [-1, 9,-1],
                                [-1,-1,-1]])# applying the sharpening kernel to the input image & displaying it.
    sharpened = cv2.filter2D(img, -1, kernel_sharpening)
    return sharpened

def GaussianBlur(img):
    img = cv2.GaussianBlur(img,(7,7),0)
    return img

def FaceRecognizion(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("../data/haarcascade_frontalface_alt.xml")
    faces = face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5);

    for x,y,w,h in faces:
        if ( (h-y)*(w*x) > 2500 ):
            img = img[y:y+h,x:x+w];
            # img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    return img

def read_image(image_path):
    img = cv2.imread(image_path,cv2.IMREAD_COLOR)
    img = FaceRecognizion(img)
    # img = sharpen(img)
    img = GaussianBlur(img)
    # img = Median(img)
    # img = Billateral(img)
    # img = sharpen(img)
    return img

# Feature extractor
def extract_features(img, vector_size=32):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    
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

def cos_cdist(sample, train):
    # getting cosine distance between search image and images database
    # v = train.reshape(1,-1)
    sample = np.array(sample).reshape(1,-1)
    train = np.array(train).reshape(1,-1)
    return scipy.spatial.distance.cdist(sample, train, 'cosine').reshape(-1)

def show_img(path):
    img = cv2.imread(path)
    cv2.imshow(path,img)

def main():

    threshold = 0.80

    sample_path = '../images/sample/'
    train_path = '../images/train/'
    # sample_path = 'MiripBanget/'
    # train_path = 'MiripBanget/'
    samples = [os.path.join(sample_path, p) for p in sorted(os.listdir(sample_path))]
    trains = [os.path.join(train_path, p) for p in sorted(os.listdir(train_path))]

    total = 0
    count = 0
    for s in samples:
        print("===========================")
        print(s)
        print("===========================")
        for t in trains:
            imgS = read_image(s)
            imgT = read_image(t)
            fS = extract_features(imgS)
            fT = extract_features(imgT)
            # print(fS)
            # print(fT)
            d = 1-cos_cdist(fS,fT)
            total += d
            count += 1

            # show_img(s)
            # show_img(t)
            nameS = s.split('/')[-1]
            nameS = nameS.translate({ord(k): None for k in digits})
            nameT = t.split('/')[-1]
            nameT = nameT.translate({ord(k): None for k in digits})
            print(t.split('/')[-1],end=' ')
            print(d,end=' ')
            if ( ((nameS == nameT) and (d > threshold)) or ((nameS != nameT) and (d < threshold)) ):
                print("--- Benar --- ")
            else:
                print("--- Salah --- ")
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
    print(f'average : {total/count}')

main()