from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import requests

app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/weather"
mongo = PyMongo(app)

@app.route('/info', methods=['POST'])
def info():
    apikey = '1b4b3ef1-ae42-4636-8cc1-5c44c1fed7c8'
    location_search = request.form['location_search']
    r = requests.get('http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/'+location_search+'?res=hourly&time=2019-12-12T00:00:00Z&key='+apikey)
    #return ('http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/'+location_search+'?res=hourly&time=2019-12-12T00:00:00Z&key='+apikey)
    json_object = r.json()

    sitereps = json_object['SiteRep']
    current_location = 'false'

    for siterep in sitereps:
        dvs = sitereps['DV']
        for dv in dvs:
            locations = dvs['Location']    
            for location in locations:
                periods = locations['Period']
                name = locations['name']
                for period in periods:
                    reps = periods['Rep']
                    time = periods['value']
                    for rep in reps:
                        temperature = reps['T']
                        weather = reps['W']

        #return siterep
    return render_template('weather.html', name=name, time=time, temperature=temperature, weather=weather, \
        dvs=dvs, locations=locations, periods=periods, reps=reps, sitereps=sitereps)

    if request.method == 'POST':
        fav = mongo.db.favLocations.insert({'location_search': location_search, 'name': name, \
            'temperature': temperature, 'weather': weather, 'current_location': current_location})
        resp = 'Added to Favourites'
        return resp
    

    #return name

'''@app.route('/delete/<id>', methods=['POST'])
def delete_location(location_search):
    mongo.db.favLocations.delete_one({'location_search': location_search})
    return userfavs()

@app.route('/current/<id>', methods=['POST'])
def current_location(location_search):
    mongo.db.favLocations.update({'location_search':location_search},{ '$set':{'current_location': 'true'}})
    return userFavs()

@app.route('/uncurrent/<id>', methods=['POST'])
def unwatch_movie(location_search):
    mongo.db.favLocations.update({'location_search':location_search},{ '$set':{'current_location': 'false'}})
    return userFavs()

@app.route('/userFavs')
def userFavs():
    favLocations = mongo.db.favLocations.find()
    return render_template('favLocations.html', favLocations=favLocations)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')'''