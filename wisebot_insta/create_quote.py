from tkinter import font as W1
from tkinter import *
from fnmatch import fnmatch
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from getImage import getImage
from getQuote import getQuote
import math
import textwrap
################################################################


def generateQuotedImage():
    # dimensions
    WIDTH = 1080
    HEIGHT = 1080
    FONT_SIZE = 36
    FW = Tk()
    FW.withdraw()

    # generating new images & quote
    getImage(WIDTH, HEIGHT)
    quote = getQuote()
    quote_length = len(quote[0])

    # open new immage
    img = Image.open("fetched_imgs/random_img.jpg")

    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(img)
    # decrease brightness to the half
    img = enhancer.enhance(0.5)

    # calculating words per line
    W2 = W1.Font(family="comicbd.ttf", size=FONT_SIZE)
    quote_width = W2.measure(quote[0])
    num_lines = math.ceil(quote_width/WIDTH)

    # draw quote on image
    draw = ImageDraw.Draw(img)
    quote_font = ImageFont.truetype("ebrima.ttf", FONT_SIZE)
    author_font = ImageFont.truetype("comicbd.ttf", FONT_SIZE-6)
    quote_segments = quote[0].split(" ")

    # spliting quote into equal lines
    lines = textwrap.wrap(quote[0], math.floor(len(quote[0])/num_lines))

    # rendering lines, line by line below each other
    x = 40
    for line in lines:
        draw.text((60, HEIGHT/1.6 + x), line,
                  font=quote_font, fill=(255, 255, 255))
        x += 40

    # rendering author name
    draw.text((60, HEIGHT/1.6 + x + 30), f"~ {quote[1]}",
              font=author_font, fill=(255, 255, 255))

    # save quote
    img.save("generated_imgs/quote_img.jpg")

    return quote
