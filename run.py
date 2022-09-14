# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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

races = SHEET.worksheet('Races')
race = races.get_all_values()
print('Welcome to the Dungeons and Drgaons character creator!')
print('To begin please choose from one of the following races.')
print(race)


def select_race(prompt):
    """
    Return the users chosen race
    """
    return input(prompt)


chosen_race = select_race('Type a race here to see their traits and starting abilities: ')
print(chosen_race)


def pull_racial_traits():
    """
    Pull the relevent racial traits
    """
    trait_sheet = SHEET.worksheet('Human')
    racial_traits = trait_sheet.get_all_values()
    if chosen_race == 'Human':
        print(racial_traits)
    else:
        print('not human')


pull_racial_traits()
