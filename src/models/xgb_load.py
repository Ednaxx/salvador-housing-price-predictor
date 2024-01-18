import joblib

model = {}

def load_model():
    global model
    model["xgboost"] = joblib.load("./models/xgb.pkl")

def clear_model():
    global model
    model.clear()
