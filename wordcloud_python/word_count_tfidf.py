# keyword_extraction_tfidf.py

import os
import glob
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

# Directory containing the text files
script_directory = os.getcwd()
text_files_directory = os.path.join(script_directory, 'text')

# Get a list of all text files in the directory
text_files = glob.glob(os.path.join(text_files_directory, '*.txt'))
if not text_files:
    print("No text files found in the 'transcripts' directory.")
    exit()

# Load stopwords
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
stop_words = set(stopwords.words('english'))

# Additional stopwords specific to your data (optional)
additional_stopwords = {'people', 'going', 'said', 'country', 'know', 'like', 'want', 'great', 'one', 'get',
                        'think', 'say', 'got', 'right', 'would', 'never', 'thank', 'good', 'much', 'go', 'lot',
                        'years', 'back', 'even', 'make', 'ever', 'take', 'way', 'president', 'thing', 'us', 'look',
                        'time', 'really', 'world', 'many', 'let', 'see', 'big', "paid", "ready", "social", "hes", "dead", "court", "plants", "easy", 
                        "debate", "records", "comes", "auto", "georgia", "november", "tonight", 
                        "senator", "rid", "water", "workers", "imagine", "worked", "answer", 
                        "democracy", "cuts", "harris", "treated", "teamster", "stopped", "threat", 
                        "school", "john", "judge", "drill", "brain", "show", "room", "charts", 
                        "vicious", "bill", "hit", "mike"}
stop_words = stop_words.union(additional_stopwords)

# Read and preprocess documents
documents = []
print("Reading and preprocessing texts...")
for file_path in text_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        # Remove non-alphabetic characters and convert to lowercase
        text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
        text = text.lower()
        # Remove extra whitespace
        text = text.strip()
        # Tokenize
        tokens = nltk.word_tokenize(text)
        # Remove stopwords
        filtered_tokens = [token for token in tokens if token not in stop_words]
        # Rejoin tokens into string
        text = ' '.join(filtered_tokens)
        documents.append(text)
print("Preprocessing completed.")

# Initialize vectorizer
vectorizer = TfidfVectorizer(max_df=0.7, min_df=5)

# Fit and transform
print("Calculating TF-IDF scores...")
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names
feature_names = vectorizer.get_feature_names_out()

# Sum TF-IDF scores for each term
import numpy as np
tfidf_scores = np.sum(tfidf_matrix.toarray(), axis=0)

# Create a dictionary of terms and scores
tfidf_scores_dict = dict(zip(feature_names, tfidf_scores))

# Sort the terms by score
sorted_tfidf = sorted(tfidf_scores_dict.items(), key=lambda x: x[1], reverse=True)

# Save Keywords to CSV
# Save Keywords to CSV
with open('keywords_tfidf_2.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Keyword', 'TF-IDF Score'])
    for keyword, score in sorted_tfidf[:60]:  # Top 60 keywords
        writer.writerow([keyword, score])
print("\nTop 60 keywords have been saved to 'keywords_tfidf_2.csv'.")
