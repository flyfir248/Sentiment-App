import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from langdetect import detect
import nltk
import pandas as pd
import matplotlib.pyplot as plt


nltk.download('vader_lexicon')
nltk.download('punkt')
st.set_page_config(page_title="Streamlit Sentiment App", page_icon="static/res/favicon.png")


def predict_sentiment(text, language, threshold_positive, threshold_negative):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = {}  # Initialize with an empty dictionary

    if language == 'en':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'es':
        sid_spanish = SentimentIntensityAnalyzer()
        sentiment_scores = sid_spanish.polarity_scores(text)
    elif language == 'af':
        sid_afrikaans = SentimentIntensityAnalyzer()
        sentiment_scores = sid_afrikaans.polarity_scores(text)
    elif language == 'ar':
        sid_arabic = SentimentIntensityAnalyzer()
        sentiment_scores = sid_arabic.polarity_scores(text)
    elif language == 'bg':
        sid_bulgarian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_bulgarian.polarity_scores(text)
    # Add more elif conditions for other languages

    threshold_positive = float(threshold_positive)
    threshold_negative = float(threshold_negative)

    if sentiment_scores.get('compound', 0) >= threshold_positive:
        sentiment = 'Positive'
        sentiment_color = '#03fc1c'
        sentiment_size = '15px'
        sentiment_weight = 'normal'
    elif sentiment_scores.get('compound', 0) <= threshold_negative:
        sentiment = 'Negative'
        sentiment_color = '#ff050d'
        sentiment_size = '15px'
        sentiment_weight = 'bold'
    else:
        sentiment = 'Neutral'
        sentiment_color = '#f2f8fc'
        sentiment_size = '15px'
        sentiment_weight = 'normal'

    confidence_score = sentiment_scores.get('compound', 0) * 100
    confidence_score = round(confidence_score, 2)

    return sentiment, sentiment_color, sentiment_size, sentiment_weight, confidence_score



def main():
    st.markdown(
        '''
        <style>
            .center-image {
                display: flex;
                justify-content: center;
            }
        </style>
        <a href="https://pythonpythonme.netlify.app/index.html">
        <div class="center-image">
        <img src="https://pythonpythonme.netlify.app/PythonPythonME.png" alt="Header image">
        </div>
        </a>
        <p></p>
        <p></p>
        ''',
        unsafe_allow_html=True
    )

    st.title('Sentiment Analysis App ❤️🔥')
    default_text = "I am feeling great today!"
    texts = st.text_area('Enter multiple texts (separated by line breaks):', value=default_text, height=200)
    text_list = texts.split('\n')

    supported_languages = [
        'Afrikaans',
        'Arabic',
        'Bulgarian',
        'Bengali',
        'Catalan',
        'Czech',
        'Welsh',
        'Danish',
        'German',
        'Greek',
        'English',
        'Spanish',
        'Estonian',
        'Persian (Farsi)',
        'Finnish',
        'French',
        'Gujarati',
        'Hebrew',
        'Hindi',
        'Croatian',
        'Hungarian',
        'Indonesian',
        'Italian',
        'Japanese',
        'Kannada',
        'Korean',
        'Lithuanian',
        'Latvian',
        'Macedonian',
        'Malayalam',
        'Marathi',
        'Nepali',
        'Dutch',
        'Norwegian',
        'Punjabi',
        'Polish',
        'Portuguese',
        'Romanian',
        'Russian',
        'Slovak',
        'Slovenian',
        'Somali',
        'Albanian',
        'Swedish',
        'Swahili',
        'Tamil',
        'Telugu',
        'Thai',
        'Tagalog',
        'Turkish',
        'Ukrainian',
        'Urdu',
        'Vietnamese',
        'Chinese (Simplified)',
        'Chinese (Traditional)'
    ]

    selected_language = st.selectbox('Select the language of the texts:', supported_languages)

    threshold_positive = st.number_input("Threshold for Positive Sentiment:", value=0.05, step=0.01)
    threshold_negative = st.number_input("Threshold for Negative Sentiment:", value=-0.05, step=0.01)

    sentiment_data = []
    for text in text_list:
        if text.strip() != '':
            language = selected_language if selected_language != 'auto' else detect(text)
            sentiment, sentiment_color, sentiment_size, sentiment_weight, confidence_score = predict_sentiment(text,
                                                                                                               language,
                                                                                                               threshold_positive,
                                                                                                               threshold_negative)
            sentiment_data.append([text, sentiment, confidence_score])

    if st.button('Predict Sentiments'):
        if sentiment_data:
            df = pd.DataFrame(sentiment_data, columns=['Text', 'Sentiment', 'Confidence Score'])
            st.table(df)

            sentiment_counts = df['Sentiment'].value_counts()
            labels = sentiment_counts.index.tolist()
            sizes = sentiment_counts.tolist()

            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            ax.set_title('Sentiment Distribution')

            st.pyplot(fig)
        else:
            st.warning('Please enter some texts to analyze.')

    show_history = st.checkbox("Show Sentiment Analysis History")
    if show_history:
        sentiment_history_df = pd.DataFrame(sentiment_history, columns=['Text', 'Sentiment', 'Confidence Score'])
        st.subheader("Sentiment Analysis History")
        st.table(sentiment_history_df)


sentiment_history = []

if __name__ == '__main__':
    main()
