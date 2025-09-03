from proj.modules.crop_image import crop_image
import cv2

if __name__ == "__main__":
    print("hello world.")

    # ==== Testing Out crop_image.py ====
    test_image_directory = 'proj/python_notebook/dataset/abedi/Image_3.jpg'
    test_image = cv2.imread(test_image_directory)

    crop_image(test_image, "abedi", 1)
