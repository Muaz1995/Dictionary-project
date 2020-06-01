import json
from difflib import get_close_matches

data = json.load(open(r"C:\Users\USER\Desktop\Dictionary App\data.json"))
def translate(word):
    if word in data:
        return data[word]            
    elif len(get_close_matches(word,data.keys())) > 0:
        matches = get_close_matches(word,data.keys())[0]
        user_input = input(f"You have inputted a wrong word. Did you mean {matches}. Type Y for Yes and N for No: ").lower()
        if user_input == "y":
            return data[matches]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif user_input == "n":
            user_again = input("Please enter the word again: ")
            return translate(user_again)
        else:
            return "We did not understand your input"
    else:
        print("The word either doesn't exist or it is not stored in my dictionary, Sorry :(")
        new_word = input("Would you like to add this word into the dictionary? Type Y for Yes and N for No: ").lower()
        if new_word == "y":
            definition = input("Definition: ")
            with open ("data.json") as json_file:
                data = json.load(json_file)
                temp = data.keys()
                y = {word : definition}
                temp.append(y)
                write_json(data)


word = input("Enter word: ").lower()
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

def write_json(data, filename = data.json):
    with open (filename, "w") as f:
        json.dump(data, f)
