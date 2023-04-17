# app.py

from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def predict():
   
    dong = request.form['dong']
    area = float(request.form['area'])
    usage = request.form['usage']

    with open('model2.pkl', 'rb') as file:
        model, cols = pickle.load(file)

    
    input_df = pd.DataFrame({'법정동명': [dong], '임대면적(㎡)': [area], '건물용도': [usage]})
    input_df = pd.get_dummies(input_df, columns=['법정동명', '건물용도'], drop_first=True)
    input_df = input_df.reindex(columns=cols, fill_value=0)

    
    prediction = model.predict(input_df)[0]

    return render_template('result.html', result=prediction)

if __name__ == '__main__':
    app.run(debug=True)