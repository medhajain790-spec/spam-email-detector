# 📧 Spam Email Detector

A machine learning project that classifies an email as **SPAM** or **NOT SPAM**.
It includes a trained model, a Flask API, and a simple web interface.

## How it works

```
Email text
   ↓
Cleaning (lowercase, numbers → "escapenumber", remove punctuation)
   ↓
TF-IDF Vectorizer (text → numbers)
   ↓
Multinomial Naive Bayes
   ↓
SPAM / NOT SPAM  (+ spam probability)
```

## Tech stack

- Python, pandas, scikit-learn (training in Google Colab)
- Flask + Flask-CORS (backend API)
- HTML, CSS, JavaScript (frontend)

## Dataset

[Spam Email Classification Dataset](https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset) from Kaggle
(TREC 2007 and Enron spam emails). After removing very short emails (under 5 words),
about 83,000 emails were used, with roughly 52% spam and 48% not spam.

The dataset is **not included** in this repository because of its size.
Download it from the link above if you want to retrain the model.

## Results

Evaluated on 20% unseen test data (16,631 emails):

| Metric | Value |
|---|---|
| Accuracy | 97.35% |
| Precision (spam) | 0.98 |
| Recall (spam) | 0.97 |
| F1-score (spam) | 0.97 |

Confusion matrix:

| | Predicted NOT SPAM | Predicted SPAM |
|---|---|---|
| **Actual NOT SPAM** | 7731 | 162 |
| **Actual SPAM** | 278 | 8460 |

## Project structure

```
spam-email-detector/
├── backend/
│   ├── app.py              # Flask API
│   └── predictor.py        # cleaning + prediction logic
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── model/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
├── training/
│   └── spam_email_detector.ipynb
├── requirements.txt
└── README.md
```

## How to run

1. Clone the repository and go into the folder:

```bash
git clone https://github.com/YOUR_USERNAME/spam-email-detector.git
cd spam-email-detector
```

2. Create a virtual environment and install the libraries:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Start the backend:

```bash
python backend/app.py
```

4. In a new terminal, open the frontend:

```bash
open frontend/index.html
```

Paste an email, click **Check Email**, and see the prediction.

## API

`POST /predict`

Request:

```json
{ "email": "Congratulations! You won a free iPhone." }
```

Response:

```json
{ "label": "SPAM", "spam_probability": 91.0 }
```

## Limitations

- The training data is already lowercase with punctuation removed, so new emails
  are cleaned in the same style before prediction.
- The model only knows words from its training vocabulary, so it works best on
  English emails similar to the Enron and TREC data. It has not seen Hinglish or
  other languages.
- The probability is the model's estimate, not a guarantee.# spam-email-detector
