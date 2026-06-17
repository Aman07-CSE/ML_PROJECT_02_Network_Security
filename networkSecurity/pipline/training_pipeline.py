import os, sys
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_transformation import DataTransformation
from networkSecurity.components.model_trainer import ModelTrainer

from networkSecurity.entity.config_entity import (
    TainingPipelineConfig,
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelTrainerConfig
)

from networkSecurity.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifacts,
    DataIngestionArtifact,
    DataValiditonArtifacts,
    ClassificationMatricArtifact
)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config=TainingPipelineConfig()

    def Start_data_ingestion(self):
        try:
            self.data_ingestion_config= DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("----------- Started Data Ingestion --------")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            logging.info("Initiate data ingestion")
            data_ingestion_artifact=data_ingestion.initiate_data_ingection()
            logging.info(f"Data intiatin complited___ {data_ingestion_artifact }")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            data_validation_config=DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("----------- Started Data Validation --------")
            data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            logging.info("Initiate data Validation --------------")
            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info("Data Validation complited---------")
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self,data_validation_artifact:DataValidationConfig):
        try:
            data_transformation_config= DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Data transformation started---------")
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
            logging.info("Initiate data Transformation --------------")
            data_transformation_artifact=data_transformation.initiate_data_transformation()
            logging.info("Data transformation complited---------")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifacts:
        try:
            logging.info("Model Training started---------")
            self.model_trainer_config:ModelTrainerConfig = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,model_trainer_config=self.model_trainer_config)
            logging.info("Initiate Model training --------------")
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            logging.info("Ended Model training --------------")
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.Start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)