import pandas as pd

movies = pd.read_csv(
    "data/raw/movie_titles.csv",
    header=None,
    names=["MovieID", "Year", "Title"],
    encoding="latin1",
    on_bad_lines="skip"
)

movie_dict = dict(
    zip(movies["MovieID"], movies["Title"])
)

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

# Recommendation Function

def recommend_movies(movie_id, top_n=5):

    print(f"\nMovies similar to Movie {movie_id}:")

    similar_movies = similarity_df[movie_id].sort_values(
        ascending=False
    )

    recommendations = similar_movies.iloc[1:top_n+1]

    for movie, score in recommendations.items():
        movie_name = movie_dict.get(movie, "Unknown Movie")

    print(
        f"MovieID: {movie} | "
        f"Title: {movie_name} | "
        f"Similarity: {score:.4f}"
    )

    return recommendations

print("\nTesting recommendation function...")
recommend_movies(1)