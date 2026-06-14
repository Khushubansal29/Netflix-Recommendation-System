# 🎬 Netflix Recommendation System

A Netflix inspired Movie Recommendation System built using **Collaborative Filtering** and **Cosine Similarity**. The application analyzes user movie rating patterns and recommends movies that are most similar to the movie selected by the user.

The project demonstrates the complete Machine Learning workflow including data preprocessing, similarity computation, recommendation generation, interactive web application development, and cloud deployment.

---

## Live Demo

🔗 **Streamlit App**
https://netflix-recommendation-system01.streamlit.app/

🔗 **GitHub Repository**
https://github.com/Khushubansal29/Netflix-Recommendation-System

---

## Project Preview

###Home Page

![Home Page](presentation/home_page.png)

### Recommendation Results

![Recommendation Results](presentation/recommendations.png)

---

## Project Overview

Recommendation systems are among the most widely used applications of Machine Learning and power platforms such as Netflix, Amazon, Spotify, and YouTube.

This project implements a **Collaborative Filtering Recommendation Engine** that suggests movies based on user rating behavior.

Instead of analyzing movie genres or descriptions, the system learns patterns from user interactions and recommends movies that are frequently liked by users with similar preferences.

---

## Problem Statement

Given historical movie ratings from users, recommend movies that are most similar to a selected movie.

The recommendation engine should:

* Analyze user movie interactions
* Compute movie similarity scores
* Generate relevant recommendations
* Deliver recommendations instantly
* Provide a simple and interactive interface

---

## Tech Stack

| Category               | Technologies              |
| ---------------------- | ------------------------- |
| Programming Language   | Python                    |
| Machine Learning       | Scikit-Learn              |
| Data Processing        | Pandas, NumPy             |
| Similarity Computation | Cosine Similarity         |
| Web Framework          | Streamlit                 |
| Version Control        | Git                       |
| Repository Hosting     | GitHub                    |
| Deployment             | Streamlit Community Cloud |

---

## Machine Learning Approach

### Collaborative Filtering

Collaborative Filtering recommends movies by learning patterns from user rating behavior.

The system assumes that users who liked similar movies in the past are likely to prefer similar movies in the future.

### Cosine Similarity

Movie similarity is computed using Cosine Similarity.

Movies with higher similarity scores are considered more relevant and are recommended to the user.

---

## System Workflow

```text
Movie Ratings Dataset
          │
          ▼
Data Cleaning & Preprocessing
          │
          ▼
User-Movie Pivot Matrix
          │
          ▼
Cosine Similarity Matrix
          │
          ▼
Recommendation Engine
          │
          ▼
Streamlit Web Application
          │
          ▼
Movie Recommendations
```

---

## Features

| Feature                    | Description                                          |
| -------------------------- | ---------------------------------------------------- |
| Collaborative Filtering    | Generates recommendations using user rating behavior |
| Cosine Similarity          | Calculates similarity between movies                 |
| Interactive UI             | Easy movie selection through Streamlit               |
| Real Time Recommendations  | Instant recommendation generation                    |
| Netflix Inspired Interface | Clean and user friendly design                       |
| Cloud Deployment           | Accessible from anywhere                             |
| GitHub Integration         | Version-controlled development                       |

---

## Dataset Information

The project uses a sampled subset of the **Netflix Prize Dataset**.

### Dataset Components

| Component         | Description                                 |
| ----------------- | ------------------------------------------- |
| Movie IDs         | Unique movie identifiers                    |
| Movie Titles      | Movie names                                 |
| User Ratings      | Ratings provided by users                   |
| User Movie Matrix | Interaction matrix used for recommendations |

A representative subset was used to enable lightweight deployment and faster experimentation.

The recommendation engine can be scaled to larger datasets with minimal code modifications.

---

## Recommendation Pipeline

### Step 1: Data Preprocessing

* Load ratings dataset
* Remove inconsistencies
* Handle missing values

### Step 2: Matrix Creation

* Create user movie pivot table
* Convert ratings into matrix form

### Step 3: Similarity Computation

* Compute Cosine Similarity matrix
* Store similarity scores

### Step 4: Recommendation Generation

* Find nearest similar movies
* Rank recommendations
* Return top recommendations

### Step 5: Web Application

* User selects a movie
* System generates recommendations
* Results displayed instantly

---

## Key Learnings

Through this project, I gained hands-on experience in:

* Recommendation Systems
* Collaborative Filtering
* Cosine Similarity
* Data Preprocessing
* Matrix Transformations
* Similarity-Based Learning
* Streamlit Development
* Git & GitHub Workflow
* Cloud Deployment
* End-to-End Machine Learning Projects

---

## Future Improvements

* Hybrid Recommendation Systems
* Content Based Filtering
* User Personalization
* Deep Learning Based Recommenders
* Larger Movie Dataset Integration
* Recommendation Explanations

---

## Author

**Khushboo**
B.Tech Chemical Engineering
Indian Institute of Technology Roorkee

GitHub:
https://github.com/Khushubansal29
