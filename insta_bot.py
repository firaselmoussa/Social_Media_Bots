import glob
from instabot import Bot
from create_quote import generateQuotedImage
import os


def newInstaPost():
    # delete config
    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])
    os.system("rm -rf config")

    # login credentials
    MY_USERNAME = os.environ["WISEBOT_INSTA_USERNAME"]
    MY_PASSWORD = os.environ["WISEBOT_INSTA_PASSWORD"]

    # created bot & logged it in
    bot = Bot()
    bot.login(username=MY_USERNAME, password=MY_PASSWORD)

    # generating new post
    quote = generateQuotedImage()
    img = "generated_imgs/quote_img.jpg"
    cptn = f'''"{quote[0]}"
                                
        ~{quote[1]}
                                
                                
                                
        #wisebot89'''

    # uploading  post
    bot.upload_photo(img, caption=cptn)
    # liking post
    bot.like_user(MY_USERNAME, amount=1)
