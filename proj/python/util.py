import cv2
import numpy as np

def convertToRGB(image : np.ndarray) -> np.ndarray:
    '''convert the given image from black and white to RGB

    :param image: The input image in BGR format.
    :type image: np.ndarray

    :return: The output image in RGB format.
    :rtype: np.ndarray
    '''
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def extend_bbox(bbox: np.ndarray, offset: float = 0.1) -> np.ndarray:
    '''Extend the bounding box dimensions by a given offset.

    :param bbox: The input bounding box as [x, y, w, h].
    :type bbox: np.ndarray
    :param offset: Fraction of the bounding box dimensions to extend on each side, defaults to 0.1.
    :type offset: float

    :return: The extended bounding box as [x_new, y_new, w_new, h_new].
    :rtype: np.ndarray
    '''
    x, y, w, h = bbox
    left = right = top = bottom = offset
    return np.array([x - w * left, y - h * top, w * (1.0 + right + left), h * (1.0 + top + bottom)]).astype("int32")


def extend_to_rect(bbox: np.ndarray) -> np.ndarray:
    '''Convert the bounding box to a square while maintaining its center.

    :param bbox: The input bounding box as [x, y, w, h].
    :type bbox: np.ndarray

    :return: The square bounding box as [x_new, y_new, w_new, h_new].
    :rtype: np.ndarray
    '''
    x, y, w, h = bbox
    if w > h:
        diff = w - h
        return np.array([x, y - diff // 2, w, w])
    else:
        diff = h - w
        return np.array([x - diff // 2, y, h, h])

