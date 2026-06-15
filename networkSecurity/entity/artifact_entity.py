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