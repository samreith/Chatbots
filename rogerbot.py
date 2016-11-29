#!/usr/bin/env python

# Default bot template

# from chatServer import sleep, output
import chatServer as c
import random

def setup():
    c.output("This is the rogor.")
    c.sleep(1)
    c.output("hallo")

def response(input):
    # print(input)
    if not respondToTrigger(input):
        output(randomResponse())

def randomResponse():
    answers = [
    "ok"
    "hallo"
    ]
    return random.choice(answers)

def respondToTrigger(input):
    if "assignment" in input:
    output("the assignment...")
    return True
    return False
