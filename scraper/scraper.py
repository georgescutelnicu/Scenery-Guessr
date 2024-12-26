import os
import requests
from bs4 import BeautifulSoup
import argparse


class ImageScraper:
    def __init__(self):
        self.url = "https://geohints.com/Scenery"
        self.base_url = "https://geohints.com/"

    def scrape_images(self):
        """Scrape image URLs from the page."""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        img_sources = []

        for div in soup.find_all("div", class_="bollard"):
            img_tag = div.find("img")
            img_src = self.base_url + img_tag.get("src")
            img_sources.append(img_src)

        return img_sources

    def download_images(self, img_sources, output_dir):
        """Download the images to the specified output directory."""
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
            except OSError as e:
                raise ValueError(f"Failed to create directory on the specified path '{output_dir}': {e}")

        for img_src in img_sources:
            img_name = img_src.split("/")[-1].split(".")[0]
            img_response = requests.get(img_src)
            if img_response.status_code == 200:
                img_path = os.path.join(output_dir, img_name + ".jpg")
                with open(img_path, "wb") as f:
                    f.write(img_response.content)
            else:
                print(f"Failed to download {img_name}.")

        print("Download complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape and download images from Geohints Scenery page.")
    parser.add_argument("--output_dir", "-o", type=str, required=True, help="The directory where the images"
                                                                            " will be saved.")
    args = parser.parse_args()

    scraper = ImageScraper()
    img_sources = scraper.scrape_images()
    scraper.download_images(img_sources, args.output_dir)
