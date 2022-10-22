#this save the model as py file
# Import libraries
import gzip
import json
import pickle

import pandas as pd


# Add wrangle function from lesson 5.4
def wrangle(filename):
    # Open compressed file, load into dictionary
    with gzip.open(filename,"r") as f:
        data=json.load(f)
    # Load dictionary into DataFrame, set index
    df=pd.DataFrame().from_dict(data["data"]).set_index("company_id")
    
    
    return df


# Add make_predictions function from lesson 5.3
def make_predictions(data_filepath, model_filepath):
    # Wrangle JSON file
    X_test = wrangle(data_filepath)
    # Load model
    with open(model_filepath,"rb") as f:
        model=pickle.load(f)
    # Generate predictions
    y_test_pred = model.predict(X_test)
    # Put predictions into Series with name "bankrupt", and same index as X_test
    y_test_pred = pd.Series(y_test_pred,index=X_test.index,name="bankrupt")
    return y_test_pred




#now load your saved module
# Import your module
from my_predictor_lesson import make_predictions

# Generate predictions
y_test_pred = make_predictions(
    data_filepath="data/poland-bankruptcy-data-2009-mvp-features.json.gz",
    model_filepath="model-5-4.pkl",
)

print("predictions shape:", y_test_pred.shape)
y_test_pred.head()