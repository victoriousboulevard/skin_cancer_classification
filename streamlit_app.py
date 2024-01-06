import streamlit as st
from streamlit_option_menu import option_menu
#from tf.keras.model import load_model
#import cv2

#import os

import numpy as np

#import pickle

import tensorflow as tf

from tensorflow.keras import layers

from tensorflow.keras import models,utils

import pandas as pd

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import load_img,img_to_array

from tensorflow.python.keras import utils

model1 = load_model('model_EfficientNetV2B0.h5')
model2 = load_model('model_EfficientNetV2B1.h5')
model3 = load_model('model_EfficientNetV2S.h5')

def load_image(image): # here image is file name
  #img = load_img(image, target_size=(256,256))

  img = img_to_array(image)

  img= tf.image.resize(img,(224,224))

  img = np.expand_dims(img,axis = 0)


  return img


#functions


def detect_skin_cancer(model_type, image):
  img = load_image(image)
  class_dict = {0:'AKIEC',  1: 'BCC', 2:'BKL', 3:'DF', 4:'MEL', 5:'NV', 6:'VASC'}
  if model_type == 'EfficientV2B0':
    predict = np.argmax(model1.predict(img))
    #st.text( str(model_type)+' selected ')
    st.text(class_dict[predict])
  elif model_type == 'EfficientV2B1':
    #st.text(str(model_type)+ ' selected ')
    predict = np.argmax(model2.predict(img))
    st.text(class_dict[predict])
  else:
  #st.text(str(model_type)+' selected ')
    predict = np.argmax(model3.predict(img))
    st.text(class_dict[predict])



def generate_prediction(image):
  from PIL import Image
  uploaded_image = image
  #uploaded_image = st.file_uploader("Upload an Image")

  # text over upload button "Upload an Image"

  if uploaded_image:

      # display the image

      display_image = Image.open(uploaded_image)

      st.image(display_image)
      model_type = st.radio("Choose a classifier",
      ["***EfficientV2B0***", "***EfficientV2B1***", "***EfficientV2S***"],horizontal =True)
      if model_type:
        detect_button = st.button('Classify')
        if detect_button:
          detect_skin_cancer(model_type,display_image)


#side bar to show options
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Detector'],
        icons=['house', 'thermometer'], menu_icon="cast",
         default_index=0)
    selected

if selected == 'Home':
  st.text_area('Skin cancer occurs when skin cells are damaged, for example, by overexposure toultraviolet (UV) radiation from the sun.')


if selected == 'Detector':
  st.title('Skin Cancer Classification')
  uploaded_image = st.file_uploader("Upload an Image")
  generate_prediction(uploaded_image)
