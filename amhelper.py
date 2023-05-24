import logging
import math
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

excel = None
image = None
colours = []

def get_diff(a: int, b: int):
    a = int(a)
    b = int(b)
    if a > b:
        return a - b
    return b - a

# Calculates the Euclidean distance between two tuples 
def get_diff_tuple(a, b):
    toReturn = math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b))) 
    return toReturn

def get_tuple_avg(a):
    return sum(map(float, filter(None, a[:])))/3

def compare_tuple(a, b):
    return True

class Item:
    def __init__(self, name, colour1, colour2, colour3, colour4):
        self.name = name
        self.colour1 = self.seperate_RGB(colour1)
        self.colour2 = self.seperate_RGB(colour2)
        self.colour3 = self.seperate_RGB(colour3)
        self.colour4 = self.seperate_RGB(colour4)

    def seperate_RGB(self, rgb):
        separate = rgb.split(',')      
        red = int(separate[0][4:])
        green = int(separate[1][1:])
        blue = int(separate[2][1:-1])

        return (red, green, blue)

    def closest_colour(self, colour):
        colour1Diff = get_diff_tuple(self.colour1, colour)
        colour2Diff = get_diff_tuple(self.colour2, colour)
        colour3Diff = get_diff_tuple(self.colour3, colour)

        closestColour, closestDiff = min([(self.colour1, colour1Diff), (self.colour2, colour2Diff), (self.colour3, colour3Diff)], key=lambda x: x[1])
        return closestDiff, closestColour

class Comparison:
    def __init__(self, item, colour):
        self.item = item
        self.colour = colour


def read_colours(file_name: str):
    
    try:
        global excel
        excel = pd.read_excel(file_name)
    except:
        return False

    # Create an array of items. Each item holds its name, along with the four colours it can produce (as an RGB tuple)
    for index, row in excel.iterrows():
        global colours
        colours.append(Item(row[0], row[1], row[2], row[3], row[4]))
        
    return True

def read_image(file_name: str):
    # Read image
    try:
        global image
        image = Image.open(file_name).convert('RGB')
        return True
    except:
        return False
        
  
def get_preview():
    # Resize to fit onto the canvas. Currently, we only support a single canvas (32x32)
    canvasSize = (32,32)
    image.thumbnail(canvasSize, Image.ANTIALIAS)

    # For each pixel, we need to find the closest-matching RGB from the items. There's probably a more efficient way of doing it.
    imageData = list(image.getdata())
            
    # Compare pixels to colour
    pixelComparisons = {}
    for i in range(len(imageData)):
        currentBestDiff = 255
        currentBestColour = Comparison('None', 'None')
        for item in colours:
            currentAvg, currentColour = item.closest_colour(imageData[i])
            if currentAvg < currentBestDiff:
                currentBestDiff = currentAvg
                currentBestColour = Comparison(item.name, currentColour)
        pixelComparisons[i] = currentBestColour
    
    # Create new image
    imageNewArr = []
    for i in pixelComparisons:
        imageNewArr.append(pixelComparisons[i].colour)

    previewImage = Image.new("RGB", image.size)
    previewImage.putdata(imageNewArr)
    previewImage.save("preview.png")
