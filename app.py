from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('trained_pipeline-0.1.0.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Identify', methods=['POST'])
def predict_language():
    input_text = request.form.get('input_text')

    # Ensure input_text is in the correct format (an iterable containing a single string)
    input_text_list = [input_text]

    # Prediction
    result = model.predict(input_text_list)

    if result[0]==0:
        result='Arabic'
    if result[0] == 1:
        result = 'Danish'
    if result[0] == 2:
        result = 'Dutch'
    if result[0] == 3:
        result = 'English'
    if result[0] == 4:
        result = 'French'
    if result[0] == 5:
        result = 'German'
    if result[0] ==6:
        result = 'Greek'
    if result[0] == 7:
        result = 'Hindi'
    if result[0] == 8:
        result = 'Italian'
    if result[0] == 9:
        result = 'kannada'
    if result[0] == 10:
        result = 'Malayalam'
    if result[0] == 11:
        result = 'Portugeese'
    if result[0] == 12:
        result = 'Russian'
    if result[0] == 13:
        result = 'Spanish'
    if result[0] == 14:
        result = 'Sweedish'
    if result[0] == 15:
        result = 'Tamil'
    if result[0] == 16:
        result = 'Turkish'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
