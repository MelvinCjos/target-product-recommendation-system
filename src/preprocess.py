import pandas as pd

def clean_reviews(input_file='data/product_reviews.xlsx', output_file='data/cleaned_reviews.csv'):
    # Load the Excel sheet
    df = pd.read_excel(input_file, engine='openpyxl')

    # Debug: Print column names
    print("[DEBUG] Columns found:", df.columns.tolist())

    # Ensure columns match your actual file
    df.dropna(subset=['product', 'rating', 'categories', 'reviews'], inplace=True)

    # Clean the review text
    df['review_text'] = df['reviews'].astype(str).str.strip().str.lower()

    # Convert numeric ratings to sentiment
    df['sentiment'] = df['rating'].apply(lambda x: 'positive' if x >= 4 else 'negative')

    # Save cleaned data to CSV
    df.to_csv(output_file, index=False)
    print(f"[✅] Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_reviews()
