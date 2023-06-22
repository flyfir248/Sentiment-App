import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from langdetect import detect
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import PyPDF2
import docx
import spacy
from spacy import displacy
import tempfile
import os

nltk.download("vader_lexicon")
nltk.download("punkt")
st.set_page_config(page_title="Streamlit Sentiment App", page_icon="static/res/favicon.png")

def extract_text_from_document(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    return text


def predict_sentiment(text, language, threshold_positive, threshold_negative):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = {}

    if language == 'en':
        sentiment_scores = sid.polarity_scores(text)

    elif language == 'es':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'af':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ar':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'bg':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'bn':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ca':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'cs':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'cy':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'da':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'de':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'el':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'et':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'fa':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'fi':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'fr':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'gu':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'he':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'hi':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'hr':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'hu':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'id':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'it':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ja':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'kn':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ko':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'lt':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'lv':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'mk':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ml':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'mr':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ne':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'nl':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'no':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'pa':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'pl':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'pt':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ro':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ru':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'sk':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'sl':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'so':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'sq':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'sv':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'sw':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ta':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'te':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'th':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'tl':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'tr':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'uk':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'ur':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'vi':
        sentiment_scores = sid.polarity_scores(text)

    elif language == 'zh-cn':
        sentiment_scores = sid.polarity_scores(text)
    elif language == 'zh-tw':
        sentiment_scores = sid.polarity_scores(text)
    # ... add conditions for other languages

    # ... add conditions for other languages

    threshold_positive = float(threshold_positive)
    threshold_negative = float(threshold_negative)

    if sentiment_scores.get("compound", 0) >= threshold_positive:
        sentiment = "Positive"
        sentiment_color = "#03fc1c"
        sentiment_size = "15px"
        sentiment_weight = "normal"
    elif sentiment_scores.get("compound", 0) <= threshold_negative:
        sentiment = "Negative"
        sentiment_color = "#ff050d"
        sentiment_size = "15px"
        sentiment_weight = "bold"
    else:
        sentiment = "Neutral"
        sentiment_color = "#f2f8fc"
        sentiment_size = "15px"
        sentiment_weight = "normal"

    confidence_score = sentiment_scores.get("compound", 0) * 100
    confidence_score = round(confidence_score, 2)

    return sentiment, sentiment_color, sentiment_size, sentiment_weight, confidence_score


def main():
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    st.title("Sentiment Analysis App ❤️🔥")
    default_text = "I am feeling great today!"
    texts = st.text_area("Enter multiple texts (separated by line breaks):", value=default_text, height=200)
    text_list = texts.split("\n")

    uploaded_file = st.file_uploader("Upload a document:", type=["pdf", "docx"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_path = temp_file.name
        document_text = extract_text_from_document(temp_path)
        text_list.extend(document_text.split("\n"))
        os.remove(temp_path)

    selected_language = st.selectbox("Select the language of the text:", ["English", "Spanish",'Afrikaans','Arabic','Bulgarian','Bengali','Catalan','Czech','Welsh','Danish','German','Greek','English','Spanish','Estonian','Persian (Farsi)','Finnish','French','Gujarati','Hebrew','Hindi','Croatian','Hungarian','Indonesian','Italian','Japanese','Kannada','Korean','Lithuanian','Latvian','Macedonian','Malayalam','Marathi','Nepali','Dutch','Norwegian','Punjabi','Polish','Portuguese','Romanian','Russian','Slovak','Slovenian','Somali','Albanian','Swedish','Swahili','Tamil','Telugu','Thai','Tagalog','Turkish','Ukrainian','Urdu','Vietnamese','Chinese (Simplified)','Chinese (Traditional)'])

    if st.button("Analyze"):
        sentiment_data = []
        for text in text_list:
            language = detect(text) if selected_language == "English" else "es"
            sentiment, sentiment_color, sentiment_size, sentiment_weight, confidence_score = predict_sentiment(
                text, language, st.session_state.threshold_positive, st.session_state.threshold_negative
            )
            sentiment_data.append([text, sentiment, confidence_score])

        sentiment_df = pd.DataFrame(sentiment_data, columns=["Text", "Sentiment", "Confidence Score"])
        st.dataframe(sentiment_df)

        # Plotting sentiment distribution
        sentiment_counts = sentiment_df["Sentiment"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    # Sidebar for setting thresholds
    st.sidebar.title("Settings")
    st.sidebar.subheader("Thresholds")
    threshold_positive = st.sidebar.number_input("Positive threshold:", min_value=0.0, max_value=1.0, step=0.1, value=0.3)
    threshold_negative = st.sidebar.number_input("Negative threshold:", min_value=0.0, max_value=1.0, step=0.1, value=-0.3)
    st.session_state.threshold_positive = threshold_positive
    st.session_state.threshold_negative = threshold_negative

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

if __name__ == "__main__":
    main()
