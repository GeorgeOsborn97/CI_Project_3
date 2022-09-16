"""
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3_test_sheet')

your_character = {
    'Race': '',
    'Class': '',
    'Level': '',
    'Hit points': '',
}    
your_ability_scores = {  
    'Strength': '',
    'Dexterity': '',
    'Constitution': '',
    'Intellegence': '',
    'wisdom': '',
    'Charisma': '',
}
your_skills_and_proficiencies = {
    'proficency_modifier': '',
}
your_feats_and_traits = {

}
your_spells_and_attacks = {

}

races = SHEET.worksheet('Races')
race = races.get_all_values()
classes = SHEET.worksheet('Classes')
classes_values = classes.get_all_values()
print('Welcome to the Dungeons and Drgaons character creator!')
print('To begin please choose from one of the following races.')
print(race)
xy = 1
yz = 1


def first_choice():
    """
    users first choice
    """
    while xy == 1:
        def select_race(prompt):
            """
            Return the users chosen race
            """
            return input(prompt)
        global chosen_race
        chosen_race = select_race('Type a race here to see their traits and starting abilities: ')

        def pull_racial_traits(choosen_race):
            """
            Pull the relevent racial traits
            """
            global xy
            try:
                trait_sheet = SHEET.worksheet(choosen_race)
                racial_traits = trait_sheet.get_all_values()
                print(racial_traits)
                xy += 1

            except Exception:
                print(f'{choosen_race} is not a playable Race, please select again.')

        pull_racial_traits(chosen_race)


first_choice()


def confirm_race(prompt):
    """
    confirm the users chosen race
    """
    return input(prompt)


confirmed_race = None
while confirmed_race != 'Yes':
    confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No" ')
    if confirmed_race == 'Yes':
        print(f'{chosen_race} confirmed!')
    elif confirmed_race == 'No':
        xy = 1
        print('change decision')
        first_choice()
        confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No" ')
        if confirmed_race == 'Yes':
            print(f'{chosen_race} confirmed!')
    else:
        print('Please only type "Yes" or "No".')
        confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No" ')
        if confirmed_race == 'Yes':
            print(f'{chosen_race} confirmed!')

your_character['Race'] = chosen_race
print(your_character)
print('end of step one')

print("Now you that you have chosen a race for your chracter it's time to pick a class")
print('Please choose from one of the following classes.')
print(classes_values)


def second_choice():
    """
    users second choice
    """
    while yz == 1:
        def select_class(prompt):
            """
            Return the users chosen class
            """
            return input(prompt)
        global chosen_class
        chosen_class = select_class('Type a class here to see their description and abilities: ')

        def pull_class_traits(choosen_class):
            """
            Pull the relevent racial traits
            """
            global yz
            try:
                trait_sheet = SHEET.worksheet(choosen_class)
                class_traits = trait_sheet.get_all_values()
                print(class_traits)
                yz += 1

            except Exception:
                print(f'{choosen_class} is not a playable class, please select again.')

        pull_class_traits(chosen_class)


second_choice()


def confirm_class(prompt):
    """
    confirm the users chosen class
    """
    return input(prompt)


confirmed_class = None
while confirmed_class != 'Yes':
    confirmed_class = confirm_class(f'Are you sure you want to choose {chosen_class}? Please answer "Yes" or "No" ')
    if confirmed_class == 'Yes':
        print(f'{chosen_class} confirmed!')
    elif confirmed_class == 'No':
        yz = 1
        print('change decision')
        second_choice()
        confirmed_class = confirm_class(f'Are you sure you want to choose {chosen_class}? Please answer "Yes" or "No" ')
        if confirmed_class == 'Yes':
            print(f'{chosen_class} confirmed!')
    else:
        print('Please only type "Yes" or "No".')
        confirmed_class = confirm_class(f'Are you sure you want to choose {chosen_class}? Please answer "Yes" or "No" ')
        if confirmed_class == 'Yes':
            print(f'{chosen_class} confirmed!')

your_character['Class'] = chosen_class
print(your_character)
print('end of step two')
