# src/sentiment_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

def train_and_predict(input_file='data/cleaned_reviews.csv', output_file='data/predicted_reviews.csv'):
    df = pd.read_csv(input_file)

    # Features & Labels
    X = df['review_text']
    y = df['sentiment']

    # Vectorize text
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    X_vec = tfidf.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_vec)
    df['predicted_sentiment'] = predictions
    df.to_csv(output_file, index=False)

    print("[✅] Sentiment predictions saved to:", output_file)
    print("\n[📊] Model performance on test set:\n")
    print(classification_report(y_test, model.predict(X_test)))

    # Save model and vectorizer
    joblib.dump(model, 'src/model.joblib')
    joblib.dump(tfidf, 'src/vectorizer.joblib')

if __name__ == "__main__":
    train_and_predict()
