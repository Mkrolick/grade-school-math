from transformers import BertTokenizer
from dotenv import load_dotenv
from os import getenv
import requests
import ast
from re import split
import string  
import pysbd
import sent2vec


load_dotenv()



def replacement_index(sentence, word, replacement):
    lower_sentence = sentence.lower()
    lower_word = word.lower()
    index = lower_sentence.find(lower_word)
    if index == -1:
        raise ValueError("Word Not In Sentence")
    # start sentence[:index], end sentence[index + len(word):]
    return (index, index + len(word))

# ast.literal_eval alternative
def eval_code(code):
    parsed = ast.parse(code, mode='eval')
    fixed = ast.fix_missing_locations(parsed)
    compiled = compile(fixed, '<string>', mode='eval')
    return eval(compiled)






# add threading to improve speed
def define(word, remove_gaps = False):

    try:
        RapidApiKey = getenv("RAPID_API_KEY")

        url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"

        headers = {
            "X-RapidAPI-Key": RapidApiKey,
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        
        # depricated eval function
        # response_object = ast.literal_eval(response.text)

        # eval object
        response_object = eval_code(response.text)
        
       

        # check if works
        if "success" in response_object.keys():
            raise "Error Word Does Not Exist"
        else:
            
            #grab definitions
            definitions = [x["definition"] for x in response_object["definitions"]]

            if remove_gaps:
                new_definition = []
                
                # spilts definitons by ; and removes the first part
                for definition in definitions:
                    definition = re.split(';.', definition)[0]
                    new_definition.append(definition)
                
                return new_definition

            return definitions
    except:
        raise "Error Word Does Not Exist"

# add threading to improve speed
def synonyms(word):
    try:
        RapidApiKey = getenv("RAPID_API_KEY")

        url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"

        headers = {
            "X-RapidAPI-Key": RapidApiKey,
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)


        # depricated eval function
        # response_object = ast.literal_eval(response.text)

        # eval object
        response_object = eval_code(response.text)

        

        # check if works
        if "success" in response_object.keys():
            raise "Error Word Does Not Exist"
        else:
            return response_object["synonyms"]
    except:
        print("Failed To Get Synonyms")
            

def filter_words(text):
    # use WordPiece tokenizer to split words. Simple easy and fast implementation
    # https://huggingface.co/transformers/model_doc/bert.html#transformers.BertTokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # split text into words
    tokens = tokenizer.tokenize(text)

    # remove punctuation 
    words = [x for x in tokens if x not in string.punctuation]
    lower_words = [x.lower() for x in words]

    return lower_words


def convert_to_words(document):
    chunks = document.split(" ")
    words = [x for x in chunks if x not in string.punctuation]
    lower_words = [x.lower() for x in words]
    # clean punctuation on ends and start of words
    clean_words = [x.strip(string.punctuation) for x in lower_words]
    return clean_words


# breaks data into sentences for sentence to vec processing
def tokenize_sentence(data):
    seg = pysbd.Segmenter(language="en", clean=False)
    return seg.segment(data)

"""
Depricated Code
def words_in_sentence(sentence):
    # split sentence into words
    words = convert_to_words(sentence)
    # remove words that are not in the data
    valid_words = [x for x in words if word_in_data(x)]
    return valid_words
"""

def split_sentece_by_word(sentence, word):
    sentence_chunks = sentence.split(word)
    return sentence_chunks

def max_iterator(iterator_list, previous_index = [], function = lambda x: print(x)):
    if len(iterator_list) > 0: 
        for i in range(iterator_list[-1]):
            max_iterator(iterator_list[:-1], [i] + previous_index, function)
    elif len(iterator_list) == 0:
        function(previous_index)
        #print(previous_index)


    
    


if __name__ == "__main__":
    load_dotenv()
    # use requests to fetch data from https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt

    import requests
    import re

    url = "https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt"

    response = requests.request("GET", url)

    data = response.text
    print(data)

    print(convert_to_words(data))



