from sent2vec.vectorizer import Vectorizer
from nltk.tokenize import sent_tokenize
from dataset import get_examples
from word_frequency import *
from pathlib import Path
from utils import *
import sys


#train sent2vec
# load sentence to vec mode from wiki_unigrams.bin

# Load sent2vec vectorizer
# using bert-base-uncased
# vectorizer.bert("bert-base-uncased")
vectorizer = Vectorizer()

# my own multi dimensional list iterator :)

def max_iterator(iterator_list, previous_index = []):
    if len(iterator_list) > 0: 
        for i in range(iterator_list[-1]):
            max_iterator(iterator_list[:-1], [i] + previous_index)
    elif len(iterator_list) == 0:
        do_thing(previous_index)
        print(previous_index)

def do_thing(previous_index, sub_list):
    sub_list.append()
            

# make this generalized
summed_percentile = 0.68
words_to_remove = list(subset_percentile(summed_percentile)["word"])
count_word_to_remove = len(words_to_remove)

print("length of words to remove", count_word_to_remove)
print("Word Vocab Space", word_space() - count_word_to_remove)


#sys.exit()

training_exaples = get_examples("train")



questions = [example["question"] for example in training_exaples]

for question in questions:
    
    sentences = tokenize_sentence(question)
    
    for sentence in sentences:
        
        # breaks apart sentence into words

        #toeknizes and prelimiary filtering
        words = filter_words(sentence) 

        # remove words that are not in the data
        valid_words = [x for x in words if word_in_data(x)]
        
        word_to_remove = [words for words in words if words in words_to_remove]


        replacement_tuples = {}
        for word in word_to_remove:
            # for word, appends valid synonym

            replacement_tuples[word] = synonym_better(word)[0]
            # dict structure is {word: [synonym, synonym, synonym]}

        # make possible matrix of all possible combinations of sentences

        # find where the word is in the sentence including uppercase and lowercase combinations
        words = replacement_tuples.keys()
        
        #index_start = [0 for x in range(len(words))]

        index_end = [len(replacement_tuples[x]) for x in words]

        def create_sentence(word, index):
            return sentence.replace(word, replacement_tuples[word][index])

        max_iterator(index_end, )



        





#correlation_matrix = vectorizer.run(list(sentence))
#print(correlation_matrix)

            



    

sys.exit()
"""

for sentence in data:
    correlation = sent_2_vec

    # find acceptable correlation
    words = sentence . split fancy


    if words in full_words:
        get union of two sets
        
        for word in union:
            
            definiions.append()
            definiions = []
            for definiion in words:

                sentce with modified defintion = xxxx

                deffinninition.append(sentence_2vec( sentce with modified defintion ))

            alered = [x - sentecne_2_vec for x in defintions]
            
            # use pythagorean theorem do find shortest distance
            # take squares and then sqrt the values to find closest to real
            take pythagorean theorem of all values by list comprehension
            
            store values then find min 

            min is real value 

            substitute real value in sentence

            continue




# first rounds

"""
            



