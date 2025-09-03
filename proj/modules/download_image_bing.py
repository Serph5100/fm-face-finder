from better_bing_image_downloader import downloader
import os
from config import DESIRED_SEASON, BING_BAD_FILTER_WEBSITE, BING_DOWNLOAD_PATH, BING_DOWNLOAD_VERBOSE, BING_IMAGES_PER_PLAYER

def download_image_bing(query: object) -> str :
    """
    Download images from Bing based on the provided query.
    The Query shall contain player name, club, and season before searching

    :param query: A list containing player name, club, and season
    :return: True if download was successful, False otherwise
    """

    # Construct the search query
    search_query = f"footballer {query['Name']} {query['Club']} \"{DESIRED_SEASON}\""

    # Download images using the downloader
    success = downloader(
        query=search_query,
        output_dir=BING_DOWNLOAD_PATH,
        limit=BING_IMAGES_PER_PLAYER,
        filter="photo",
        badsites=BING_BAD_FILTER_WEBSITE,
        verbose=BING_DOWNLOAD_VERBOSE
    )

    output_folder = os.path.join(BING_DOWNLOAD_PATH, search_query)
    print(f"Download image for {query['Name']} successful\n Folder is in {output_folder}")

    return output_folder
