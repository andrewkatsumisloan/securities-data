from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Basic Flask App"

@app.route('/about')
def about():
    return "About Page"

@app.route('/ticker_entry', methods=['GET', 'POST'])
def get_ticker_data():
    if request.method == 'POST':  
        ticker = request.args.get('ticker')
        df = pd.read_csv('../raw_data/individual/{0}.csv'.format(ticker))
        df = df.to_json(orient='records')
        return jsonify(df)
    else: 
        return

if __name__ == '__main__':
    app.run(debug=True)
