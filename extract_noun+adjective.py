#from __future__ import unicode_literals

import csv
import spacy


f = file("labeledTrainData.tsv")
tsv = csv.reader(f, delimiter='\t')

i=1
data = []
nlp = spacy.load('en')

for line in tsv:
    if i == 1:
        i = i + 1
        continue
    else:
        sentence = ""
        id = line[0].split("_")
        doc = nlp(line[2].decode('utf8'))
        for token in doc:
            if token.pos_ in ('NOUN', 'ADJ') or token.text in [',', '.']:
                sentence = sentence + " " + token.text
        sentence = sentence.encode('utf8')
        id.append(sentence)
        # print i
        # print id
        data.append(id)
    i=i+1
    if i%100 == 0:
        print i
w = open('traindata_nlp.tsv', 'w')
writer = csv.writer(w, delimiter="\t")
writer.writerow(["id", "sentiment", "review"])
writer.writerows(data)
w.close()
