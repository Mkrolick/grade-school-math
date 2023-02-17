from sent2vec.vectorizer import Vectorizer
from nltk.tokenize import sent_tokenize
from dataset import get_examples
from word_frequency import *
from scipy import spatial
from pathlib import Path
from utils import *
import numpy as np
import json
import sys


#train sent2vec
# load sentence to vec mode from wiki_unigrams.bin

# Load sent2vec vectorizer
# using bert-base-uncased


vectorizer = Vectorizer()
# make this generalized
summed_percentile = 0.68
words_to_remove = list(subset_percentile(summed_percentile)["word"])
count_word_to_remove = len(words_to_remove)

print("length of words to remove", count_word_to_remove)
print("Word Vocab Space", word_space() - count_word_to_remove)


#sys.exit()

training_exaples = get_examples("train")
training_exaples = training_exaples[1570:]


questions = [example["question"] for example in training_exaples]

# resume training on last 1390 data points

for example in training_exaples:
    skip = False    
    question = example["question"]
    sentences = tokenize_sentence(question)
    sentences = [x for x in sentences]
    new_sentences = ""
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

        #print(index_end)
        #print(replacement_tuples)
        #sys.exit()
        
        

        try:
            sentences_unflattened = max_iterator(index_end, previous_index=[], function_args = [sentence, replacement_tuples])
            
            # casting list to array and flattening it
            sentences_unflattened = np.asarray(sentences_unflattened)

            sentence_subsititions = sentences_unflattened.flatten()

            comparison_sentences = [sentence] + sentence_subsititions.tolist()

            #reset vector value for each sentence
            vectorizer.vectors = []

            vectorizer.run(comparison_sentences)

            # get sentence to vec for each sentence
            sentence_vectors = vectorizer.vectors

            # get sentence to vec for original sentence 
            original_sentence_vector = sentence_vectors[0]

            # get sentence to vec for all other sentences
            other_sentence_vectors = sentence_vectors[1:]

            # find the closest sentence to the original sentence's index

            vectors = [spatial.distance.cosine(original_sentence_vector, x) for x in other_sentence_vectors]

            closest_sentence_index = np.argmin(vectors)

            print(len(vectors))
        

            # get the closest sentence
            #print(closest_sentence_index)
            closest_sentence = comparison_sentences[1:][closest_sentence_index]

            new_sentences += closest_sentence


            #Make a confidence interval for the sentence to vec model, then label data with a confidence interval
            #help elimates outlier data points
        except:
            skip = True
            print("error")
            continue
        
    if skip:
        continue

    data_point = {"question": new_sentences[:-2], "answer": example["answer"]}
    # append data point to new data set

    with open("C:\\Users\\malco\\OneDrive\\Documents\\GitHub\\grade-school-math\\data_filtering\\new_data\\train.jsonl", "a") as f:
        f.write(json.dumps(data_point))
        f.write("\n")


