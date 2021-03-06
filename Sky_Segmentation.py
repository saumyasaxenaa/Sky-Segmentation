# -*- coding: utf-8 -*-
"""Proj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QXWvzlDLb69QOaGSGUaR-7KcPMiiK09P
"""

!pip install keras-segmentation
from google.colab import drive
from keras.layers import Input, Conv2D, Dropout, MaxPooling2D, UpSampling2D, concatenate
from keras_segmentation.models.model_utils import get_segmentation_model

drive.mount("/content/drive")
train_x_filepath = "drive/Shared drives/Data Mining Project/Data/train_x/"
train_y_filepath = "drive/Shared drives/Data Mining Project/Data/train_y/"
test_x_filepath = "drive/Shared drives/Data Mining Project/Data/test_x/"
test_y_filepath = "drive/Shared drives/Data Mining Project/Data/test_y/"
checkpoints_filepath = "drive/Shared drives/Data Mining Project/Data/checkpoints/CNN"
example1 = "drive/My Drive/Data Mining/Project Edge Cases/Sky Segmentation/example1.jpg"
example2 = "drive/My Drive/Data Mining/Project Edge Cases/Sky Segmentation/example2.jpg"

img_input = Input(shape=(480, 640, 3))
conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(img_input)
conv1 = Dropout(0.2)(conv1)
conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv1)
pool1 = MaxPooling2D((2, 2))(conv1)
conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool1)
conv2 = Dropout(0.2)(conv2)
conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv2)
pool2 = MaxPooling2D((2, 2))(conv2)
conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(pool2)
conv3 = Dropout(0.2)(conv3)
conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv3)
up1 = concatenate([UpSampling2D((2, 2))(conv3), conv2], axis=-1)
conv4 = Conv2D(64, (3, 3), activation='relu', padding='same')(up1)
conv4 = Dropout(0.2)(conv4)
conv4 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv4)
up2 = concatenate([UpSampling2D((2, 2))(conv4), conv1], axis=-1)
conv5 = Conv2D(32, (3, 3), activation='relu', padding='same')(up2)
conv5 = Dropout(0.2)(conv5)
conv5 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv5)
out = Conv2D(256, (1, 1), padding='same')(conv5)
CNN_model = get_segmentation_model(img_input, out)
CNN_model.train( 
    train_images = train_x_filepath,
    train_annotations = train_y_filepath,
    val_images = test_x_filepath,
    val_annotations = test_y_filepath,
    checkpoints_path = checkpoints_filepath,
    auto_resume_checkpoint=True,
    epochs=5,
    steps_per_epoch=128,
    verify_dataset=False
)
out1 = CNN_model.predict_segmentation(
    inp=example1,
    out_fname="drive/Shared drives/Data Mining Project/Data/output1.png"
)
out2 = CNN_model.predict_segmentation(
    inp=example2,
    out_fname="drive/Shared drives/Data Mining Project/Data/output2.png"
)