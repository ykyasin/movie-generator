from application import app, db 
from flask import render_template, jsonify, request
import requests

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    weather = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)


@app.route('/')
@app.route('/home')
def home():
    ip_address = request.environ['HTTP_X_FORWARDED_FOR']

    location_response = requests.post('http://movie-gen_location_service:5000/location', data=ip_address)
    location_response = location_response.json()
    weather_response = requests.post('http://movie-gen_weather_service:5000/weather', json=location_response)
    #movie_response = requests.post("http://movie-gen_movie_service:5000/movie", data=weather_response.text)
    movie_response = "Avengers"

    #new_movie = Movies(name=movie_response.text,weather=weather_response.text,location=location_response.text)
    #db.session.add(new_movie)
    #db.session.commit()

    return render_template('index.html', location=location_response.json()["city"], weather=weather_response.json()["weather"][0]["main"], movie=movie_response)