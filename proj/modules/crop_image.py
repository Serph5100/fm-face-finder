"""
This Script is for cropping image focused on a human head, using VGGHeads Library
"""
import os
import sys

from config import CROPPED_IMAGES_PATH, IMAGE_SIZE

import numpy as np

from head_detector import HeadDetector
import cv2
import proj.util as util


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

def crop_image(image: np.ndarray, folder_name: str, image_num: int) -> bool:
    '''Crop the image to focus on the human head and save it to the specified path.

    :param image_path: The path to the input image.
    :type image_path: str
    :param save_path: The path to save the cropped image.
    :type save_path: str

    :return: True if cropping and saving were successful, False otherwise.
    :rtype: bool
    '''
    # ==== Find Head from the image ====
    predictions = detector(image)

    # ==== Only choose to write image with 1 head. ====
    if len(predictions.heads) > 1 :
        print(f"Image has more than 1 head, skipping image.")
        return False

    image_copy = image.copy()

    image_height = image_copy.shape[0]
    image_width = image_copy.shape[1]

    # ==== Expand bounding box to cover other part of the body ====
    for head in predictions.heads:
    
        rectangles = util.extend_to_custom_rect(
        util.extend_bbox_ratio(bbox=head.bbox, 
                                  height=image_height, 
                                  width=image_width,
                                  offset=0.5
                                  ),
                                  width=IMAGE_SIZE[0],
                                  height=IMAGE_SIZE[1]
        )
        x, y, w, h = rectangles

    print(f"x={x}, y={y}, w={w}, h={h}")


    # ==== Crop and Resizing Image ====
    image = image[y:y+h, x:x+w]
    image = util.resize_image(image, IMAGE_SIZE)

    save_path = os.path.join(CROPPED_IMAGES_PATH, folder_name, f"cropped_{image_num}.jpg")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    print(f"Saving cropped image {image_num} to {save_path}")

    return cv2.imwrite(save_path, image)
