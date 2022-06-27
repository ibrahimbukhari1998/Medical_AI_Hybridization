import random
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np
from keras import backend as K
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
from sklearn.metrics import roc_auc_score, roc_curve
from tensorflow.compat.v1.logging import INFO, set_verbosity
import os
from keras.models import load_model
import pandas as pd



# LABELS
labels = ['Cardiomegaly', 
        'Emphysema', 
        'Effusion', 
        'Hernia', 
        'Infiltration', 
        'Mass', 
        'Nodule', 
        'Atelectasis',
        'Pneumothorax',
        'Pleural_Thickening', 
        'Pneumonia', 
        'Fibrosis', 
        'Edema', 
        'Consolidation']



# PREPING IMAGES
random.seed(a=None, version=2)

set_verbosity(INFO)


def get_mean_std_per_batch(image_dir, df, H=320, W=320):
    sample_data = []
    for img in df.sample(100)["Image"].values:
        image_path = os.path.join(image_dir, img)
        sample_data.append(
            np.array(tf.keras.utils.load_img(image_path, target_size=(H, W))))

    mean = np.mean(sample_data, axis=(0, 1, 2, 3))
    std = np.std(sample_data, axis=(0, 1, 2, 3), ddof=1)
    return mean, std


def load_image(img, image_dir, df, preprocess=True, H=320, W=320):
    """Load and preprocess image."""
    mean, std = get_mean_std_per_batch(image_dir, df, H=H, W=W)
    img_path = os.path.join(image_dir, img)
    x = tf.keras.utils.load_img(img_path, target_size=(H, W))
    if preprocess:
        x -= mean
        x /= std
        x = np.expand_dims(x, axis=0)
    return x


# MODEL LOADING 
mcnn = load_model("multiLabel.h5", compile=False)



# MODEL PREDICT
def Classify(img):
    df = pd.read_csv("train-small.csv")
    basedir = Path(__file__).resolve().parent.parent
    tmp = img.split("/")
    imgname = tmp[-1]
    
    imgdir = str(basedir)+"/media/temp"
    
    preprocessed_input = load_image(imgname, imgdir, df)
    pred = mcnn.predict(preprocessed_input)
    max_prob = pred[0].max()
    
    if max_prob >= 0.65:
        
        i=0
        for prob in pred[0]:
            
            if(prob == max_prob):
                likelihood = round(prob*100, 2)
                return {"label":labels[i], "prob":likelihood}
            
            i=i+1
        
        
    else:
        return {"label":'None', "prob":0}
    
    


