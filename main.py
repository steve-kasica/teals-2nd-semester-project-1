import requests
import nltk
from nltk import word_tokenize
from random import randint

key = 'HO5sagAkDfE09Wv4DFOudFAou8gcTRpL'

# Step 1: Display story title
title = 'Remix the News: a Mad Lib'
print(title)

welcome = 'Welcome! You are about to play a fantastic word game. I will ask you for nouns, verbs, adjectives, and proper nouns. Using those words I will create an unexpected story for you!'
print(welcome, '\n')

# Step 2: Get the summary of a random story on the front page of The New York Times
url = 'https://api.nytimes.com/svc/topstories/v2/home.json?api-key=' + key
res = requests.get(url)
articles = res.json()['results']
index = randint(0, len(articles))
abstract = articles[index]['abstract']

# Step 3: Tag the part of speech for each word in the article's abstract
text = word_tokenize(abstract)
tags = nltk.pos_tag(text)

# Step 4: Prompt the user to replace nouns, verbs, and adjectives from the article's abstract
story = ''
for tag in tags:
    word = ''
    pos = tag[1]  # the second item in the tuple is the Part Of Speech
    if (pos == 'NN'):  # NN means noun
        word = input('Give me a noun: ')
    elif (pos == 'NNS'):  # NNS means plural noun
        word = input('Give me a plural noun: ')
    elif (pos == 'VB'):  # VB means verb
        word = input('Give me a verb: ')
    elif (pos == 'NNP'):  # NNP means proper noun
        word = input('Give me a proper noun: ')
    elif (pos == 'NNPS'):  # NNPS means plural proper noun
        word = input('Give me a plural proper noun: ')
    elif (pos == 'JJ'):  # JJ means adjective
        word = input('Give me an adjecive: ')
    else:
        word = tag[0]
    story = story + word + ' '

# Step 5: Display MadLib story back to user
print('\n' + story)