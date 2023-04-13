import os
import sys 
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transform import DataTransformation 


##Intilize the Data Ingestion configration
@dataclass
class DataIngestionconfigration:
    train_data_path:str=os.path.join("artifacts",'train.csv')
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")

# create a class for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfigration()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion method strated")
        try:
            df=pd.read_csv("https://raw.githubusercontent.com/krishnaik06/FSDSRegression/main/notebooks/data/gemstone.csv")
            logging.info("Dataset read as pandas")
            
            #make our directory
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("train_test_split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info("exception occured  ata data ingestion stage")
            raise CustomException(e,sys)
            
