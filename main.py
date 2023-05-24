import amhelper as amh

def main():
    print("Hello, World!")
    amh.read_colours("colour_info.xlsx")
    amh.read_image("image.png")
    amh.get_preview()

if __name__ == "__main__":
    main()
