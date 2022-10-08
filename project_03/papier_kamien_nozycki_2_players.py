import sys

player_1 = input('Podaj imie player_1: ')
player_2 = input('Podaj imie player_2: ')

player_1_odpowiedz = input(f'Hej {player_1} wybierz papier, kamien lub nozyczki: ')
player_2_odpowiedz = input(f'Hej {player_2} wybierz papier, kamien lub nozyczki: ')


def compare(answer1, answer2):

            if answer1 == answer2:
                return('remis :)')

            elif answer1 == 'papier':
                if answer2 == 'kamien':
                    return(f'Brawo! {player_1} wygrywasz wybierając {answer1}:)')
                else:
                    return(f'Brawo! {player_2} wygrywasz wybierajac {answer2} :)')

            elif answer1 == 'kamien':
                if answer2 == 'nozyczki':
                    return (f'Brawo! {player_1} wygrywasz wybierając {answer1}:)')
                else:
                    return (f'Brawo! {player_2} wygrywasz wybierajac {answer2} :)')

            elif answer1 == 'nozyczki':
                if answer2 == 'papier':
                    return (f'Brawo! {player_1} wygrywasz wybierając {answer1}:)')
                else:
                    return (f'Brawo! {player_2} wygrywasz wybierajac {answer2} :)')

            else:
                print('To nie jest prawidłowy wybór')
                sys.exit()



print(compare(player_1_odpowiedz,player_2_odpowiedz))
