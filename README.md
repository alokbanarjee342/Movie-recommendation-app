<img width="1112" height="624" alt="Screenshot 2026-06-05 212102" src="https://github.com/user-attachments/assets/b54cb76d-400a-4421-b185-3e7dbec2784a" />



1.Overview:

An end-to-end Machine Learning project that suggests movies based on a user's favorite title. This system uses Content-Based Filtering to find similarities between movies using metadata like genres, keywords, cast, and directors.

2.Here i uesd :

  Language: Python 3.0
  Data Manipulation: Pandas, NumPy
  Machine Learning: Scikit-learn (TfidfVectorizer, cosine_similarity)
  Text Processing: difflib (for fuzzy string matching)
  Web Framework: Streamlit (for the interactive UI)
  Environment: Developed in Google Colab and deployed via Spyder
3.Features:

  -The system uses difflib to find the closest match to your input
  - Recommendations are based on a "Combined Feature" string consisting of:
  - 
      a.Genres
      b.Keywords
      c.Taglines
      d.Cast members
      e.Director names
   -Uses TF-IDF vectorization and pre-calculated similarity matrices for near-instant results.
   -Interactive web UI for clean, easy-to-use interface built with Streamlit.
  



