from networkSecurity.components.data_ingestion import DataIngestion

from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig
from networkSecurity.entity.config_entity import TainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        tainingpipelineconfig=TainingPipelineConfig()
        dataingestionconfig= DataIngestionConfig(tainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingection()
        print(dataingestionartifact)
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)