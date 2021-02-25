import sys
from csv import reader
import pandas as pd
import nltk.data
import re
import nltk
nltk.download('punkt')
import numpy as np
import json
import requests

file_enzyme = open("/content/enzyme.txt", "r")#import the results from the different models 
enzyme = file_enzyme.read() 
file_enzyme.close()

file_gene = open("/content/gene.txt", "r")#import the results from the different models 
gene = file_gene.read() 
file_gene.close()


file_genia = open("/content/genia.txt", "r")#import the results from the different models 
output =  file_genia.read() 
file_genia.close()


def matching_function(list_input,list_w):
  list_input = nltk.word_tokenize(list_input)
  list_w = nltk.word_tokenize(list_w)
  list_input = [word for word in list_input if len(word) > 3]#only regard words that are longer than two characters
  list_w = [word for word in list_w if len(word) > 3]#only regard words that are longer than two characters
  co_occuring_words = set(list_input) & set(list_w)#find cooccuring entities between the two collections
 #print(len(set(co_occuring_words = set(output) & set(enzyme))))#find cooccuring entities between the two collections
  print(len(co_occuring_words))
  for word_item in co_occuring_words:
    print('string contains a word from the word list: %s' % (word_item))
    
