from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/info', methods=['POST'])
def info():
    apikey = '1b4b3ef1-ae42-4636-8cc1-5c44c1fed7c8'
    location_search = request.form['location_search']
    r = requests.get('http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/'+location_search+'?res=hourly&key='+apikey)
    json_object = r.json()

    siterep = json_object['SiteRep']
    dv = siterep['DV']
    location = dv['Location']
    period = location['Period']
    rep = period['Rep']

    for siterep in siterep:
        for dv in dv:
            for location in location:
                name = json_object['name']
                for period in period:
                    time = json_object['value']
                    for rep in rep:
                        temperature = json_object['T']
                        weather = json_object['W']
    #return siterep
    return render_template('movie.html', name=name, time=time, temperature=temperature, weather=weather, dv=dv, location=location, period=period, rep=rep, siterep=siterep)


@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')