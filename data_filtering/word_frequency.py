import gmpy2
import numpy
import pandas as pd
from gmpy2 import mpfr
import sys
import numpy as np
from utils import *


#set precision: 100
#gmpy2.get_context().precision=100
data = pd.read_csv("english_word_data/unigram_freq.csv").copy()



data["count"] = data["count"].astype(str)
data["count"] = data["count"].apply(lambda x: mpfr(x))
total_vals = sum(data["count"])
data["count"] = data["count"].apply(lambda x: mpfr(x) / total_vals)
data["cumulative_density"] = 0

word_space_val = len(data)

print("Loaded Word Frequency with a size of", len(data))


cumulative_density = []

for index, value in enumerate(data["count"]):
    if index == 0:
        cumulative_density += [0]
    else:
        cumulative_density += [cumulative_density[index-1] + value]


data["cumulative_density"] = cumulative_density




# gets words index for a word

def word_to_beat_index(word):
    return numpy.where(data["word"].values == word)[0][0]
    

# word to beat index with a false return
def word_index(word):
    try:
        return word_to_beat_index(word)
    except:
        return False


# testing words
def synonym_better(word):
    synonym_list = synonyms(word)
    if synonym_list == None:
        return ([], False)
    elif len(synonym_list) == 0:
        return ([], False)
    

    syn_index = [word_index(x) for x in synonym_list]

    cleaned_synonym_list = []
    for index, synonym in enumerate(syn_index):
        if synonym < word_to_beat_index(word) and synonym:
            # no need for indicies anymore
            cleaned_synonym_list.append(synonym_list[index])
        else:
            #return ("Failing", False)
            continue
    
    if len(cleaned_synonym_list) == 0:
        return ([], False)
    else:
        return (cleaned_synonym_list, True)
    







# returns data below the word's index

def subset_data(word, include_word = True):
    index = word_to_beat_index(word)
    if include_word:
        return data[index:]
    else:
        if index + 1 == len(data):
            raise ValueError("No Words Left In Data")
        return data[index+1:]

# returns data below the index

def subset_data_index(index, include_word = True):
    if include_word:
        return data[index:]
    else:
        if index + 1 == len(data):
            raise ValueError("No Words Left In Data")
        return data[index+1:] 

# returns data with a count below the count

def subset_data_count(count, include_word = True):
    if include_word == True:
        return data[data["count"] <= count]
    else:
        return data[data["count"] < count]

    # for implementation
def get_words_by_freq(count, include_word = True):
    if include_word == True:
        return data[data["count"] <= count]["word"].values
    else:
        return data[data["count"] < count]["word"].values


def word_in_data(word):
    # make into class to reduce load time
    data = pd.read_csv("english_word_data/unigram_freq.csv")
    return word in data["word"].values

def subset_percentile(percentile):
    return data[data["cumulative_density"] >= percentile]

def word_space():
    return word_space_val
