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

def extend_bbox_ratio(bbox: np.ndarray, height: int, width: int, offset: float = 0.5, height_scale: float = 1.5) -> np.ndarray:
    '''Extend the bounding box dimensions based on the ratio between given bbox and original image size.

    :param bbox: The input bounding box as [x, y, w, h].
    :type bbox: np.ndarray
    :param height: Height of the original image
    :type height: int
    :param width: Width of the original image
    :type width: int
    :param offset: Fraction of the bounding box dimensions to extend on each side, defaults to 0.5.
    :type offset: float
    :param height_scale: Scaling factor for the height extension, defaults to 1.5.
    :type height_scale: float

    :return: The extended bounding box as [x_new, y_new, w_new, h_new].
    :rtype: np.ndarray
    '''
    x, y, w, h = bbox
    width_ratio = abs(offset - (w / width))
    height_ratio = abs(offset - (h / height))
    left = right = width_ratio
    top = bottom = height_ratio

    return np.array([x - w * left, 
                     y - h * top, 
                     w * (1.0 + right + left), 
                     h * (1.0 + top + bottom) * height_scale]).astype("int32")

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
    return np.array([x - w * left, 
                     y - h * top, 
                     w * (1.0 + right + left), 
                     h * (1.0 + top + bottom)]).astype("int32")


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

def extend_to_custom_rect(bbox: np.ndarray, width: int = 260, height: int = 310) -> np.ndarray:
    '''Convert the bounding box to a custom rectangle while maintaining its center.

    :param bbox: The input bounding box as [x, y, w, h].
    :type bbox: np.ndarray
    :param height: The desired height of the output rectangle.
    :type height: int
    :param width: The desired width of the output rectangle.
    :type width: int

    :return: The custom rectangle as [x_new, y_new, w_new, h_new].
    :rtype: np.ndarray
    '''
    x, y, w, h = bbox
    target_aspect = width / height
    current_aspect = w / h
    if current_aspect > target_aspect:
        new_h = w / target_aspect
        diff = new_h - h
        return validate_box_size(np.array([x, y - diff // 2, w, int(new_h)]).astype("int32"))
    else:
        new_w = h * target_aspect
        diff = new_w - w
        return validate_box_size(np.array([x - diff // 2, y, int(new_w), h]).astype("int32"))

def resize_image(image: np.ndarray, target_size: tuple[int, int]) -> np.ndarray:
    '''Resize the given image to the target size.

    :param image: The input image.
    :type image: np.ndarray
    :param target_size: The desired output size as (width, height).
    :type target_size: tuple[int, int]

    :return: The resized image.
    :rtype: np.ndarray
    '''

    
    
    return cv2.resize(image, target_size)

def validate_box_size(box: np.ndarray) -> np.ndarray:
    '''Ensure that the bounding box has non-negative coordinates and dimensions.

    :param box: The input bounding box as [x, y, w, h].
    :type box: np.ndarray

    :return: The validated bounding box with non-negative values.
    :rtype: np.ndarray
    '''
    x, y, w, h = box
    x = max(0, x)
    y = max(0, y)
    w = max(0, w)
    h = max(0, h)
    return np.array([x, y, w, h]).astype("int32")
