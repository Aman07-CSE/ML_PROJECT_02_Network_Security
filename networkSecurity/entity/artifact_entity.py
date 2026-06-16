from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str


@dataclass
class DataValiditonArtifacts:
    validation_status: bool
    valid_train_file_path : str
    invalid_train_file_path : str
    valid_test_file_path : str
    invalid_test_file_path : str
    drift_report_file_path :str

@dataclass
class DataTransformationArtifact:
    transform_object_file_path:str
    transform_train_file_path:str
    transform_test_file_path:str

@dataclass
class ClassificationMatricArtifact:
    f1_score: float
    precision_score:float
    recall_score:float

@dataclass
class ModelTrainerArtifacts:
    trained_model_file_path:str
    train_matric_artifact:ClassificationMatricArtifact
    test_matric_artifact:ClassificationMatricArtifact