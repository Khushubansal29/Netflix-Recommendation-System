import pandas as pd

df = pd.read_csv("data/sample_ratings.csv")

print("Dataset Loaded")
print(df.shape)

# Movie statistics
movie_stats = (
    df.groupby("MovieID")["Rating"]
    .agg(["count", "mean"])
    .reset_index()
)

movie_stats.columns = [
    "MovieID",
    "NumRatings",
    "AverageRating"
]

movie_stats = movie_stats.sort_values(
    by=["AverageRating", "NumRatings"],
    ascending=False
)

print("\nTop 10 Movies\n")
print(movie_stats.head(10))