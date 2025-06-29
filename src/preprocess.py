# src/preprocess.py

import pandas as pd

def clean_reviews(input_file='data/product_reviews.xlsx', output_file='data/cleaned_reviews.csv'):
    # Load Excel file
    df = pd.read_excel(input_file, engine='openpyxl')

    # Drop missing values
    df.dropna(subset=['review_text', 'rating', 'product name', 'category path'], inplace=True)

    # Clean text and map ratings to sentiment
    df['review_text'] = df['review_text'].str.strip().str.lower()
    df['sentiment'] = df['rating'].apply(lambda x: 'positive' if x >= 4 else 'negative')

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"[✅] Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_reviews()
