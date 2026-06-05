1.𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰 :

An end-to-end Machine Learning project that suggests movies based on a user's favorite title. This system uses Content-Based Filtering to find similarities between movies using metadata like genres, keywords, cast, and directors.

2.𝐇𝐞𝐫𝐞 𝐢 𝐮𝐞𝐬𝐝 :

  i. 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : Python 3.0
  
  ii. 𝐃𝐚𝐭𝐚 𝐌𝐚𝐧𝐢𝐩𝐮𝐥𝐚𝐭𝐢𝐨𝐧 : Pandas, NumPy
  
  iii. 𝐌𝐚𝐜𝐡𝐢𝐧𝐞 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 : Scikit-learn (TfidfVectorizer, cosine_similarity)
  
  iv. 𝐓𝐞𝐱𝐭 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 : difflib (for fuzzy string matching)
  
  v. 𝐖𝐞𝐛 𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤 : Streamlit (for the interactive UI)
  
  vi. 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭 : Developed in Google Colab and deployed via Spyder
  
3. 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 :

  -The system uses difflib to find the closest match to your input
  
  - Recommendations are based on a "Combined Feature" string consisting of:
    
      a. Genres
    
      b. Keywords
    
      c. Taglines
    
      d. Cast members
    
      e. Director names
    
   -Uses TF-IDF vectorization and pre-calculated similarity matrices for near-instant results.
   
   -Interactive web UI for clean, easy-to-use interface built with Streamlit.


<img width="1112" height="624" alt="Screenshot 2026-06-05 212102" src="https://github.com/user-attachments/assets/d1d3d84d-5c70-4bc4-8761-e90b99bc58c1" />


   
  



