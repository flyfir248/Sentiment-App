import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
st.set_page_config(page_title="Streamlit Sentiment App", page_icon="static/res/favicon.png")

def predict_sentiment(text):
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

    return sentiment, sentiment_color, sentiment_size, sentiment_weight

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
    #text = st.text_area('Enter text:')
    default_text = "I am feeling great today!"
    text = st.text_area('Enter text:', value=default_text)
    if st.button('Predict Sentiment'):
        sentiment, sentiment_color, sentiment_size, sentiment_weight = predict_sentiment(text)
        st.markdown(
            f'<p style="color: {sentiment_color}; font-size: {sentiment_size}; font-weight: {sentiment_weight};">'
            f'Predicted Sentiment: {sentiment}'
            '</p>',
            unsafe_allow_html=True
        )
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
