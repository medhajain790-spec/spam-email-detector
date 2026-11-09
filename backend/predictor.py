import re
from pathlib import Path

import joblib


# Project ka main folder dhundo
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "spam_model.pkl"
VECTORIZER_PATH = BASE_DIR / "model" / "tfidf_vectorizer.pkl"


# Saved model aur vectorizer ek baar load karo
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def clean_text(text):

    # 1. Lowercase
    text = text.lower()

    # 2. Har number ki jagah "escapenumber"
    text = re.sub(r"\d+", " escapenumber ", text)

    # 3. Letters aur spaces ke alawa sab kuch hatao
    text = re.sub(r"[^a-z\s]", " ", text)

    # 4. Extra spaces hatao
    text = re.sub(r"\s+", " ", text).strip()

    return text


def predict_email(email):

    cleaned = clean_text(email)

    numbers = vectorizer.transform([cleaned])

    prediction = model.predict(numbers)[0]
    probability = model.predict_proba(numbers)[0][1]

    return {
        "label": "SPAM" if prediction == 1 else "NOT SPAM",
        "spam_probability": round(float(probability) * 100, 1),
    }


# Sirf tab chalega jab file ko seedha run karo
if __name__ == "__main__":

    print(predict_email("Congratulations! You have won a free iPhone. Click here to claim your prize."))

    print(predict_email("Hi, please send me the project report before 5 PM."))