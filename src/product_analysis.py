# src/product_analysis.py

import pandas as pd

def analyze_products(input_file='data/predicted_reviews.csv'):
    df = pd.read_csv(input_file)

    # Group by product and category
    summary = df.groupby(['product name', 'category path']).agg({
        'predicted_sentiment': lambda x: (x == 'positive').sum(),
        'rating': ['mean', 'count']
    }).reset_index()

    summary.columns = ['product_name', 'category', 'positive_reviews', 'avg_rating', 'total_reviews']

    # Best-selling = most reviews with high average rating
    best = summary.sort_values(['total_reviews', 'avg_rating'], ascending=False).head(10)
    best.to_csv('reports/best_selling_products.csv', index=False)

    # Least-selling = few reviews with mostly negative sentiment
    least = summary.sort_values(['positive_reviews', 'avg_rating'], ascending=True).head(10)
    least.to_csv('reports/least_selling_products.csv', index=False)

    print("[✅] Product analysis reports saved in 'reports/' folder.")

if __name__ == "__main__":
    analyze_products()
