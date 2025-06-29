# src/generate_reports.py

from preprocess import clean_reviews
from sentiment_model import train_and_predict
from product_analysis import analyze_products

def run_pipeline():
    print("📥 Step 1: Cleaning the data...")
    clean_reviews()

    print("\n🤖 Step 2: Training sentiment model and predicting...")
    train_and_predict()

    print("\n📊 Step 3: Analyzing products...")
    analyze_products()

    print("\n✅ All steps complete! Check the 'reports/' folder and your GitHub README.")

if __name__ == "__main__":
    run_pipeline()
