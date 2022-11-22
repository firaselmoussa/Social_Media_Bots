import glob
from instabot import Bot
from create_quote import generateQuotedImage
import os
import schedule
import time

# delete config
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
# os.system("rm -rf config")

# login credentials
MY_USERNAME = os.environ["WISEBOT_INSTA_USERNAME"]
MY_PASSWORD = os.environ["WISEBOT_INSTA_PASSWORD"]

# created bot & logged it in
bot = Bot()
bot.login(username=MY_USERNAME, password=MY_PASSWORD)


# NEW POST
def newInstaPost():

    # generating new post
    quote = generateQuotedImage()
    img = "generated_imgs/quote_img.jpg"
    cptn = f'''"{quote[0]}"

        ~{quote[1]}


        #wisebot89'''

    # uploading  post
    bot.upload_photo(img, caption=cptn)

    bot.upload_story_photo(img, capyion="New Post!")
    # liking post
    bot.like_user(MY_USERNAME, amount=2)
    # comment
    my_id = bot.get_user_id_from_username(MY_USERNAME)
    my_media = bot.get_last_user_medias(my_id)
    bot.comment(my_media, """Share, Comment & Like

    #wisebot89""")

    # liking tags
    tags = ['quotes', 'wise', 'bot']
    for i in tags:
        bot.like_hashtag(i, amount=10)


# post every hour
schedule.every(1).days.do(newInstaPost)

while 1:
    schedule.run_pending()
    time.sleep(1)
