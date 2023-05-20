import pandas as pd
import logging

def main():
    print("Starting")
    
    fileName="colour_info.xlsx"
    
    logging.basicConfig(filename="file.log",
                   format="%(asctime)s %(message)s",
                   filemode="w")
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)
        
    excel = pd.read_excel(fileName)
    logger.info("Read excel file ", fileName)
    print(excel)

if __name__ == '__main__':
    main()
