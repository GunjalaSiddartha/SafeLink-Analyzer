
from tensorflow import keras
import numpy as np
from Feature_Extractor import extract_features
# ------------------------------------------------------------------------

# This function takes the url and returns probability value

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = np.array([url_features])
    print(url_features)

    print("Making prediction...")
    prediction = model.predict([url_features])

    i = prediction[0][0] * 100
    i = round(i,3)
    print("There is ",i,"% chance,the url is malicious !")

    return i
