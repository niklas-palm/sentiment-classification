import pickle

import model.helper_methods as help

def get_model_api():
    """Returns lambda function for api"""
    # 1. initialize model once and for all
    model = help.model
    probs_model = help.prob_model

    def model_api(input_data):
        cleaned = help.cleanTweet(input_data)
        vector = help.getVector(cleaned)
        pred = model.predict(vector) # Get prediction
        probs = probs_model.predict_proba(vector) # Get class probs

        return pred, probs

    return model_api
