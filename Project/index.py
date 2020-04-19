from flask import Flask
from flask import render_template
from flask import jsonify

from hotel_recommendation import summarize
from feature_extraction import extract_reviews

app = Flask(__name__)

@app.route('/suggest')
def home():
    details = summarize()
    hotels = details[0]
    reviews = details[1] 
    scores = details[2]
    return jsonify(hotels, reviews, scores) #'index.html', hotels=hotels, len_hotel=len(hotels),reviews=reviews)

def recommendBy(filterName):
    details = extract_reviews(filterName)
    return jsonify(details[0], details[1], details[2])

@app.route('/suggest/food')
def filterByFood():
    return recommendBy('food')


@app.route('/suggest/stay')
def filterByStay():
    return recommendBy('stay')


@app.route('/suggest/service')
def filterByService():
    return recommendBy('service')


@app.route('/suggest/room')
def filterByRoom():
    return recommendBy('room')


if __name__ =='__main__':
    app.run(debug=True)
