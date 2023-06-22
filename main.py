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

    elif language == 'bn':
        sid_Bengali = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Bengali.polarity_scores(text)

    elif language == 'ca':
        sid_Catalan = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Catalan.polarity_scores(text)

    elif language == 'cs':
        sid_Czech = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Czech.polarity_scores(text)

    elif language == 'cy':
        sid_Welsh = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Welsh.polarity_scores(text)

    elif language == 'da':
        sid_Danish = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Danish.polarity_scores(text)

    elif language == 'de':
        sid_German = SentimentIntensityAnalyzer()
        sentiment_scores = sid_German.polarity_scores(text)

    elif language == 'el':
        sid_Czech = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Czech.polarity_scores(text)

    elif language == 'et':
        sid_Estonian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Estonian.polarity_scores(text)

    elif language == 'fa':
        sid_Persian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Persian.polarity_scores(text)

    elif language == 'fi':
        sid_Finnish = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Finnish.polarity_scores(text)

    elif language == 'fr':
        sid_French = SentimentIntensityAnalyzer()
        sentiment_scores = sid_French.polarity_scores(text)

    elif language == 'gu':
        sid_Gujarati = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Gujarati.polarity_scores(text)

    elif language == 'he':
        sid_Hebrew = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Hebrew.polarity_scores(text)

    elif language == 'hi':
        sid_Hindi = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Hindi.polarity_scores(text)

    elif language == 'hr':
        sid_Croatian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Croatian.polarity_scores(text)

    elif language == 'hu':
        sid_Hungarian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Hungarian.polarity_scores(text)

    elif language == 'id':
        sid_Indonesian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Indonesian.polarity_scores(text)

    elif language == 'it':
        sid_Italian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Italian.polarity_scores(text)

    elif language == 'ja':
        sid_Japanese = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Japanese.polarity_scores(text)

    elif language == 'kn':
        sid_Kannada = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Kannada.polarity_scores(text)

    elif language == 'ko':
        sid_Korean = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Korean.polarity_scores(text)

    elif language == 'lt':
        sid_Lithuanian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Lithuanian.polarity_scores(text)

    elif language == 'lv':
        sid_Latvian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Latvian.polarity_scores(text)

    elif language == 'mk':
        sid_Macedonian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Macedonian.polarity_scores(text)

    elif language == 'ml':
        sid_Malayalam = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Malayalam.polarity_scores(text)

    elif language == 'mr':
        sid_Marathi = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Marathi.polarity_scores(text)

    elif language == 'ne':
        sid_Nepali = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Nepali.polarity_scores(text)

    elif language == 'nl':
        sid_Dutch = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Dutch.polarity_scores(text)

    elif language == 'no':
        sid_Norwegian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Norwegian.polarity_scores(text)

    elif language == 'pa':
        sid_Punjabi = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Punjabi.polarity_scores(text)

    elif language == 'pl':
        sid_Polish = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Polish.polarity_scores(text)

    elif language == 'pt':
        sid_Portuguese = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Portuguese.polarity_scores(text)

    elif language == 'ro':
        sid_Romanian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Romanian.polarity_scores(text)

    elif language == 'ru':
        sid_Russian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Russian.polarity_scores(text)

    elif language == 'sk':
        sid_Slovak = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Slovak.polarity_scores(text)

    elif language == 'sl':
        sid_Slovenian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Slovenian.polarity_scores(text)

    elif language == 'so':
        sid_Somali = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Somali.polarity_scores(text)

    elif language == 'sq':
        sid_Albanian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Albanian.polarity_scores(text)

    elif language == 'sv':
        sid_Swedish = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Swedish.polarity_scores(text)

    elif language == 'sw':
        sid_Swahili = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Swahili.polarity_scores(text)

    elif language == 'ta':
        sid_Tamil = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Tamil.polarity_scores(text)

    elif language == 'te':
        sid_Telugu = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Telugu.polarity_scores(text)

    elif language == 'th':
        sid_Thai = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Thai.polarity_scores(text)

    elif language == 'tl':
        sid_Tagalog = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Tagalog.polarity_scores(text)

    elif language == 'tr':
        sid_Turkish = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Turkish.polarity_scores(text)

    elif language == 'uk':
        sid_Ukrainian = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Ukrainian.polarity_scores(text)

    elif language == 'ur':
        sid_Urdu = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Urdu.polarity_scores(text)

    elif language == 'vi':
        sid_Vietnamese = SentimentIntensityAnalyzer()
        sentiment_scores = sid_Vietnamese.polarity_scores(text)

    elif language == 'zh-cn':
        sid_ChineseSimplified = SentimentIntensityAnalyzer()
        sentiment_scores = sid_ChineseSimplified.polarity_scores(text)

    elif language == 'zh-tw':
        sid_ChineseTraditional = SentimentIntensityAnalyzer()
        sentiment_scores = sid_ChineseTraditional.polarity_scores(text)




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
