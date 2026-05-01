"""
Web utility functions for downloading and processing web content.
"""

import os
import requests
from urllib.parse import urlparse

def download_html(url, save_path):
    """
    Download HTML content from a URL and save it to a file.

    Args:
        url (str): The URL to download content from
        save_path (str): The path where the HTML content should be saved

    Returns:
        bool: True if download was successful, False otherwise
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save the HTML content
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

        return True
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False

def get_filename_from_url(url):
    """
    Extract filename from URL.

    Args:
        url (str): The URL to extract filename from

    Returns:
        str: The filename extracted from the URL
    """
    parsed_url = urlparse(url)
    path = parsed_url.path
    filename = os.path.basename(path)

    # If there's no filename, use the last part of the path
    if not filename:
        # Get the last non-empty part of the path
        path_parts = [p for p in path.split('/') if p]
        if path_parts:
            filename = path_parts[-1]
        else:
            filename = "index"

    return filename