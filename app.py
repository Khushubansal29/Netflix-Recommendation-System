import streamlit as st
import pandas as pd
from src.recommendation_engine import (
    recommend,
    available_movies
)

st.markdown("""
<style>
.stApp {
    background-color: #141414;
}

h1 {
    color: #E50914;
    text-align: center;
}

.stButton > button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #B20710;
}

div[data-testid="stMetric"] {
    background-color: #222222;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.markdown(
    "<h1>🎬 Netflix Recommendation System</h1>",
    unsafe_allow_html=True
)

st.write(
    "Movie Recommendation System using Collaborative Filtering"
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Movies Available", len(available_movies))

with col2:
    st.metric("Recommendations", 5)

movie = st.selectbox(
    "Choose a Movie",
    available_movies
)

if st.button("Recommend"):

    with st.spinner("Finding similar movies..."):

        recommended_movies = recommend(movie)

    st.subheader("Recommended Movies")

    if len(recommended_movies) == 0:
        st.warning("No recommendations found.")
    else:
        for i, rec in enumerate(recommended_movies, start=1):

            st.markdown(
                f"""
                <div style="
                    background-color:#222222;
                    padding:15px;
                    border-radius:10px;
                    margin-bottom:10px;
                    border-left:5px solid #E50914;
                ">
                    <h4>{i}. {rec}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )