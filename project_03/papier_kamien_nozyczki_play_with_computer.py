import sys
import random

gramy = (input("Cześć, zagramy w papier kamień nożyce? (y/n): "))
if gramy.lower() == "n":
    print("I see...")
    sys.exit(0)


player_1 = input('Podaj imie player_1: ')
bot_1 = ['kamien', 'papier', 'nozyczki']
bot = random.choice(bot_1)

player_1_odpowiedz = input(f'Hej {player_1} wybierz papier, kamien lub nozyczki: ')



def compare(answer1, answer2):


    if answer1 == answer2:
        return('remis :)')

    elif answer1 == 'papier':
        if answer2 == 'kamien':
            return(f'Brawo! {player_1} wygrywasz wybierając {answer1}:)')
        else:
            return(f'Brawo! Bot wygrywasz wybierajac {answer2} :)')

    elif answer1 == 'kamien':
        if answer2 == 'nozyczki':
            return (f'Brawo! {player_1} wygrywasz wybierając {answer1}:)')
        else:
            return (f'Brawo! Bot wygrywasz wybierajac {answer2} :)')

    elif answer1 == 'nozyczki':
        if answer2 == 'papier':
            return (f'Brawo! {player_1} wygrywasz wybierając {answer1}:)')
        else:
            return (f'Brawo! Bot wygrywasz wybierajac {answer2} :)')

    elif:
        print('To nie jest prawidłowy wybór')
        sys.exit()

print(compare(player_1_odpowiedz, bot))
