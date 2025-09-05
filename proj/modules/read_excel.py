"""
Module to read data from an Excel file that is specified in the config.py file.
"""
from config import EXCEL_FILE_PATH, EXCEL_SHEET_NAME
import pandas as pd

def get_excel_data() -> pd.DataFrame:
    """
    Read data from an Excel file and return it as a DataFrame.

    :return: DataFrame containing the Excel data
    """
    df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=EXCEL_SHEET_NAME)
    return df
