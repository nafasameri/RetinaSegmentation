# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:15:43 2019

@author: Reza Azad
"""
from __future__ import division
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
import numpy as np
#from help_functions import *
#from extract_patches import *

#function to obtain data for training/testing (validation)
from extract_patches import get_data_training

#========= Load settings from Config file
#patch to the datasets
path_data = './dataset_training/'


print('extracting patches')
patches_imgs_train, patches_masks_train = get_data_training(
    DRIVE_train_imgs_original = path_data + 'imgs_train.hdf5',
    DRIVE_train_groudTruth    = path_data + 'groundTruth_train.hdf5',  #masks
    patch_height = 64,
    patch_width  = 64,
    N_subimgs    = 60000,
    inside_FOV = 'True' #select the patches only inside the FOV  (default == True)
)


np.save('patches_imgs_train',patches_imgs_train)
np.save('patches_masks_train',patches_masks_train)


