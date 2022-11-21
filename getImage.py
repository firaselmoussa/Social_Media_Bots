import requests
################################################################

# https://random.imagecdn.app/500/150
# https://picsum.photos/200/300


def getImage(w, h):
    url = f"https://picsum.photos/{w}/{h}?blur=2"

    response = requests.get(url)

    filename = "fetched_imgs/random_img.jpg"

    with open(filename, 'wb') as f:
        f.write(response.content)
