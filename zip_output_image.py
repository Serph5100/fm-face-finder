from config import FINAL_IMAGES_PATH
import os
import zipfile

if __name__ == "__main__":
    if os.path.exists(FINAL_IMAGES_PATH):
        zipf = zipfile.ZipFile('final_images.zip', 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(FINAL_IMAGES_PATH):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                           os.path.join(FINAL_IMAGES_PATH, '..')))
        zipf.close()
        print(f"Zipped final images to final_images.zip")