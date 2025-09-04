from proj.modules.crop_image import crop_image
from proj.modules.read_excel import get_excel_data
from proj.modules.download_image_bing import download_image_bing
from proj.modules.search_similiar_image import search_familiar_image
from config import DATA_START_ROW, DATA_END_ROW
import os
import cv2

if __name__ == "__main__":
    print("hello world.")

    # ==== Testing Out read_excel.py ====
    excel_data = get_excel_data()

    data_end = min(DATA_END_ROW, len(excel_data))  # Ensure we don't exceed the DataFrame length
    for row_index in range(DATA_START_ROW, data_end):
        try:
            player_data = excel_data.iloc[row_index]

            # ==== Download image from Bing ====
            downloaded_image_path = download_image_bing(player_data)

            image_num_count = 1

            for image_file in os.listdir(downloaded_image_path):
                image_path = os.path.join(downloaded_image_path, image_file)
            
                # ==== if image unable to load ====
                image = cv2.imread(image_path)
                if image is None:
                    print(f"Failed to load image: {image_path}")
                    continue

                # ==== Check if image is not corrupted and can be read ====
                if not cv2.haveImageReader(image_path):
                    print(f"Corrupted image file: {image_path}")
                    continue

                # ==== Crop image by focusing on head ====
                crop_image(image, player_data["UID"], image_num_count)
                image_num_count += 1

            # ==== Search for the most similar image and save it ====
            player_image_path = search_familiar_image(folder_name=str(player_data["UID"]))

            if player_image_path:
                print(f"Similar image saved at: {player_image_path}")
            else:
                print("No similar image found.")

        except Exception as e:
            print(f"Error occurred while processing row_index {row_index}: {e}")
            break

    print(f"********************* Process completed. *********************\nRow Processed from {DATA_START_ROW} to {row_index}\n*********************")
