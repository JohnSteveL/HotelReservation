import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.exception import CustomException
from config.path_config import *
from utils.common import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["test_ratio"]

        os.makedirs(RAW_DIR , exist_ok=True)

        logger.info(f"Data Ingestion started with {self.bucket_name} and file is {self.file_name}")

    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"Raw file is succesfully downloaded to {RAW_FILE_PATH}")
        
        except Exception as e:
            logger.error("Error occured while downloading the csv file")
            raise CustomException("Failed to download csv file", e)
    
    def split_data(self):
        try:
            logger.info("Started Train-Test splitting process")
            data = pd.read_csv(RAW_FILE_PATH)

            train_data, test_data = train_test_split(data, test_size=self.train_test_ratio, random_state=42)
            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")
        
        except Exception as e:
            logger.error("Error occured during splitting data")
            raise CustomException("Failed to Split the data", e)
    
    def run(self):
        try:
            logger.info("Starting Data Ingestion")

            self.download_csv_from_gcp()
            self.split_data()

            logger.info("Data Ingestion completed succesfully")
        
        except CustomException as ce:
            logger.error(f"CustomeException : {str(ce)}")
        
        finally:
            logger.info("Data Ingestion Completed")


if __name__ =="__main__":

    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()