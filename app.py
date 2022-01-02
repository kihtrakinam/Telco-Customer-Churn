import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final_features = [[int(int_features[0]), 1 if int_features[1] == 'One Year' else 0, 1 if int_features[1] == 'Two Year' else 0,
    1 if 'OS' in int_features else 0, 1 if 'TS' in int_features else 0, 1 if int_features[4] == 'Fiber optic' else 0,
    1 if int_features[2] == 'Electronic check' else 0, 1 if 'OB' in int_features else 0, 1 if 'SM' in int_features else 0,
    1 if int_features[4] == 'Not subscribed' else 0, 1 if 'ST' in int_features else 0, 1 if 'PB' in int_features else 0,
    1 if 'SC' in int_features else 0, 1 if int_features[3] == 'Not subscribed' else 0, 1 if int_features[3] == 'Multiple Lines' else 0]]

    prediction = np.squeeze(model.predict(final_features))
    output = 'Risk' if prediction == 1 else 'Safe'

    return render_template('index.html', prediction_text='Prediction : {}'.format(output))

@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
