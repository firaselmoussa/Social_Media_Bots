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
    WIDTH = 300
    HEIGHT = 500
    FONT_SIZE = 16
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
