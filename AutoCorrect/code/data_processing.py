# import required packages
import re
from collections import Counter
import numpy as np
import pandas as pd



#read the shakespeare.txt file
with open ('shakespeare.txt') as file:
    data=file.read()  
words=re.findall(r'\w+', data.lower())   

# Note, 'words' is converted to a python `set`. This eliminates any duplicate entries.
vocab=set(words)
 
probs={}
def get_probs():   
    
    '''returns a dictionary where the keys are words,and the value for each word is its probability 
    in the corpus of words.'''
    
    word_count_dict = {}  
    word_count_dict=Counter(words)
    for k in word_count_dict.keys():
        probs[k]=word_count_dict[k]/len(words)
        
    return probs
    
