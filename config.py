import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

#Desired Season, Used for Image Query!
DESIRED_SEASON = "1994"

# Final Image Size
IMAGE_SIZE = (260, 310)  # Width, Height

# Excel File Path
EXCEL_FILE_PATH = os.path.join(INPUT_DIR, "serie_a_1994.xlsx")

# Range
EXCEL_SHEET_NAME = "Sheet1"
DATA_START_ROW = 2  # Assuming the first row is the header

# Bing download settings
BING_IMAGES_PER_PLAYER = 5
BING_DOWNLOAD_PATH = os.path.join(OUTPUT_DIR, "downloaded")
BING_DOWNLOAD_VERBOSE = False # Set to True for detailed logs
BING_BAD_FILTER_WEBSITE = []

# Processing settings
CROPPED_IMAGES_PATH = os.path.join(OUTPUT_DIR, "cropped")
FINAL_IMAGES_PATH = os.path.join(OUTPUT_DIR, "player_faces")

