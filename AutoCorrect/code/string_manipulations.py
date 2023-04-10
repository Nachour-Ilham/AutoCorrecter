
from data_processing import *


# delete function
def delete_letter(word, verbose=False):
    '''
    Input:
        word: the string/word for which you will generate all possible words 
                in the vocabulary which have 1 missing character
    Output:
        delete_l: a list of all possible strings obtained by deleting 1 character from word
    '''
    
    delete_l = []
    split_l = []
    
    split_l= [(word[:i],word[i:]) for i in range(len(word))]
    delete_l=[ a+b[1:] for a,b in split_l]

    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l

# switch function
def switch_letter(word, verbose=False):
    '''
    Input:
        word: input string
     Output:
        switches: a list of all possible strings with one adjacent charater switched
    ''' 
    
    split_l = [(word[:i],word[i:]) for i in range(len(word))]
    switch_l = [a+b[1]+b[0]+b[2:] for a, b in split_l  if len(b)>1]

    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 

    return switch_l

# replace function
def replace_letter(word, verbose=False):
    '''
    Input:
        word: the input string/word 
    Output:
        replaces: a list of all possible strings where we replaced one letter from the original word. 
    ''' 
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []
    split_l = []
   
    split_l=[(word[:i],word[i:]) for i in range(len(word))]
    replace_l=[a + letter + (b[1:] if len(b)> 1 else '') for a,b in split_l for letter in letters]
    replace_set = set(replace_l)
    replace_set.remove(word)
    # turn the set back into a list and sort it, for easier viewing

    replace_l = sorted(list(replace_set))
    
    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")   
    
    return replace_l

# insert function
def insert_letter(word, verbose=False):
    '''
    Input:
        word: the input string/word 
    Output:
        inserts: a set of all possible strings with one new letter inserted at every offset
    ''' 
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []
    split_l = []
    
    split_l=[(word[:i],word[i:]) for i in range(len(word)+1)]
    insert_l= [ a + letter + b for a,b  in split_l for letter in letters ]

    if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    
    return insert_l

# edit one letters
def edit_one_letter(word, allow_switches = True):
    """
    Input:
        word: the string/word for which we will generate all possible wordsthat are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit. Please return a set. and not a list.
    """
    edit_one_set=set()
    
    if allow_switches:
        edit_one_set.update(switch_letter(word))    
    
    edit_one_set.update(delete_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))

    return edit_one_set

# edit two letters
def edit_two_letters(word, allow_switches = True):
    '''
    Input:
        word: the input string/word 
    Output:
        edit_two_set: a set of strings with all possible two edits
    '''
    
    edit_two_set = set()
    edit_one = edit_one_letter(word,allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w,allow_switches)
            edit_two_set.update(edit_two)
    
    return edit_two_set

# suggest spelling suggestions
# returns a list of zero to n possible suggestion tuples of the form (word, probability_of_word)
get_probs() 
def get_corrections(word, probs, vocab, n=2, verbose = False):
   
    '''
    Input: 
        word: a user entered string to check for suggestions
        probs: a dictionary that maps each word to its probability in the corpus
        vocab: a set containing all the vocabulary
        n: number of possible word corrections you want returned in the dictionary
    Output: 
        n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''
    
    suggestions = []
    n_best = []
    
    suggestions =(word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(vocab)
    n_best = [[i,probs[i]] for i in reversed(list(suggestions))]
    

    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best