from config import CROPPED_IMAGES_PATH, FINAL_IMAGES_PATH, BING_DOWNLOAD_PATH
import os
import shutil

def clear_and_recreate_dir(path, label):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Deleted {label} directory and all its contents: {path}")
    os.makedirs(path)
    print(f"Created directory: {path}")

if __name__ == "__main__":
    clear_and_recreate_dir(CROPPED_IMAGES_PATH, "cropped images")
    clear_and_recreate_dir(FINAL_IMAGES_PATH, "final images")
    clear_and_recreate_dir(BING_DOWNLOAD_PATH, "Bing download")
