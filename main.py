from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networkSecurity.entity.config_entity import TainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        tainingpipelineconfig=TainingPipelineConfig()
        dataingestionconfig= DataIngestionConfig(tainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingection()
        logging.info("Data intiatin complited")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(tainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate data Validation --------------")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation complited---------")
        print(data_validation_artifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)