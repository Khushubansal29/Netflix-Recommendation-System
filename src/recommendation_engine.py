import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# Load ratings
df = pd.read_csv("data/sample_ratings.csv")

# User-Movie Matrix
user_movie_matrix = df.pivot_table(
    index="UserID",
    columns="MovieID",
    values="Rating"
)

# Fill missing values
user_movie_filled = user_movie_matrix.fillna(0)

# Similarity Matrix
similarity_matrix = cosine_similarity(
    user_movie_filled.T
)

similarity_df = pd.DataFrame(
    similarity_matrix,
    index=user_movie_filled.columns,
    columns=user_movie_filled.columns
)

# Movie titles
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

title_to_id = dict(
    zip(movies["Title"], movies["MovieID"])
)


def recommend(movie_title, top_n=5):

    movie_id = title_to_id.get(movie_title)

    if movie_id not in similarity_df.columns:
        return []

    similar_movies = (
        similarity_df[movie_id]
        .sort_values(ascending=False)
        .iloc[1:top_n+1]
    )

    recommendations = []

    for movie_id in similar_movies.index:
        recommendations.append(
            movie_dict.get(movie_id)
        )

    return recommendations

available_movies = sorted(
    [
        movie_dict[movie_id]
        for movie_id in similarity_df.columns
        if movie_id in movie_dict
    ]
)