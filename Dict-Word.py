import json
from difflib import get_close_matches
data = json.load(open("/Users/Adi/Desktop/Dict_App/data.json"))
def translateword(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    #elif word.uppar() in data: 
        #return data[word.uppar]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn== "y" or yn=="Yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or "n" or "No":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    
word = input("Enter word: ")
output = translateword(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)