from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

app = Flask(__name__)

nltk.download('vader_lexicon')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    text = request.form['text']
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
        sentiment_color = '#03fc1c'
        sentiment_size = '15px'
        sentiment_weight = 'normal'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
        sentiment_color = '#ff050d'
        sentiment_size = '15px'
        sentiment_weight = 'bold'
    else:
        sentiment = 'Neutral'
        sentiment_color = '#f2f8fc'
        sentiment_size = '15px'
        sentiment_weight = 'normal'

    return render_template('index.html', sentiment=sentiment, sentiment_color=sentiment_color, sentiment_size=sentiment_size, sentiment_weight=sentiment_weight)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)