import os
import pandas as pd
from src.logger import get_logger
from src.exception import CustomException
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File is not in the given path")
        
        with open(file_path,"r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Succesfully read the YAML file")
            return config
    
    except Exception as e:
        logger.error("Error occured while reading YAML file")
        raise CustomException("Failed to read YAML file", e)

def load_data(path):
    try:
        logger.info("Loading Data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Errpr loading the data{e}")
        raise CustomException("Failed to load data" , e)
    