import os
from pathlib import Path

'''
Data Ingestion
'''

RAW_DIR = Path("artifacts/raw")
RAW_FILE_PATH = RAW_DIR / "raw.csv"
TRAIN_FILE_PATH = RAW_DIR / "train.csv"
TEST_FILE_PATH = RAW_DIR / "test.csv"
CONFIG_PATH = Path("config/config.yaml")

'''
Data Processing
'''

PROCESSED_DIR = Path("artifacts/processed")
PROCESSED_TRAIN_DATA_PATH = PROCESSED_DIR/"processed_train.csv"
PROCESSED_TEST_DATA_PATH = PROCESSED_DIR/"processed_test.csv"