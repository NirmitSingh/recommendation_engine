import numpy as np
from flask import Flask, render_template, redirect, url_for, request
import joblib
import pandas as pd

app = Flask(__name__)  


def give_rec(title, sig):
    final_df=pd.read_csv('gamerec.csv')
    indices = pd.Series(final_df.index, index=final_df['name']).drop_duplicates()
    idx = indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True) 
    sig_scores = sig_scores[1:11]
    game_indices = [i[0] for i in sig_scores]
    return list(final_df['name'].iloc[game_indices])


@app.route('/', methods=['GET', 'POST'])
def home():
   
    return render_template('index.html')

@app.route('/pred', methods=['GET', 'POST'])
def show():
    name=None
    if request.method == 'POST':
        name=request.form['name']
        obj = joblib.load('filename.pkl')
        ans=give_rec(name,obj)



    return render_template('home.html',games=ans)


if __name__ == "__main__":  
	app.run(debug=True)  
 
