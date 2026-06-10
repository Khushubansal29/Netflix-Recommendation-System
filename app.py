import streamlit as st
from src.recommendation_engine import (
    recommend,
    available_movies
)

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(
        circle at top,
        rgba(229,9,20,0.18),
        #141414 35%
    );
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.stApp {
    background-color: #141414;
}

.stButton > button {
    background-color: #E50914;
    color: white;
    font-size: 20px;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    height: 60px;
    width: 100%;
}

.stButton > button:hover {
    background-color: #B20710;
}

.movie-card {
    background-color: #1F1F1F;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    border-left: 6px solid #E50914;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background: linear-gradient(90deg,#111111,#1d1d1d);
padding:40px;
border-radius:20px;
text-align:center;
margin-bottom:25px;
">

<h1 style="
color:#E50914;
font-size:60px;
margin-bottom:10px;
">
🎬 Netflix Recommendation System
</h1>

<p style="
color:#CCCCCC;
font-size:22px;
">
AI-Powered Movie Discovery using Collaborative Filtering
</p>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Movies Available",
        len(available_movies)
    )

with col2:
    st.metric(
        "Recommendations",
        5
    )

st.write("")

st.subheader("🔍 Search Movie")

movie = st.selectbox(
    "",
    available_movies
)

st.write("")


if st.button("🎯 Recommend Movies"):

    with st.spinner("Finding similar movies..."):

        recommended_movies = recommend(movie)

    st.markdown("## 🍿 Recommended Movies")

    if len(recommended_movies) == 0:

        st.warning("No recommendations found.")

    else:

        for i, rec in enumerate(recommended_movies, start=1):

            st.success(f"#{i} {rec}")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
             <div style="
                background:#1F1F1F;
                padding:18px;
                border-radius:12px;
                text-align:center;
                color:#BBBBBB;
                font-size:18px;
                border:1px solid #333333;
            ">
                🎯 Recommendations generated because you selected
            <span style="color:#E50914;font-weight:bold;">
                {movie}
            </span>
            </div>
             """,
            unsafe_allow_html=True
        )

st.write("")
st.write("")
st.markdown("---")

st.caption(
    "Built using Python • Pandas • Scikit-Learn • Streamlit"
)