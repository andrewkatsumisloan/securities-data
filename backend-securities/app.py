from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Basic Flask App"

@app.route('/about')
def about():
    return "About Page"

@app.route('/ticker_entry', methods=['GET', 'POST'])
def get_ticker_data():
    if request.method == 'POST':  
        ticker = request.get_json(['ticker'])
        ticker = ticker['ticker']
        print('This endpoint hit')
        df = pd.read_csv('./sp_joined_closes.csv')
        print(df)
        # ticker = ticker.tostring()
        ret_val = df[ticker]
        ret_val = ret_val.to_json(orient='records')
        print(ret_val)
        return ret_val

    if request.method == 'GET':
        print('This endpoint hit')
        return 'This endpoint hit'

if __name__ == '__main__':
    app.run(debug=True)
