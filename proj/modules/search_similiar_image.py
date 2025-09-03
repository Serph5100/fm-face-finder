from config import CROPPED_IMAGES_PATH, BASE_IMAGE_PATH, FINAL_IMAGES_PATH
from DeepImageSearch import Load_Data, Search_Setup
import os
import cv2

base_image_list = Load_Data().from_folder([BASE_IMAGE_PATH])
print(f'Base Image List : {base_image_list}')

def search_familiar_image(folder_name: str) -> None :
    """
    
    """
    cropped_folder = os.path.join(CROPPED_IMAGES_PATH, folder_name)
    search_image_list = Load_Data().from_folder([cropped_folder])

    search_model = Search_Setup(image_list=search_image_list, model_name='vgg19', pretrained=True, image_count=len(search_image_list))
    search_model.run_index()

    final_image = search_model.get_similar_images(image_path=base_image_list[0], number_of_images=1)
    print(f'================== FINAL IMAGE IS {final_image} ==================')
    print(f'================== final_image type IS {type(final_image)} ==================')

    #save the output image in final image path
    #if final_image is not None:
    #    output_path = os.path.join(FINAL_IMAGES_PATH, f"{folder_name}.jpg")
    #   cv2.imwrite(output_path, final_image)