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
        # print('This is the request: ', request)
        ticker = request.get_json(['ticker'])
        ticker = ticker['ticker']
        df = pd.read_csv('./sp_joined_closes.csv')

        # print(df)
        trimmed_df = (df[[ticker, 'datetime']].dropna())
        print(trimmed_df)

        dates = trimmed_df['datetime'].tolist()
        values = trimmed_df[ticker].tolist()

        ret_list = []
        for i, x in enumerate(dates): 
            ret_list.append({'date': x, 'value': values[i]})

        return jsonify(ret_list)
        # ret_json = jsonify({'dates': dates,
        #                     'values': values})
        # print(ret_json)
        # return ret_json
        

    if request.method == 'GET':
        print('This endpoint hit')
        return 'This endpoint hit'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
