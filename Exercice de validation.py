import time
import requests
import threading


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

    t1 =threading.Thread(target=download_image, args=(img_urls[0],))
    t2 =threading.Thread(target=download_image, args=(img_urls[1],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.perf_counter()

    print(f"Tasks ended in {round(end - start, 2)} second(s)")



