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

@app.route('/get_heatmap', methods=['GET', 'POST'])
def correlation():
    """
    Creates a correlation table from a given list of SP500 companies.
    :param list: List containing ticker symbols as strings
    :return: correlation table with heatmap
    """
    if request.method == 'POST':
        print(request.get_json('HeatMapInput'))
        heatmapinput = request.get_json('HeatMapInput').values()
        ticker_list = list(heatmapinput)
        main_df = pd.read_csv('./sp_joined_closes.csv')
        # print(main_df)
        df = pd.DataFrame()

        for a in range(len(ticker_list)):
            array = main_df[ticker_list[a]].values
            df['{}'.format(ticker_list[a])] = array

        corr_table = df.corr().to_dict()
    
        # print(corr_table)
        return corr_table


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
