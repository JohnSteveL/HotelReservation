from src.logger import get_logger
from src.exception import CustomException
import sys

logger = get_logger(__name__)

def divide_number(a,b):
    try:
        result = a/b
        logger.info("dividing two number")
        return result
    except Exception as e:
        logger.error("Error occured")
        raise CustomException("Custom Error Zero",sys)

if __name__ =="__main__":
    try:
        logger.info("Starting main Program")
        divide_number(10,2)
    except CustomException as ce:
        logger.error(str(ce))