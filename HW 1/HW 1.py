
import re
import json
import nltk

"""
Reads in reviews from Appliances json file into documents array.
"""
documents = []
with open("Appliances_5.json") as file:
    for line in file:
        documents.append(json.loads(line)['reviewText'])
    
for doc in documents:
    words = re.findall(r'\w+[,\.\-\']?\w+|[^\s\w\[\]\-,:;?\'\"]+',doc)
    print(words)
