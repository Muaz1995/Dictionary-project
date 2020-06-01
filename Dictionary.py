import json
from difflib import get_close_matches

dictionary = r"C:\Users\USER\Desktop\Dictionary App\data.json"

def write_json(data):
    with open(dictionary, "w") as f:
        json.dump(data, f)

def translate(word):
    data = json.load(open(dictionary))
    if word in data:
        return data[word]            
    elif len(get_close_matches(word,data.keys())) > 0:
        matches = get_close_matches(word,data.keys())[0]
        user_input = input(f"You have input a wrong word. Did you mean {matches}. y/n: ").lower()
        if user_input == "y":
            return data[matches]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif user_input == "n":
            user_again = input("Please enter the word again: or type 'add' to add it to the dictionary. ? ")
            if user_again != "add":
                return translate(user_again)
            else:
                definition = input("Definition: ")
                data[word] = []
                data[word].append(definition)
                write_json(data)
                return f"{word} added to the dictionary as: {definition}."

word = input("Enter word: ").lower()
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)