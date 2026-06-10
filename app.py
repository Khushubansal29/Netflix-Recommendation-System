import streamlit as st
import pandas as pd
from src.recommendation_engine import (
    recommend,
    available_movies
)

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Netflix Recommendation System")

st.write(
    "Movie Recommendation System using Collaborative Filtering"
)

movie = st.selectbox(
    "Choose a Movie",
    available_movies
)

if st.button("Recommend"):

    recommended_movies = recommend(movie)

    st.subheader("Recommended Movies")

    if len(recommended_movies) == 0:
        st.warning("No recommendations found.")
    else:
        for i, rec in enumerate(recommended_movies, start=1):
            st.write(f"{i}. {rec}")