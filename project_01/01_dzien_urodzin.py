"""Program, który wyświetli dzień tygodnia, w którym się urodziliśmy"""


import datetime
import calendar
from datetime import date

def translate_to_polish(day_name):
    english_to_polish_day_name  = {
        'Monday' : 'Poniedziałek',
        'Tuesday' : 'Wtorek',
        'Wednesday' : 'Środa',
        'Thursday' : 'Czwartek',
        'Friday' : 'Piątek',
        'Saturday' : 'Sbobota',
        'Sunday' : 'Niedziela'
    }

    return english_to_polish_day_name[day_name]




date_of_birth = input('Podaj swoją date urodzin w formacie dzień-miesiąc-rok (np. 1-1-2000): ')
day, month, year = date_of_birth.split('-')
print(f'Urodziłeś się {day}.{month}.{year} roku.')

date_of_birth = datetime.datetime(int(year), int(month), int(day))

day_name = calendar.day_name[date_of_birth.weekday()]
print(f'Był to {translate_to_polish(day_name)}')


how_many_years = input('Czy chcesz dodatkowo sprawdzić ile lat mineło od twoich urodzin? (WPISZ COKOLWIEK): ')

date_today = datetime.datetime(2022,9,22)
your_birthday = datetime.datetime(int(year), int(month), int(day))


how_many_years = date_today - your_birthday
x = how_many_years.days
years = int(round((x / 365)))
print((f'Żyjesz {years} lata'))



how_many_days= input('Czy chcesz dodatkowo sprawdzić ile dni mineło od twoich urodzin? (WPISZ COKOLWIEK): ')

date_today = datetime.datetime(2022,9,22)
your_birthday = datetime.datetime(int(year), int(month), int(day))


how_many_days = date_today - your_birthday
x = how_many_years.days
print((f'Żyjesz {x} dni'))





