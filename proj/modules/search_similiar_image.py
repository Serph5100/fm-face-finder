"""
This script searches for similar images using the DeepImageSearch library.
loads images from the cropped image folder, indexes them, and finds the most similar image compared to the base image.
"""
from config import CROPPED_IMAGES_PATH, BASE_IMAGE_PATH, FINAL_IMAGES_PATH
from DeepImageSearch import Load_Data, Search_Setup
import os
import cv2
import shutil

# Load base image
base_image_list = Load_Data().from_folder([BASE_IMAGE_PATH])
print(f'Base Image List : {base_image_list}')

model_name = 'vgg19'

# Initialize the search model
search_model = Search_Setup(image_list=base_image_list, model_name=model_name, pretrained=True, image_count=5)

def clear_metadata(model_name: str):
    """
    Deletes only the .pkl and .idx files for the given model.

    :param model_name: The name of the model whose metadata files are to be deleted.
    :type model_name: str
    """
    metadata_dir = f'metadata-files/{model_name}'
    if os.path.exists(metadata_dir):
        for file_name in os.listdir(metadata_dir):
            # Only delete .pkl and .idx files
            if file_name.endswith('.pkl') or file_name.endswith('.idx'):
                file_path = os.path.join(metadata_dir, file_name)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

def search_familiar_image(folder_name: str) -> str:
    """
    Searches for the most similar image in the specified folder and saves it to FINAL_IMAGES_PATH.
    
    :param folder_name: The name of the folder containing cropped images.
    :return: The path to the saved similar image, or None if no image was found.
    :rtype: str or None
    """
    # Clear metadata and index files
    clear_metadata(model_name=model_name)


    #Set up folder that we want to search
    cropped_folder = os.path.join(CROPPED_IMAGES_PATH, folder_name)
    search_image_list = Load_Data().from_folder([cropped_folder])

    # If no images found, return None
    if not search_image_list:
        print(f"==== No images found in folder: {cropped_folder} ====")
        return None

    search_model.image_list = search_image_list
    search_model.run_index()

    #search for the most similar image compared to the base image
    final_image_path = search_model.get_similar_images(image_path=search_image_list[0], number_of_images=1)
    print(f'Final Image Path : {final_image_path}')

    # Extract the first image path from the dictionary
    if final_image_path:
        similar_image_path = list(final_image_path.values())[0]
        output_path = os.path.join(FINAL_IMAGES_PATH, f"{folder_name}.jpg")

        # Copy the image to the FINAL_IMAGES_PATH
        shutil.copy(similar_image_path, output_path)
        print(f"Saved similar image to: {output_path}")
        return output_path

    return None

