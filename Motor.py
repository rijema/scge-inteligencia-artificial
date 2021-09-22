import nltk
from collections import Counter
import spacy
from string import punctuation
from flask import Flask, jsonify,json


nlp = spacy.load("en_core_web_lg")
import en_core_web_lg
nlp = en_core_web_lg.load()

arquivo = open('list.json','r')
jsondata=arquivo.read()

lendo=json.loads(jsondata)
y = json.dumps(lendo['Perguntas'][0]['Mensagem'])


def get_hotwords(text):
    result = []
    pos_tag = ['ADJ', 'NOUN']
    doc = nlp(text.lower())
    for token in doc:

        if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue

        if (token.pos_ in pos_tag):
            result.append(token.text)

    return result


output = get_hotwords(y)
hashtags = [('#' + x[0]) for x in Counter(output).most_common(5)]
print(' '.join(hashtags))

with open ("saida.json","w") as f:
    json.dump(hashtags,f,indent=4)