"""The user route"""

from fastapi import APIRouter, File
from fastapi.datastructures import UploadFile
from fastapi.params import Depends
from joblib import load
from sklearn.metrics import balanced_accuracy_score, accuracy_score

from schemas import user_schema, predict_schema
from api import deps


router = APIRouter()


@router.post("/",
        name="Return the performance of the specified machine learning model",
        response_model=predict_schema.Prediction,
)
async def get_ml_performance(
        models: str,
        x_file: UploadFile=File(...),
        y_file: UploadFile=File(...),
        current_user: user_schema.User = Depends(deps.get_current_user)
):
    """Get the performance of the specified machine learning model."""
    X = x_file # Voir pour lire un CSV
    y= y_file # Voir pour lire un CSV
    model = load(f"rain-forecast-api/ml-models/{models}.pickle") # a tester
    predict = model.predict(X)
    accuracy = accuracy_score(y, predict)
    balanced_accuracy = balanced_accuracy_score(y, predict)

    result = {
            "model": models,
            "accuracy": accuracy, 
            "balanced_accuracy": balanced_accuracy,
    }

    return result

