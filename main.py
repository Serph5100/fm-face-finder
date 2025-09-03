from proj.modules.crop_image import crop_image
from proj.modules.read_excel import get_excel_data
from proj.modules.download_image_bing import download_image_bing
from proj.modules.search_similiar_image import search_familiar_image
import os
import cv2

if __name__ == "__main__":
    print("hello world.")

    # ==== Testing Out read_excel.py ====
    test_excel = get_excel_data()
    print(test_excel.iloc[32])
    #print(f'data type : {test_excel.iloc[0]["Club"]}')
    player_data = test_excel.iloc[32]

    downloaded_image_path = download_image_bing(player_data)

    print(f"Downloaded images are in: {downloaded_image_path}")

    image_num_count = 0

    for image_file in os.listdir(downloaded_image_path):
        image_path = os.path.join(downloaded_image_path, image_file)

        # DEBUG : Check if image is intact
        print(image_path)
        
        # ==== if image unable to load ====
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to load image: {image_path}")
            continue

        # ==== Check if image is not corrupted and can be read ====
        
        
        crop_image(image, player_data["UID"], image_num_count)
        image_num_count += 1

    search_familiar_image(folder_name=str(player_data["UID"]))