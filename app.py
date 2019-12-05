from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/info', methods=['POST'])
def info():
    apikey = '69b70c6a'
    imdb_search = request.form['imdb_search']
    r = requests.get('http://www.omdbapi.com/?apikey='+apikey+'&i='+imdb_search)
    json_object = r.json()

    ratings = json_object['Ratings']

    for rating in ratings:
        source = rating['Source']
        value = rating['Value']

    title = json_object['Title']
    year = json_object['Year']
    poster = json_object['Poster']
    rated = json_object['Rated']
    released = json_object['Released']
    plot = json_object['Plot']
    #return json_object
    return render_template('movie.html', title=title, year=year, poster=poster, rated=rated, released=released, plot=plot, ratings=ratings)


@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')