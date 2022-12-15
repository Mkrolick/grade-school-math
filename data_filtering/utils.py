from transformers import BertTokenizer
from dotenv import load_dotenv
from os import getenv
import requests
import ast
import re
import string  
from word_frequency import word_in_data, get_words_by_freq, subset_data, subset_data_index, subset_data_count, word_to_beat_index, subset_data_count, subset_data_index, subset_data, word_to_beat_index


load_dotenv()



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
        
        response_object = ast.literal_eval(response.text)
        
        #testing
        #print(response_object)

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


def filter_words(text):
    # use WordPiece tokenizer to split words. Simple easy and fast implementation
    # https://huggingface.co/transformers/model_doc/bert.html#transformers.BertTokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    # split text into words
    tokens = tokenizer.tokenize(text)

    # remove punctuation 
    words = [x for x in tokens if x not in string.punctuation]
    lower_words = [x.lower() for x in words]
    valid_words = [x for x in lower_words if word_in_data(x)]

    return valid_words




print(filter_words("I like cats. they aren't cool."))