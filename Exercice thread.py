import requests
import time

img_urls = [
'https://cdn.pixabay.com/photo/2017/07/15/19/42/train-track-2507499_1280.jpg',
'https://pixabay.com/photos/android-linux-marshmallow-994910/'
]
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")


if __name__ == '__main__':
    start = time.perf_counter()

    for url in img_urls:
        download_image(url)

    end= time.perf_counter()

    print(f"Tasks ended in {round(end - start, 3)} second(s)")