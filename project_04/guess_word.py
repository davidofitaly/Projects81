import random
from os import system,name

random_words_to_guess = ['wakacje', 'slonce', 'plaza','python', 'tosia', 'koala']


def pick_a_word(list_words):
    """The function selects a word from the list """
    drawn_word = random.choice(random_words_to_guess)

    return drawn_word


def array_for_str(arrays):
    """Function that converts arrays into str"""
    str1 = ""

    for i in arrays:
        str1 += i + " "

    return str1

def check_to_input(input_g):
    if(input_g == ""):
        print('Brak odpowiedzi! Twoja odpowiedzi musi zawierac jedna litere')
    elif len(input_g) > 1:
        print('Podałes za duzo liter')


def guess_word(word):
    """The function turns word into stars"""
    anwers_player = []
    for i in word:
        anwers_player.append("*")

    lives = 8

    while(lives > 0):
        print(f'\nMasz jeszcze {lives} żyć, aby zgadnac slowo')
        print('Tajemne slowo: '+ " " + array_for_str(anwers_player))
        print('Podaj jedna litere: ')
        input_g = input().upper()

        check_to_input(input_g)




    print(word)
    print(anwers_player)


guess_word((pick_a_word(random_words_to_guess)))




