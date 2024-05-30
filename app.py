from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Load model
model = pickle.load(open('online_fraud_detection_model.pkl', 'rb'))


# create flask app

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    type = int(request.form['type'])
    amount = float(request.form['amount'])
    old_balance_org = float(request.form['oldbalanceOrg'])
    new_balance_org = float(request.form['newbalanceOrig'])
    old_balance_dest = float(request.form['oldbalanceDest'])
    new_balance_dest = float(request.form['newbalanceDest'])

    feature_list = [type, amount, old_balance_org,
                    new_balance_org, old_balance_dest, new_balance_dest]
    single_pred = np.array(feature_list).reshape(1, -1)

    predict = model.predict(single_pred)

    fraud_dict = {1: 'Fraud', 0: 'Not Fraud'}
    fraud = fraud_dict.get(predict[0], 'Unknown')

    result = f"This payment is {fraud}"

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
