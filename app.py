# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:50:36 2026

@author: user
"""

import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- SETTING UP THE PAGE ---
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")
st.markdown("Enter a movie you like, and we'll suggest similar ones!")

# --- STEP 1: DATA LOADING & PREPROCESSING ---
@st.cache_data # This prevents reloading data every time you click a button
def load_data():
    movies_data = pd.read_csv('movies.csv') # Ensure path is correct
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
    
    # Replacing null values
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')
        
    # Combining features
    combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + \
                        movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + \
                        movies_data['director']
    
    # Vectorizing
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)
    
    # Calculating Similarity
    similarity = cosine_similarity(feature_vectors)
    
    return movies_data, similarity

movies_data, similarity = load_data()
list_of_all_titles = movies_data['title'].tolist()

# --- STEP 2: USER INTERFACE ---
movie_name = st.selectbox("Select or type a movie name:", list_of_all_titles)

if st.button('Recommend'):
    # Finding the close match
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    if find_close_match:
        close_match = find_close_match[0]
        
        # Getting index of the movie
        index_of_the_movie = movies_data[movies_data.title == close_match].index[0]
        
        # Getting similarity scores
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        
        # Sorting movies
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        
        # Displaying Results
        st.subheader(f"Movies suggested for you based on '{close_match}':")
        
        cols = st.columns(2) # Split into two columns for better look
        for i, movie in enumerate(sorted_similar_movies[1:21]): # Show top 20
            index = movie[0]
            title_from_index = movies_data.iloc[index]['title']
            
            if i < 10:
                cols[0].write(f"{i+1}. {title_from_index}")
            else:
                cols[1].write(f"{i+1}. {title_from_index}")
    else:
        st.error("Movie not found. Please try another name.")