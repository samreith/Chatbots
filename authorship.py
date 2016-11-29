#!/usr/bin/env python

# Default bot template

import chatServer as c
import json
import random


with open("authorship/authorship.json") as f:
    jsondata = f.read()
    data = json.load(jsondata)

# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


def setup():
    output("This is the bot template.")
    sleep(1)
    output('It does nothing more than just responding with "Ok".')


def response(input):
    # print(input)
    # output("Ok")
    answers = []
    for a in data.keys():
        for l in data[a]:
        if input in l:
                answers.append(l)
                print
                print l

    if len(answers)> 0;
        response = random.choice(answers)
        output(response)
        response = random.choice(answers)
        output(response)
    else:
         output("")
