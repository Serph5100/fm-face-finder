"""
This Script is for cropping image focused on a human head, using VGGHeads Library
"""
import os

from config import CROPPED_IMAGES_PATH, BING_DOWNLOAD_PATH

import numpy as np

from head_detector import HeadDetector
import cv2
import util

# ================= FIX FOR OLDER CODE =================

np.bool = np.bool_  
np.int = np.int_    
np.float = np.float_  
np.complex = np.complex_ 
np.object = np.object_  
np.unicode = np.unicode_  
np.str = np.str_ 

# ================= initialize head detector =================
detector = HeadDetector()

def crop_image(image: np.ndarray, save_path: str) -> bool:
    '''Crop the image to focus on the human head and save it to the specified path.

    :param image_path: The path to the input image.
    :type image_path: str
    :param save_path: The path to save the cropped image.
    :type save_path: str

    :return: True if cropping and saving were successful, False otherwise.
    :rtype: bool
    '''
    
    predictions = detector.detect(image)