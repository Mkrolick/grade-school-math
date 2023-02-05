from sent2vec.vectorizer import Vectorizer
from nltk.tokenize import sent_tokenize
from dataset import get_examples
from pathlib import Path
from utils import *
import sys


#train sent2vec
# load sentence to vec mode from wiki_unigrams.bin

# Load sent2vec vectorizer
# using bert-base-uncased
# vectorizer.bert("bert-base-uncased")
vectorizer = Vectorizer()





training_exaples = get_examples("train")


print(training_exaples[0])
questions = [example["question"] for example in training_exaples]

for question in questions:
    pass
    #print(question)
    # for sentence in question:
    sentences = tokenize_sentence(question)
    #print(sentences)

    for sentence in sentences:

        correlation_matrix = vectorizer.run(list(sentence))
        print(correlation_matrix)




    

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
            



