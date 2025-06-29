import pandas as pd

def analyze_products(input_file='data/product_reviews.xlsx', output_file='data/cleaned_reviews.csv'):
    df = pd.read_excel(input_file, engine='openpyxl')

    print("[DEBUG] Columns found:", df.columns.tolist())

    # Drop rows missing key info
    df.dropna(subset=['product', 'rating', 'categories', 'reviews'], inplace=True)

    # Clean review text
    df['review_text'] = df['reviews'].astype(str).str.strip().str.lower()

    # Create sentiment label
    df['sentiment'] = df['rating'].apply(lambda x: 'positive' if x >= 4 else 'negative')

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"[✅] Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_reviews()
