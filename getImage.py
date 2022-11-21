import json
import requests
from PIL import Image

# https://random.imagecdn.app/500/150
# https://picsum.photos/200/300


def getImage():
    url = "https://picsum.photos/200/300"

    response = requests.get(url)
    filename = 'fetched_imgs/random_img.jpg'
    with open(filename, 'wb') as f:
        f.write(response.content)


getImage()
