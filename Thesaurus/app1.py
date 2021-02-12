import json

data = json.load(open("data.json"))

def lookup(w):
    return data[w]

word = input("Enter Word: ")

print(lookup(word))