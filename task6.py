import os
import argparse
import requests
from concurrent.futures import ThreadPoolExecutor

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.basename(url)
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {url} as {filename}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: str{e}")

def main():
    parser = argparse.ArgumentParser(description="Parallel image downloader using concurrent.futures.")
    parser.add_argument("urls",
                        nargs='+',
                        help="List of image URLs to download."
                        )
    args = parser.parse_args()

    urls = args.urls

    if not urls:
        print("No URLs provided.")
        return

    with ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)

if __name__ == "__main__":
    main()
