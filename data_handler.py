import nltk
from nltk.corpus import brown, names, inaugural, reuters
from nltk import bigrams
from collections import Counter
import re
import pandas as pd
import numpy as np
import csv

def most_common_bigrams(corpus, corpus_name, n):
    nltk.download(corpus_name)
    nltk.download('punkt')
    
    words = corpus.words()
    text = " ".join(words).lower()
    cleaned_text = re.sub(r'[^a-z,.]', '', text)

    # Remove instances where a comma or period comes before a letter
    cleaned_text = re.sub(r'[,.][a-z]', '', cleaned_text)
    
    # Remove instances where a comma and period are next to each other, or periods are next to each other, or commas are next to each other
    cleaned_text = re.sub(r'[,.]{2,}', '', cleaned_text)

    bg = bigrams(cleaned_text)
    bg_freq = Counter(bg)

    # Filter out bigrams that don't match our criteria
    filtered_bigrams = {k: v for k, v in bg_freq.items() if not(k[0] in [',', '.'] and k[1].isalpha())}
    most_common = Counter(filtered_bigrams).most_common(n)

    

def relative_letter_frequency(corpus, corpus_name):
    nltk.download(corpus_name)
    nltk.download('punkt')

    words = corpus.words()
    text = " ".join(words).lower()
    cleaned_text = re.sub(r'[^a-z,.]', '', text)

    total_chars = len(cleaned_text)
    char_freq = Counter(cleaned_text)
    
    # Sort char_freq by the frequency of the characters
    char_freq = {k: v for k, v in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)}
    
    relative_freq = {}
    for char, freq in char_freq.items():
        relative_freq[char] = freq / total_chars
    
    return relative_freq



def relative_bigram_frequency2(corpus, corpus_name):
    nltk.download(corpus_name)
    nltk.download('punkt')
    
    # Prepare the text
    words = corpus.words()
    text = " ".join(words).lower()
    
    # Remove non-alphabetic characters (except for commas, periods, and spaces)
    cleaned_text = re.sub(r'[^a-z,.\' ]', '', text)
    
    # Remove spaces before commas and periods
    cleaned_text = re.sub(r' [,.]', '', cleaned_text)
    
    # Remove spaces before and after apostrophes
    cleaned_text = re.sub(r' \' ', '\'', cleaned_text)
    
    # Remove instances where a comma or period comes before a comma or period
    cleaned_text = re.sub(r'[,.]{2,}', '', cleaned_text)

    # Generate bigrams
    bg = bigrams(cleaned_text)
    bg_freq = Counter(bg)
    bg_freq = {k: v for k, v in bg_freq.items() if not(' ' in k)}

    # Calculate total number of bigrams for normalization
    total_bigrams = sum(bg_freq.values())

    # Initialize an empty DataFrame with rows and columns as letters and punctuation
    chars = [chr(c) for c in range(ord('a'), ord('z')+1)] + [',', '.', '\'']
    df = pd.DataFrame(np.zeros((len(chars), len(chars))), index=chars, columns=chars)

    # Populate the DataFrame with relative frequencies
    for (first, second), count in bg_freq.items():
        if first in df.columns and second in df.index:
            df.at[second, first] = count / total_bigrams

    return df

def sum_values_in_df(df):
    return df.values.sum()

def get_frequency_of_bigram(df, first, second):
    return df.at[second, first]

#df = relative_bigram_frequency2(brown, 'brown')
#print(get_frequency_of_bigram(df, 't', 'h'))
#print(get_frequency_of_bigram(df, 'l', 't'))

def relative_bigram_frequency(corpus, corpus_name):
    nltk.download(corpus_name)
    nltk.download('punkt')
    
    # Prepare the text
    words = corpus.words()
    text = " ".join(words).lower()
    
    # Remove non-alphabetic characters (except for commas, periods, and spaces)
    cleaned_text = re.sub(r'[^a-z,.\' ]', '', text)
    
    # Remove spaces before commas and periods
    cleaned_text = re.sub(r' [,.]', '', cleaned_text)
    
    # Remove spaces before and after apostrophes
    cleaned_text = re.sub(r' \' ', '\'', cleaned_text)
    
    # Remove instances where a comma or period comes before a comma or period
    cleaned_text = re.sub(r'[,.]{2,}', '', cleaned_text)

    # Generate character bigrams as tuples
    bigrams = [(cleaned_text[i], cleaned_text[i+1]) for i in range(len(cleaned_text)-1)]
    
    # Calculate frequencies of bigrams
    bigram_freq = Counter(bigrams)

    # Filter out bigrams that contain spaces
    bigram_freq = {k: v for k, v in bigram_freq.items() if ' ' not in k[0] and ' ' not in k[1]}

    # Calculate total number of bigrams for normalization
    total_bigrams = sum(bigram_freq.values())

    # Calculate relative frequencies
    bigram_rel_freq = {k: round(v / total_bigrams, 4) for k, v in bigram_freq.items()}
    
    # Sort bigram_rel_freq by frequency
    bigram_rel_freq = {k: v for k, v in sorted(bigram_rel_freq.items(), key=lambda item: item[1], reverse=True)}

    return bigram_rel_freq

#corpus = brown
#corpus_name = 'brown'
#bigram_freq = relative_letter_frequency(corpus, corpus_name)
#print(bigram_freq)
from tqdm import tqdm

def relative_letter_frequency_csv(filename):
    text = ""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in tqdm(reader, desc="Processing CSV file"):
            word, count = row
            text += word.lower() * int(count)

    cleaned_text = re.sub(r'[^a-z]', '', text)

    total_chars = len(cleaned_text)
    char_freq = Counter(cleaned_text)

    # Sort char_freq by the frequency of the characters
    char_freq = {k: v for k, v in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)}

    relative_freq = {}
    for char, freq in char_freq.items():
        relative_freq[char] = freq / total_chars

    return relative_freq

#csv_file_test = "test_data.csv"
#csv_file = "unigram_freq.csv"
#freq = relative_letter_frequency_csv(csv_file)
#print(freq)

