import gmpy2
import numpy
import pandas as pd
from gmpy2 import mpfr


#set precision: 100
gmpy2.get_context().precision=100
data = pd.read_csv("english_word_data/unigram_freq.csv")
data["count"] = data["count"].astype(str)
data["count"] = data["count"].apply(lambda x: mpfr(x))
total_vals = sum(data["count"])
data["count"] = data["count"].apply(lambda x: mpfr(x) / total_vals)

# gets words index for a word

def word_to_beat_index(word, array):
    return numpy.where(array["word"].values == word)[0][0]

# returns data below the word's index

def subset_data(data, word, include_word = True):
    index = word_to_beat_index(word, data)
    if include_word:
        return data[index:]
    else:
        if index + 1 == len(data):
            raise ValueError("No Words Left In Data")
        return data[index+1:]

# returns data below the index

def subset_data_index(data, index, include_word = True):
    if include_word:
        return data[index:]
    else:
        if index + 1 == len(data):
            raise ValueError("No Words Left In Data")
        return data[index+1:] 

# returns data with a count below the count

def subset_data_count(data, count, include_word = True):
    if include_word == True:
        return data[data["count"] <= count]
    else:
        return data[data["count"] < count]

    # for implementation
def get_words_by_freq(data, count, include_word = True):
    if include_word == True:
        return data[data["count"] <= count]["word"].values
    else:
        return data[data["count"] < count]["word"].values

def word_in_data(word):
    # make into class to reduce load time
    data = pd.read_csv("english_word_data/unigram_freq.csv")
    return word in data["word"].values