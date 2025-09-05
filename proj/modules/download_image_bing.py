"""
This script is for downloading images from Bing using the better_bing_image_downloader library.

better_bing_image_downloader is from KTS-o7
source : https://github.com/KTS-o7/better_bing_image_downloader
"""

from better_bing_image_downloader import downloader
import os
from config import DESIRED_SEASON, BING_BAD_FILTER_WEBSITE, BING_DOWNLOAD_PATH, BING_DOWNLOAD_VERBOSE, BING_IMAGES_PER_PLAYER

def download_image_bing(query: object) -> str :
    """
    Download images from Bing based on the provided query.
    The Query shall contain player name, club, and season before searching

    :param query: A list containing player name and club
    :return: The path to the folder where images are downloaded.
    :rtype: str
    """

    # Construct the search query
    # Example: footballer "Alan Shearer" "Newcastle United" "1994"
    search_query = f"footballer {query['Name']} {query['Club']} \"{DESIRED_SEASON}\""

    # Download images using the downloader
    success = downloader(
        query=search_query,
        output_dir=BING_DOWNLOAD_PATH,
        limit=BING_IMAGES_PER_PLAYER,
        filter="photo",
        badsites=BING_BAD_FILTER_WEBSITE,
        verbose=BING_DOWNLOAD_VERBOSE,
        timeout=40
    )

    output_folder = os.path.join(BING_DOWNLOAD_PATH, search_query)
    print(f"Download image for {query['Name']} successful\n Folder is in {output_folder}")

    return output_folder
