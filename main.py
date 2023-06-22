import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from langdetect import detect
import nltk
import pandas as pd
import matplotlib.pyplot as plt

nltk.download('vader_lexicon')
nltk.download('punkt')
st.set_page_config(page_title="Streamlit Sentiment App", page_icon="static/res/favicon.png")


def predict_sentiment(text, language):
    sid = SentimentIntensityAnalyzer()

    if language == 'en':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'es':
        sid_spanish = SentimentIntensityAnalyzer()
        sentiment_scores = sid_spanish.polarity_scores(text)
    # Add more elif conditions for other languages
    elif language == 'af':
        # Load sentiment analysis model for Afrikaans
        sid_afrikaans = SentimentIntensityAnalyzer()
        sentiment_scores = sid_afrikaans.polarity_scores(text)
    elif language == 'ar':
        # Load sentiment analysis model for Arabic
        sid_arabic = SentimentIntensityAnalyzer()
        sentiment_scores = sid_arabic.polarity_scores(text)
    elif language == 'bg':
        # Load sentiment analysis model for Bulgarian
        sid_bulgarian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_bulgarian.polarity_scores(text)
    # Add more elif conditions for other languages

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

    confidence_score = sentiment_scores['compound'] * 100  # Calculate confidence score
    confidence_score = round(confidence_score, 2)  # Round the confidence score to two decimal places

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

    supported_languages = ['af', 'ar', 'bg', 'bn', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'fa', 'fi',
                           'fr', 'gu', 'he', 'hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv', 'mk', 'ml',
                           'mr', 'ne', 'nl', 'no', 'pa', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'so', 'sq', 'sv', 'sw',
                           'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'zh-cn', 'zh-tw']

    selected_language = st.selectbox('Select the language of the texts:', supported_languages)

    sentiment_data = []
    for text in text_list:
        if text.strip() != '':
            language = selected_language if selected_language != 'auto' else detect(text)
            sentiment, sentiment_color, sentiment_size, sentiment_weight, confidence_score = predict_sentiment(text,
                                                                                                               language)
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
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_title('Sentiment Distribution')

            st.pyplot(fig)
        else:
            st.warning('Please enter some texts to analyze.')

    st.markdown(
        '''
        <style>
            .center-image {
                display: flex;
                justify-content: center;
            }
            .follow-me {
                text-align: center;
            }
            .social-icons {
                display: flex;
                justify-content: center;
                list-style: none;
                padding: 0;
            }
            .social-icons li {
                margin: 0 10px;
            }
        </style>
        <body>
            <div class="center-image">
                <h4>Anoop Johny 🤖</h4>
            </div>
            <div class="center-image">
                <h4>Follow Me</h4>
            </div>
            <div class="center-image">
                <ul class="social-icons">
                    <li><a href="https://www.linkedin.com/in/anoop-johny-30a746181/"><img src="https://pythonpythonme.netlify.app/static/res/linkedin.png" width="55" height="55" alt="LinkedIn"></a></li>
                    <li><a href="https://github.com/flyfir248"><img src="https://pythonpythonme.netlify.app/static/res/github.png" width="55" height="55" alt="GitHub"></a></li>
                    <li><a href="https://pythonpythonme.netlify.app/index.html"><img src="https://pythonpythonme.netlify.app/static/res/web.png" width="55" height="55" alt="Website"></a></li>
                    <li><a href="https://medium.com/@anoopjohny2000"><img src="https://pythonpythonme.netlify.app/static/res/medium.png" width="55" height="55" alt="Medium"></a></li>
                    <li><a href="https://www.kooapp.com/profile/anoop2DEVLJ"><img src="https://www.kooapp.com/_next/static/media/logoKuSolidOutline.1f4fa971.svg" width="55" height="55" alt="The Koo App" width="55" height="55"></a></li>
                </ul>
            </div>
            <footer class="footer">
                <div class="container">
                    <div class="row">
                        <div class="center-image">
                            <p class="text-muted">© 2023-2024 PythonPythonME.</p>
                            <p>All rights reserved.</p>
                        </div>
                    </div>
                </div>
            </footer>
        </body>
        ''',
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    main()
