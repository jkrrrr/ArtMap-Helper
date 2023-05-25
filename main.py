import amhelper as amh

import logging
import sys
import math

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from PIL import ImageTk, Image

file_path = ""

# Function to initialize the tkinter window
def init_window():
    window = tk.Tk()

    window.title("Art Map Helper")

    # Center window and define width and height
    window_width = 900
    window_height = 500

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
     
    window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    window.resizable(False, False)

    return window

# Button function: gets an image and renders it in a label widget
def get_file():
    global image
    # Ask the user to select a file
    file_path = filedialog.askopenfilename()
    amh.read_image(file_path)
    if file_path:
        # Open file as an image
        image = Image.open(file_path)
        # Scale the image while keeping its aspect ratio
        width = 300
        width_ratio = width/image.width
        height = int(image.height * width_ratio)
        image = image.resize((width, height))
        # Prepare image for render
        render = ImageTk.PhotoImage(image)
        imageWidget.configure(image=render)
        imageWidget.image = render
        imageWidget.place(x=0, y=0)

# Button function: converts the image into an artmap and renders it
def get_artmap():
    global preview
    preview = amh.get_preview()
    width = 200
    width_ratio = width/preview.width
    height = int(preview.height * width_ratio)
    preview = preview.resize((width, height), resample=Image.NEAREST) # Image.NEAREST is used, as by default, antialiasing is applied, which we don't want with pixel art
    render = ImageTk.PhotoImage(preview)
    previewWidget.configure(image=render)
    previewWidget.image = render

# Button function: saves the preview produce by get_artmap() into a file
def save_to_file():
    file_path = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=[("PNG", "*.png"), ("All files", "*.*")], title="Save image")
    if file_path and preview:
        preview.save(file_path.name)

# Initialize window widgets
def init_widgets(window):
    ttk.Frame(window)

    # Select the image from a file
    button = ttk.Button(window, text="Select image from file", command=get_file)
    button.pack(fill=tk.Y)

    # Displays the selected image
    global imageWidget
    imageWidget = ttk.Label(window)
    imageWidget.pack(anchor=tk.W)

    # Calculates the artmap of that image
    button = ttk.Button(window, text="Calculate ArtMap", command=get_artmap)
    button.pack(anchor=tk.N, side=tk.TOP)

    # Displays the artmap
    global previewWidget
    previewWidget = ttk.Label(window)
    previewWidget.pack()

    # Save the artmap as a file
    saveButton = ttk.Button(window, text="Save to file", command=save_to_file)
    saveButton.pack(anchor=tk.S, side=tk.BOTTOM, fill=tk.X)

def main():
    # Create logger
    logging.basicConfig(filename="file.log",
                        format="%(asctime)s %(message)s",
                        filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # fileName is the spreadsheet containing all the colour information
    fileName="colour_info.xlsx"

    # Read colours
    amh.read_colours("colour_info.xlsx")

    logger.info("Creating window")
    window = init_window()

    logger.info("Intializing window")
    init_widgets(window)

    logger.info("Starting window main loop")
    window.mainloop()

if __name__ == "__main__":
    main()
