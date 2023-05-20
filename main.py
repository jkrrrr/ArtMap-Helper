import pandas as pd
import logging
import sys

class item:
    def __init__(self, name, colour1, colour2, colour3, colour4):
        self.name = name
        self.colour1 = self.seperate_RGB(colour1)
        self.colour2 = self.seperate_RGB(colour2)
        self.colour3 = self.seperate_RGB(colour3)
        self.colour4 = self.seperate_RGB(colour4)

    def seperate_RGB(self, rgb):
        separate = rgb.split(',')      
        red = separate[0][4:]
        green = separate[1][1:]
        blue = separate[2][1:-1]

        return (red, green, blue)


def main():
    # Create logger
    logging.basicConfig(filename="file.log",
                   format="%(asctime)s %(message)s",
                   filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # fileName is the spreadsheet containing all the colour information
    fileName="colour_info.xlsx"

    logger.info("Reading spreadsheet %s", fileName)
    try:
        excel = pd.read_excel(fileName)
    except:
        logger.error("%s could not be found", fileName)
        sys.exit()

    # Create an array of items. Each item holds its name, along with the four colours it can produce (as an RGB tuple)
    logger.info("Creating items")
    colours = []
    for index, row in excel.iterrows():
        colours.append(item(row[0], row[1], row[2], row[3], row[4]))


    

if __name__ == '__main__':
    main()
