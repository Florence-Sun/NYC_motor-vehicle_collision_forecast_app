from flask import Flask, render_template, request
from sklearn.externals import joblib
import pandas as pd
from data_process import data_wrangling
import requests

# #app initialization
app=Flask(__name__)

#load models
trend_model=joblib.load(open(app.static_folder + '/models/trend_model.pkl', 'rb'))
season_model=joblib.load(open(app.static_folder + '/models/season_model.pkl', 'rb'))


#main index page route
@app.route('/')
def home():
    return render_template('home.html')

#route for prediction of collision number model
@app.route('/predict', methods=['POST'])
def predict():

    #get text from the incoming request (submitted on predict button click)
    input_date=request.form['namequery']

    #request last Saturday's data from NYC Open data
    last_saturday = pd.to_datetime(input_date).strftime("%Y-%m-%dT00:00:00.000")
    params = {'crash_date': last_saturday}
    page = requests.get('https://data.cityofnewyork.us/resource/h9gi-nx95.json', params=params)

    if page.json():
        df = pd.DataFrame(page.json())
        #customed data wrangling module
        data_wrangle=data_wrangling()
        data_preprocess=data_wrangle.preprocess(df)
        manhattan=data_wrangle.Manhattan_select(data_preprocess)
        brooklyn=data_wrangle.Brooklyn_select(data_preprocess)
        queens=data_wrangle.Queens_select(data_preprocess)
        staten_island=data_wrangle.Staten_island_select(data_preprocess)
        bronx=data_wrangle.Bronx_select(data_preprocess)

        #predict manhattan
        manhattan['trend_model']=trend_model.predict(manhattan[['Julian', 'const']])
        manhattan['trend_model_error'] = manhattan['CRASH NUMBER'] - manhattan['trend_model']
        features_for_season_model=manhattan[['trend_model_error', 'sin(week)', \
                                        'cos(week)', 'sin(biweek)', 'cos(biweek)', \
                                        'sin(biyear)', 'cos(biyear)', 'sin(year)', 'cos(year)']]
        manhattan['Predicted_error_value'] = season_model.predict(features_for_season_model)
        manhattan['PREDICT NUMBER'] = manhattan['trend_model'] + manhattan['Predicted_error_value']
        manhattan_prediction=round(manhattan['PREDICT NUMBER'].values[0])

        #predict brooklyn
        brooklyn['trend_model'] = trend_model.predict(brooklyn[['Julian', 'const']])
        brooklyn['trend_model_error'] = brooklyn['CRASH NUMBER'] - brooklyn['trend_model']
        features_for_season_model_bro = brooklyn[['trend_model_error', 'sin(week)', \
                                               'cos(week)', 'sin(biweek)', 'cos(biweek)', \
                                               'sin(biyear)', 'cos(biyear)', 'sin(year)', 'cos(year)']]
        brooklyn['Predicted_error_value'] = season_model.predict(features_for_season_model_bro)
        brooklyn['PREDICT NUMBER'] = brooklyn['trend_model'] + brooklyn['Predicted_error_value']
        brooklyn_prediction = round(brooklyn['PREDICT NUMBER'].values[0])

        #predict queens
        queens['trend_model'] = trend_model.predict(queens[['Julian', 'const']])
        queens['trend_model_error'] = queens['CRASH NUMBER'] - queens['trend_model']
        features_for_season_model_que = queens[['trend_model_error', 'sin(week)', \
                                               'cos(week)', 'sin(biweek)', 'cos(biweek)', \
                                               'sin(biyear)', 'cos(biyear)', 'sin(year)', 'cos(year)']]
        queens['Predicted_error_value'] = season_model.predict(features_for_season_model_que)
        queens['PREDICT NUMBER'] = queens['trend_model'] + queens['Predicted_error_value']
        queens_prediction = round(queens['PREDICT NUMBER'].values[0])

        #predict staten_island
        staten_island['trend_model'] = trend_model.predict(staten_island[['Julian', 'const']])
        staten_island['trend_model_error'] = staten_island['CRASH NUMBER'] - staten_island['trend_model']
        features_for_season_model_stan = staten_island[['trend_model_error', 'sin(week)', \
                                                'cos(week)', 'sin(biweek)', 'cos(biweek)', \
                                                'sin(biyear)', 'cos(biyear)', 'sin(year)', 'cos(year)']]
        staten_island['Predicted_error_value'] = season_model.predict(features_for_season_model_stan)
        staten_island['PREDICT NUMBER'] = staten_island['trend_model'] + staten_island['Predicted_error_value']
        staten_island_prediction = round(staten_island['PREDICT NUMBER'].values[0])

        #predict bronx
        bronx['trend_model'] = trend_model.predict(bronx[['Julian', 'const']])
        bronx['trend_model_error'] = bronx['CRASH NUMBER'] - bronx['trend_model']
        features_for_season_model_brox = bronx[['trend_model_error', 'sin(week)', \
                                               'cos(week)', 'sin(biweek)', 'cos(biweek)', \
                                               'sin(biyear)', 'cos(biyear)', 'sin(year)', 'cos(year)']]
        bronx['Predicted_error_value'] = season_model.predict(features_for_season_model_brox)
        bronx['PREDICT NUMBER'] = bronx['trend_model'] + bronx['Predicted_error_value']
        bronx_prediction = round(bronx['PREDICT NUMBER'].values[0])


        return render_template('home.html', input_date=input_date, \
                               manhattan_prediction=manhattan_prediction, \
                               brooklyn_prediction=brooklyn_prediction, \
                               queens_prediction=queens_prediction, \
                               staten_island_prediction=staten_island_prediction, \
                               bronx_prediction=bronx_prediction)
    else:
        error_mesg="The input date is wrong. Please input any day from last week."
        return render_template('home.html', input_date=input_date, \
                               manhattan_prediction=error_mesg, \
                               brooklyn_prediction=error_mesg, \
                               queens_prediction=error_mesg, \
                               staten_island_prediction=error_mesg, \
                               bronx_prediction=error_mesg)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/model")
def model():
    return render_template('model.html')

if __name__=='__main__':
    app.run(debug=True)
