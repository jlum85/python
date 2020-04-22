# -*- coding: utf8 -*-
import random
import json

# quotes = [
#     "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
#     "On doit pouvoir choisir entre s'écouter parler et se faire entendre.",
#     "Autre citation.",
#     "Open classroom tuto "
# ]

# characters = [
#     "alvin et les Chipmunks",
#     "Babar",
#     "betty boop",
#     "calimero",
#     "casper",
#     "le chat potté",
#     "Kirikou"]


def read_value_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values


def get_random_item(my_list):
    rand_numb = random.randint(0, len(my_list)-1)
    item = my_list[rand_numb]
    return item


def random_character():
    all_value = read_value_from_json("characters.json", "character")
    return get_random_item(all_value)


def random_quote():
    all_value = read_value_from_json("quote.json", "quote")
    return get_random_item(all_value)


def capitalize(words):
    for word in words:
        word.capitalize()


def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{}  a dit : {}".format(character, quote)


user_answer = input(
    'Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')


while user_answer != "B":
    print(message(random_character(), random_quote()))
    print("  ")
    user_answer = input(
        'Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')


# for item in characters:
#     n_character = item.capitalize()
#     print(n_character)

# print(show_random_quote(quotes))
