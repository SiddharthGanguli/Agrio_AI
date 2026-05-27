from crop_recommendation.entity.entity import DataIngestionConfig
import os
import pandas as pd
from sklearn.model_selection import train_test_split    
from crop_recommendation.logging import get_logger

logger = get_logger("data_ingestion")

class DataIngestion :

    def __init__(self,config:DataIngestionConfig):
        self.config = config
        

    def _read_data(self)->pd.DataFrame:

        if not self.config.source_dir.exists():
            raise FileNotFoundError(f"Source file {self.config.source_dir} does not exist")
        
        logger.info(f"Reading data from {self.config.source_dir}")

        data=pd.read_csv(self.config.source_dir)
        logger.info(f"Data read successfully from {self.config.source_dir} with shape {data.shape}")
        return data
    

    def _save_raw_data(self,data:pd.DataFrame):
        raw_data_path = self.config.root_dir/"raw.csv"
        raw_data_path.parent.mkdir(parents=True,exist_ok=True)

        data.to_csv(raw_data_path,index=False)
        logger.info(f"Raw data saved successfully at {raw_data_path}")

        return raw_data_path
    
    def _split_data(self,data:pd.DataFrame):
        logger.info(f"Splitting data into train and test sets with test size {self.config.test_size} and random state {self.config.random_state}")
        train_data, test_data = train_test_split(data,test_size=self.config.test_size,random_state=self.config.random_state)
        logger.info(f"Data split successfully into train and test sets with shapes {train_data.shape} and {test_data.shape} respectively")
        return train_data, test_data
    
    def run(self):

        try :
            logger.info("Starting data ingestion process")
            os.makedirs(self.config.root_dir,exist_ok=True)

            data = self._read_data()
            self._save_raw_data(data)

            train_data, test_data = self._split_data(data)

            self.config.train_dir.parent.mkdir(parents=True,exist_ok=True)
            train_data.to_csv(self.config.train_dir,index=False)
            logger.info(f"Train data saved successfully at {self.config.train_dir}")

            self.config.test_dir.parent.mkdir(parents=True,exist_ok=True)
            test_data.to_csv(self.config.test_dir,index=False)
            logger.info(f"Test data saved successfully at {self.config.test_dir}")

            return self.config.train_dir, self.config.test_dir
        
        except Exception as e:
            logger.error(f"Error occurred during data ingestion: {e}")
            raise e
