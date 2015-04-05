'''
Created on Mar 3, 2013

@oriiginal author: Kevin

Modified webapp by David
'''

from flask import Flask, g, request, render_template
app = Flask(__name__)



import random

def load_list(name):
    with open(name + ".txt") as words:
        return [w.replace('\n','') for w in words]

def rand(a, b=None):
    if b:
        return random.randint(a, b)
    else:
        return random.randint(0, a-1)

def rand_unique(items, num):
    temp = items[:]
    result = []
    for i in range(num):
        item = random.choice(temp)
        result.append(item)
        temp.remove(item)
    return result

def rand_list(items, a, b):
    return make_list(rand_unique(items, rand(a, b)))

def rand_words(items, a, b):
    return " ".join(rand_unique(items, rand(a, b)))

def rand_word(items):
    return random.choice(items)

def make_list(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return items[0] + " and " + items[1]
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1] 

def capitalize(sent):
    if ord('a') <= ord(sent[0]) <= ord('z'):
        letter = chr(ord(sent[0]) + ord('A') - ord('a'))
        return letter + sent[1:]
    else:
        return sent


def generate():
    beginnings = load_list("beginnings")
    middles = load_list("middles")

    items = load_list("items")
    candos = load_list("candos")
    companies = load_list("companies")
    occupations = load_list("occupations")

    stype = rand(5)
    if stype == 0:
        company = rand_word(companies)
        occupation = rand_word(occupations)
        result = company + " for " + occupation + "s!"
    elif stype == 1:
        beginning = rand_words(beginnings, 1, 3)
        middle = rand_word(middles)
        occupation = rand_word(occupations)
        result = beginning + " " + middle + " for " + occupation + "s."
    elif stype == 2:
        cando = rand_list(candos, 2, 4)
        item = rand_word(items)
        result = cando + " your " + item + "."
    elif stype == 3:
        beginning1 = rand_word(beginnings)
        beginning2 = rand_word(beginnings)
        middle = rand_word(middles)
        item = rand_word(items)
        result = beginning1 + " " + middle + " for " + beginning2 + " " + item + "."
    elif stype == 4:
        ocupation1 = rand_word(occupations)
        ocupation2 = rand_word(occupations)
        cando = rand_word(candos)
        item = rand_word(items)
        result = "Bring together " + ocupation1 + "s and " + ocupation2 + "s to " + cando + " " + item + "."

    return capitalize(result)

def more():
    stype = rand(10)
    if stype == 0:
        datext = "NOT DISRUPTIVE ENOUGH"
    elif stype == 1:
        datext = "AYYY LMAO"
    elif stype == 2:
        datext = "GIVE ME A BETTER IDEA"
    elif stype == 3:
        datext = "GET ME INTO YCOMBINATOR"
    elif stype == 4:
        datext = "NEED MORE VC FUNDING"
    elif stype == 5:
        datext = "NEEDS MORE NODEJS"
    elif stype == 6:
        datext = "DANK MEMES"
    elif stype == 7:
        datext = "NEES MORE DISRUPTION"
    elif stype == 8:
        datext = "NOT SOCIALLY BAD ENOUGH"
    elif stype == 9:
        datext = "MORE. MORE. MORE."
    elif stype == 10:
        datext = "TOP KEK"
    return datext

@app.route('/')
def main():
    print(generate())
    return render_template('index.html', sentence=generate(), datext = more())

if __name__ == '__main__':
    app.debug = True
    app.run()
