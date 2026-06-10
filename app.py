import streamlit as st
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

movie = st.selectbox(
    "Choose a Movie",
    [
        "Dinosaur Planet",
        "Lilo and Stitch",
        "Screamers",
        "8 Man",
        "My Favorite Brunette",
        "Clifford: Clifford Saves the Day! / Clifford's Fluffiest Friend Cleo"
    ]
)

if st.button("Recommend"):

    recommended_movies = recommend(movie)

    st.subheader("Recommended Movies")

    if len(recommended_movies) == 0:
        st.warning("No recommendations found.")
    else:
        for i, rec in enumerate(recommended_movies, start=1):
            st.write(f"{i}. {rec}")