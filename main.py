import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead?\nIf yes enter Y else N" % get_close_matches(word,data.keys())[0] )
        if yn=='Y':
            return get_close_matches(word,data.keys())[0]
        elif yn=='N':
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your query!!"
    else:
        return "The word doesn't exist. Please double check it"

word=input("Enter the word : ")

output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)