
import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('best_model_SVM.pkl', 'rb'))


prediction_mapping = {1: 'Presence', 0: 'Absence'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    pour l'affichage sur html
    '''

    features = request.form.to_dict()
    features = list(features.values())
    features = list(map(int, features))
    final_features = np.array(features).reshape(1, 12)
    prediction = model.predict(final_features)

 
    decoded_prediction = prediction_mapping.get(prediction[0], 'Unknown')

    return render_template('index.html', prediction_text='Heart disease situation: {}'.format(decoded_prediction))

if __name__ == "__main__":
    app.run(debug=False, port=8082)
