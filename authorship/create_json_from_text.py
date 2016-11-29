#!/usr/bin/env python

import json

files = [
    "authorasproducer.txt",
    "barthes.txt",
    "construction.txt",
    "designerasauthor.txt",
    "fitz.txt",
    "foucalt.txt",
    "laurenrieders.txt",
    "martha.txt",
    "michaelrock.txt",
    "samreith.txt",
    "schopenhauer.txt",
    "shakespeare.txt"
]

data = {}

for filename in files:

    with open(filename) as f:
        text = f.read()

    lines = []
    prev = -1
    for (i, c) in enumerate(text):
        if c in ['.', '?', '!', ';']:
            sentence = text[prev + 1:i + 1]
            sentence = sentence.strip()
            # print sentence
            lines.append(sentence)
            prev = i
    data[filename] = lines

jsondata = json.dumps(data, indent=2)
with open("authorship.json", 'w') as jf:
    jf.write(jsondata)
