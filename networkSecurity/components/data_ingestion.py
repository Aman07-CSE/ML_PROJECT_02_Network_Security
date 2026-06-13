from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging

# configuration of Data Ingection Config 
from networkSecurity.entity.config_entity import DataIngestionConfig
from networkSecurity.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI=os.getenv("MONGO_DB_URI")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def export_collection_as_dataframe(self):
        """
        Read data From Mongodb
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URI)
            collecction = self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collecction.find()))
            if '_id' in df.columns.to_list():
                df=df.drop(columns=["_id"])
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            # creating folder
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            logging.info("Performing split_data_as_train_test on dataframe")
            train_set,test_set=train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Exited split_data_as_train_test method of data ingetion ")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_name)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(" Exporting training and testing file path")
            train_set.to_csv(
                self.data_ingestion_config.training_file_name, index=False,header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.testing_file_name, index=False,header=True
            )
            logging.info("Exported train test split file path")
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def initiate_data_ingection(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_name,
                                                            test_file_path=self.data_ingestion_config.testing_file_name)
            return data_ingestion_artifact


        except Exception as e:
            raise NetworkSecurityException(e,sys)
    