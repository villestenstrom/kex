import nltk
from nltk.corpus import brown, names, inaugural, reuters
from nltk import bigrams
from collections import Counter
import re
import pandas as pd
import numpy as np

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

    for bigram, freq in most_common:
        print(f"{bigram[0]}{bigram[1]}:{freq}")

def relative_frequency(corpus, corpus_name):
    nltk.download(corpus_name)
    nltk.download('punkt')

    words = corpus.words()
    text = " ".join(words).lower()
    cleaned_text = re.sub(r'[^a-z,.]', '', text)

    total_chars = len(cleaned_text)
    char_freq = Counter(cleaned_text)
    
    # Sort char_freq by the frequency of the characters
    char_freq = {k: v for k, v in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)}

    for char, freq in char_freq.items():
        print(f"{char}: {freq / total_chars:.4f}")



def most_common_bigrams_relative(corpus, corpus_name):
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
    print(cleaned_text)

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


# Example usage
corpus = reuters

# Get the name of the corpus
corpus_name = corpus.__name__
print(f"Corpus: {corpus_name}")

print("Most Common Bigrams:")
most_common_bigrams(corpus, corpus_name, 1000)
print("\nRelative Frequency of Letters, Comma, and Period:")
relative_frequency(corpus, corpus_name)
print("\nMost Common Bigrams Relative Frequency:")
df = most_common_bigrams_relative(corpus, corpus_name)
print(df)   # Returns a DataFrame
print("\nSum of Values in DataFrame:")
print(sum_values_in_df(df))
print("\nFrequency of Bigrams:")
print('th: ', get_frequency_of_bigram(df, 't', 'h'))
print('er: ', get_frequency_of_bigram(df, 'e', 'r'))
print('an: ', get_frequency_of_bigram(df, 'a', 'n'))
print('in: ', get_frequency_of_bigram(df, 'i', 'n'))
print('re: ', get_frequency_of_bigram(df, 'r', 'e'))
print('on: ', get_frequency_of_bigram(df, 'o', 'n'))
print('..: ', get_frequency_of_bigram(df, '.', '.'))
print(',,: ', get_frequency_of_bigram(df, ',', ','))
print('a,: ', get_frequency_of_bigram(df, 'a', ','))
print(',a: ', get_frequency_of_bigram(df, '.', 'a'))
print('s,: ', get_frequency_of_bigram(df, 's', ','))
print(',s: ', get_frequency_of_bigram(df, ',', 's'))
