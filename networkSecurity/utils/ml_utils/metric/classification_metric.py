import sys
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.entity.artifact_entity import ClassificationMatricArtifact
from sklearn.metrics import f1_score, precision_score, recall_score

def get_classification_score(y_true,y_pred)->ClassificationMatricArtifact:
    try:
        model_f1_score = f1_score(y_true,y_pred)
        model_recall_score =recall_score(y_true,y_pred)
        model_precision_score =precision_score(y_true,y_pred)

        classification_matric = ClassificationMatricArtifact(
            f1_score=model_f1_score,
            recall_score=model_recall_score,
            precision_score=model_precision_score
        )
        return classification_matric
    except Exception as e:
        raise NetworkSecurityException(e,sys)