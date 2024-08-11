# 学習したモデルを使って予測を行う

import numpy as np
import pandas as pd
import pickle

# 使用する説明変数を指定
feature_cols = [
    "AgeInt",
    "TypeofContactInt",
    "CityTier",
    "DurationInt",
    "OccupationInt",
    "GenderInt",
    "NumberOfPersonVisiting",
    "FollowupsNormalized",
    "ProductPitchedInt",
    "PreferredPropertyStar",
    "NumberOfTripsInt",
    "Passport",
    "PitchSatisfactionScore",
    "DesignationInt",
    "MonthlyIncomeInt",
    "MaritalInt",
    "CarInt",
    "ChildInt",
]
# 目的変数を指定
target_col = "ProdTaken"

# データの読み込み
data = pd.read_csv("./mid_output/test_preprocessed.csv")


class Prediction:
    @classmethod
    def get_model(cls, inference_df):
        """Get model method

        Args:
            model_path (str): Path to the trained model directory.
            inference_df: Past data not subject to prediction.

        Returns:
            bool: The return value. True for success.
        """
        cls.n_splits = 5
        cls.model = {}
        for n in range(cls.n_splits):
            cls.model[n] = pickle.load(open(f"./model/catboost_model_{n}.pkl", "rb"))

        cls.data = inference_df

        return True

    @classmethod
    def predict(cls, input: pd.DataFrame):
        """Predict method

        Args:
            input: meta data of the sample you want to make inference from (DataFrame)

        Returns:
            prediction: Inference for the given input. Return columns must be ['datetime', 'start_code', 'end_code'](DataFrame).

        Tips:
            You can use past data by writing "cls.data".
        """
        prediction = input.copy()
        prediction["prediction"] = 0.0
        for n in range(cls.n_splits):
            prediction["prediction"] += cls.model[n].predict(prediction[feature_cols]) / cls.n_splits
        # 予測値が負の場合は0にする
        prediction["prediction"] = np.where(prediction["prediction"] < 0, 0, prediction["prediction"])
        prediction = prediction[["id", "prediction"]]
        prediction.to_csv("./output/prediction.csv", index=False, header=False)

        return prediction


prediction = Prediction()
prediction.get_model(data)
prediction.predict(data)
