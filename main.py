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

import nlp as nlp

nltk.download("vader_lexicon")
nltk.download("punkt")
st.set_page_config(page_title="Streamlit Sentiment App", page_icon="static/res/favicon.png")
#st.set_page_config(page_title="Streamlit Sentiment App", page_icon="static/res/favicon.png", background='#1a1a1a')


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

    if language == "en":
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        entities = []
        for entity in doc.ents:
            entities.append(entity.text)
        sentiment_scores = sid.polarity_scores(text)
        sentiment_scores["entities"] = entities
    elif language == "es":
        # Perform sentiment analysis in Spanish with entity recognition
        pass
    elif language == "af":
        # Perform sentiment analysis in Afrikaans with entity recognition
        pass
    elif language == "ar":
        # Perform sentiment analysis in Arabic with entity recognition
        pass
    elif language == "bg":
        # Perform sentiment analysis in Bulgarian with entity recognition
        pass

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

    supported_languages = [
        "Afrikaans",
        "Arabic",
        "Bulgarian",
        "Bengali",
        "Catalan",
        "Czech",
        "Welsh",
        "Danish",
        "German",
        "Greek",
        "English",
        "Spanish",
        "Estonian",
        "Persian (Farsi)",
        "Finnish",
        "French",
        "Gujarati",
        "Hebrew",
        "Hindi",
        "Croatian",
        "Hungarian",
        "Indonesian",
        "Italian",
        "Japanese",
        "Kannada",
        "Korean",
        "Lithuanian",
        "Latvian",
        "Macedonian",
        "Malayalam",
        "Marathi",
        "Nepali",
        "Dutch",
        "Norwegian",
        "Punjabi",
        "Polish",
        "Portuguese",
        "Romanian",
        "Russian",
        "Slovak",
        "Slovenian",
        "Somali",
        "Albanian",
        "Swedish",
        "Swahili",
        "Tamil",
        "Telugu",
        "Thai",
        "Tagalog",
        "Turkish",
        "Ukrainian",
        "Urdu",
        "Vietnamese",
        "Chinese (Simplified)",
        "Chinese (Traditional)",
    ]

    selected_language = st.selectbox("Select the language of the texts:", supported_languages)

    threshold_positive = st.number_input("Threshold for Positive Sentiment:", value=0.05, step=0.01)
    threshold_negative = st.number_input("Threshold for Negative Sentiment:", value=-0.05, step=0.01)

    sentiment_data = []
    for text in text_list:
        if text.strip() != "":
            language = selected_language if selected_language != "auto" else detect(text)
            sentiment, sentiment_color, sentiment_size, sentiment_weight, confidence_score = predict_sentiment(
                text, language, threshold_positive, threshold_negative
            )
            sentiment_data.append([text, sentiment, confidence_score])

    uploaded_files = st.file_uploader("Upload Documents", accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            text = extract_text_from_document(file.name)
            if text.strip() != "":
                language = selected_language if selected_language != "auto" else detect(text)
                sentiment, sentiment_color, sentiment_size, sentiment_weight, confidence_score = predict_sentiment(
                    text, language, threshold_positive, threshold_negative
                )
                sentiment_data.append([text, sentiment, confidence_score])

    if st.button("Predict Sentiments"):
        if sentiment_data:
            df = pd.DataFrame(sentiment_data, columns=["Text", "Sentiment", "Confidence Score"])
            st.table(df)

            sentiment_counts = df["Sentiment"].value_counts()
            labels = sentiment_counts.index.tolist()
            sizes = sentiment_counts.tolist()

            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            ax.set_title("Sentiment Distribution")

            st.pyplot(fig)
        else:
            st.warning("Please enter some texts to analyze.")

    show_entities = st.checkbox("Show Entities")
    if show_entities:
        for _, row in df.iterrows():
            entities = row["Entities"]
            if entities:
                doc = nlp(row["Text"])
                displacy.render(doc, style="ent", jupyter=False)
                plt.title("Entities")
                plt.axis("off")
                plt.show()

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

sentiment_history = []

if __name__ == "__main__":
    main()
