import pandas as pd

df = pd.read_csv("data/sample_ratings.csv")

print("Dataset Loaded")
print(df.shape)

# User-Movie Matrix
user_movie_matrix = df.pivot_table(
    index="UserID",
    columns="MovieID",
    values="Rating"
)

print("\nUser-Movie Matrix Shape:")
print(user_movie_matrix.shape)

print("\nFirst 5 Rows:")
print(user_movie_matrix.head())
