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
