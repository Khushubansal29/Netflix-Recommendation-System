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


from sklearn.metrics.pairwise import cosine_similarity

print("\nCalculating movie similarity...")

movie_similarity = cosine_similarity(
    user_movie_matrix.fillna(0).T
)

similarity_df = pd.DataFrame(
    movie_similarity,
    index=user_movie_matrix.columns,
    columns=user_movie_matrix.columns
)

print("\nSimilarity Matrix Shape:")
print(similarity_df.shape)

print("\nFirst 5x5 Similarity Matrix:")
print(similarity_df.iloc[:5, :5])