import amhelper as amh

import logging

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from PIL import ImageTk, Image

file_path = ""

def button_click():
    print("THE BUTTON HAS BEEN CLICKED")

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

    # Window will appear at the top
    # window.attributes('-topmost', 1)

    return window

def get_file():
    global image
    file_path = filedialog.askopenfilename()
    amh.read_image(file_path)
    if file_path:
        image = Image.open(file_path)
        width = 300
        width_ratio = width/image.width
        height = int(image.height * width_ratio)
        image = image.resize((width, height))
        render = ImageTk.PhotoImage(image)
        print(file_path)
        imageWidget.configure(image=render)
        imageWidget.image = render
        imageWidget.place(x=0, y=0)

def get_artmap():
    preview = amh.get_preview()
    width = 300
    width_ratio = width/preview.width
    height = int(preview.height * width_ratio)
    preview = preview.resize((width, height), resample=Image.NEAREST)
    render = ImageTk.PhotoImage(preview)
    previewWidget.configure(image=render)
    previewWidget.image = render


def init_widgets(window):
    ttk.Frame(window, padding=10)

    button = ttk.Button(window, text="Select image from file", command=get_file)
    button.pack()

    global imageWidget
    imageWidget = ttk.Label(window)
    imageWidget.pack()

    button = ttk.Button(window, text="Calculate ArtMap", command=get_artmap)
    button.pack()

    global previewWidget
    previewWidget = ttk.Label(window)
    previewWidget.pack()

def main():
    # Create logger
    logging.basicConfig(filename="file.log",
                        format="%(asctime)s %(message)s",
                        filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

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
