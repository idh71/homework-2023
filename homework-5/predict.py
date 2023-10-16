import pickle
import pandas as pd
from flask import Flask, request, jsonify

# with open('model1.bin', 'rb') as model_file:
#     model = pickle.load(model_file)

# with open('dv.bin', 'rb') as dv_file:
#     dv = pickle.load(dv_file)

# I used the above for question 5 but I am changing it for the new model used 
# in question 6
with open('model2.bin', 'rb') as model_file:
    model = pickle.load(model_file)

with open('dv.bin', 'rb') as dv_file:
    dv = pickle.load(dv_file)

app = Flask("churn")


client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

@app.route('/predict', methods=['POST'])
# def predict(client, dv=dv, model=model):
def predict(dv=dv, model=model):

    client = request.get_json()
    client = dv.transform(client)
    pred = model.predict_proba(client)[:, 1]

    churn = pred >= 0.5
    
    result = {
        'churn_probability': float(pred), ## we need to conver numpy data into python data in flask framework
        'churn': bool(churn),  ## same as the line above, converting the data using bool method
    }
    
    # return jsonify(pred)
    return jsonify(result)





if __name__ == "__main__":
    # print(predict(client, dv, model))
    app.run(debug=True, host='0.0.0.0', port=9696)