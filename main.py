from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.data_transformation import DataTransformation
from networkSecurity.components.model_trainer import ModelTrainer
from networkSecurity.entity.config_entity import ModelTrainerConfig
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig, DataTransformationConfig
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

        data_transformation_config= DataTransformationConfig(tainingpipelineconfig)
        logging.info("Data transformation started---------")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data transformation complited---------")
        print(data_transformation_artifact)

        logging.info("Model Training started---------")
        model_trainer_config = ModelTrainerConfig(tainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training Ended--------------Model Training artifact created")


    except Exception as e:
           raise NetworkSecurityException(e,sys)