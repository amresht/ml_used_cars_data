from flask import Flask, render_template, jsonify,  request
import pickle 
import numpy as np

# read the pickle
model = pickle.load(open('sp.pkl', 'rb'))


#initialize the flask app
app = Flask(__name__)

@app.route('/',methods=["GET"])
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        # Get html form data
        car_age = int(request.form['car_age'])
        current_price = float(request.form['current_price'])
        kms = int(request.form['kms'])
        owner = int(request.form['owner'])
        fuel_type = int(request.form['fuel_type'])
        seller_type = int(request.form['seller_type'])
        transmission = int(request.form['transmission'])
    
    # Make prediction
    prediction = model.predict([[current_price, kms, fuel_type, seller_type, transmission, owner, car_age]])
    
    # Display prediction on index.html
    return render_template('index.html', prediction_text='Predicted Selling Price: {:.2f} lakhs'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)