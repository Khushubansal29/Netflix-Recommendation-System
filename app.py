import streamlit as st
import pandas as pd
from src.recommendation_engine import recommend

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Netflix Recommendation System")

st.write(
    "Movie Recommendation System using Collaborative Filtering"
)

movies = pd.read_csv(
    "data/raw/movie_titles.csv",
    header=None,
    names=["MovieID", "Year", "Title"],
    encoding="latin1",
    on_bad_lines="skip"
)

movie_list = sorted(
    movies["Title"]
    .dropna()
    .unique()
)

movie = st.selectbox(
    "Choose a Movie",
    movie_list
)

if st.button("Recommend"):

    recommended_movies = recommend(movie)

    st.subheader("Recommended Movies")

    if len(recommended_movies) == 0:
        st.warning("No recommendations found.")
    else:
        for i, rec in enumerate(recommended_movies, start=1):
            st.write(f"{i}. {rec}")