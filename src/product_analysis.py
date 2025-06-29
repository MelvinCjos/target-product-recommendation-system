import pandas as pd

def analyze_products(input_file='data/predicted_reviews.csv'):
    df = pd.read_csv(input_file)

    # Group by product and category
    summary = df.groupby(['product', 'categories']).agg({
        'predicted_sentiment': lambda x: (x == 'positive').sum(),
        'rating': ['mean', 'count']
    }).reset_index()

    # Rename columns
    summary.columns = ['product', 'category', 'positive_reviews', 'avg_rating', 'total_reviews']

    # Best-selling = most reviews and high rating
    best = summary.sort_values(['total_reviews', 'avg_rating'], ascending=False).head(10)
    best.to_csv('reports/best_selling_products.csv', index=False)

    # Least-selling = low positive sentiment and low rating
    least = summary.sort_values(['positive_reviews', 'avg_rating'], ascending=True).head(10)
    least.to_csv('reports/least_selling_products.csv', index=False)

    print("[✅] Product reports generated in /reports/")

if __name__ == "__main__":
    analyze_products()