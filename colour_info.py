import pandas as pd
import logging

class colour_info:
    def __init__(self):
        self.read_file

        logging.basicConfig(filename="file.log",
                           format="%(asctime)s %(message)s",
                           filemode="w")
        logger = logging.getLogger()

        logger.setLevel(logging.DEBUG)

    def read_file(self, fileName):
        excel = pd.read_excel(fileName)
        print(excel)
        return excel

