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
print('Welcome to the Dungeons and Drgaons character creator!')
print('To begin please choose from one of the following races.')
print(race)
xy = 1


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


confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No"')
while confirmed_race != 'Yes':
    if confirmed_race == 'Yes':
        print(f'{chosen_race} confirmed!')
    elif confirmed_race == 'No':  
        xy = 1
        print('change decision')
        first_choice()
        confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No"')
    else:
        print('Please only type "Yes" or "No".')
        confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No"')

print('end of step one')
