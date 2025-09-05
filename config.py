"""
Configuration file for setting up paths and parameters for the fm-face-finder project.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

#Desired Season, Used for Image Query!
DESIRED_SEASON = "1994"

# Final Image Size
IMAGE_SIZE = (260, 310)  # Width, Height

# Excel File Path
EXCEL_FILE_PATH = os.path.join(INPUT_DIR, "94_prem.xlsx") # Name of the Excel file

# Range
EXCEL_SHEET_NAME = "Sheet1"
DATA_START_ROW = 0  # Assuming the first row is the header
DATA_END_ROW = 800  # Adjust as needed

# Bing download settings
BING_IMAGES_PER_PLAYER = 5
BING_DOWNLOAD_PATH = os.path.join(OUTPUT_DIR, "downloaded")
BING_DOWNLOAD_VERBOSE = False # Set to True for detailed logs
BING_BAD_FILTER_WEBSITE = [] # List of website to filter out from searching.

# Processing settings
CROPPED_IMAGES_PATH = os.path.join(OUTPUT_DIR, "cropped")
BORDER_COLOR = (99, 104, 111)  # RGB Border Color
BORDER_SIZE = 3  # Size of the border in pixels (HAS TO BE POSITIVE INTEGER)

# Base Image Path : image you use to find the most familiar image out of the set
BASE_IMAGE_PATH = os.path.join(INPUT_DIR, "base_image")
FINAL_IMAGES_PATH = os.path.join(OUTPUT_DIR, "player_face")

