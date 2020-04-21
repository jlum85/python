# -*- coding: utf8 -*-

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"]


def show_random_quote(my_list):
    item = my_list[0]
    return item


user_answer = input(
    'Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')


while user_answer != "B":
    print(show_random_quote(quotes))
    user_answer = input(
        'Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')


for item in characters:
    n_character = item.capitalize()
    print(n_character)

print(show_random_quote(quotes))
