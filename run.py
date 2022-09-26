"""
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
import random
import gspread
import os
from character_sheet import class_hit_dice
from character_sheet import class_info
from character_sheet import race_info
from character_sheet import your_character
from character_sheet import your_ability_scores
from character_sheet import your_ability_scores_modifiers
from character_sheet import your_skills_and_proficiencies
from character_sheet import your_feats_and_traits
from character_sheet import your_spells_and_attacks
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


def create_title():
    """
    Create title
    """
    print("\033[1;34m")
    print('DND Character Creator'.center(80, '-'))
    print('\n')


# the random number generator / dice roller


def rand_num(dice):
    """
    produce random numbers
    """
    if dice == 'd4':
        roll = (random.randrange(1, 5))
    elif dice == 'd6':
        roll = (random.randrange(1, 7))
    elif dice == 'd8':
        roll = (random.randrange(1, 9))
    elif dice == 'd10':
        roll = (random.randrange(1, 11))
    elif dice == 'd12':
        roll = (random.randrange(1, 13))
    elif dice == 'd20':
        roll = (random.randrange(1, 21))
    return roll

# this function calculates the charcaters hit points using their class


def hit_dice_roller():
    """
    dice roller
    """

    dice = class_hit_dice[(your_character['Class'])]
    y = int(your_character['Level'])
    print("It's time to roll hit points for your charcter!")
    print(f"{(your_character['Class'])}'s hit dice are: {dice}\n")

    x = 0
    sum_dice = []
    while x < y:
        result = rand_num(dice)
        sum_dice.append(result)
        x += 1
    print(f'You rolled {sum_dice} your constituation modifier will be added to this soon.\n')
    return sum(sum_dice)


def create_initial_conditions():
    create_title()
    races = SHEET.worksheet('Races')
    race = races.get_all_values()
    classes = SHEET.worksheet('Classes')
    global classes_values
    classes_values = classes.get_all_values()
    print('Welcome to the Dungeons and Drgaons character creator!'.center(80))
    print('To begin please choose from one of the following races.\n'.center(80))
    print(f'{race}\n')
    global xy
    xy = 1
    global yz
    yz = 1


create_initial_conditions()

# The users first choice that will define the characters race


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
# connects to google sheets to pull the information about each race

        def pull_racial_traits(choosen_race):
            """
            Pull the relevent racial traits
            """
            os.system('cls' if os.name == 'nt' else 'clear')
            global xy
            try:
                trait_sheet = SHEET.worksheet(choosen_race)
                info_count = race_info[f'{chosen_race}']
                create_title()
                print(f'{choosen_race}'.center(80))
                global i
                i = 1
                while i < info_count:
                    def cycle_info(prompt):
                        global i
                        col_one = trait_sheet.col_values(i)
                        print(f'{col_one}')
                        i += 1
                        return input(prompt)
                    cycle_info('Click enter to cycle through info: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    create_title()
                    print(f'{choosen_race}'.center(80))
                xy += 1

            except Exception:
                print(f'{choosen_race} is not a playable Race, please select again.')

        pull_racial_traits(chosen_race)


first_choice()

# The first confirmation that allows the user to confirm their chosen race or go back and select again


def confirm_race(prompt):
    """
    confirm the users chosen race
    """
    return input(prompt)


os.system('cls' if os.name == 'nt' else 'clear')
confirmed_race = None
while confirmed_race != 'Yes':
    confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No" ')
    if confirmed_race == 'Yes':
        print(f'{chosen_race} confirmed! \n')
    elif confirmed_race == 'No':
        xy = 1
        print('change decision')
        first_choice()
        confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No" ')
        if confirmed_race == 'Yes':
            print(f'{chosen_race} confirmed! \n')
    else:
        print('Please only type "Yes" or "No".')
        confirmed_race = confirm_race(f'Are you sure you want to choose {chosen_race}? Please answer "Yes" or "No" ')
        if confirmed_race == 'Yes':
            print(f'{chosen_race} confirmed! \n')
os.system('cls' if os.name == 'nt' else 'clear')
your_character['Race'] = chosen_race
print(your_character)
print('end of step one')
os.system('cls' if os.name == 'nt' else 'clear')
create_title()
print("Now you that you have chosen a race for your chracter it's time to pick a class")
print('Please choose from one of the following classes.\n')
print(f'{classes_values}\n')

# Second choice that allows the user to choose a class for the charcter this acts in the same way as the first function


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

        def pull_class_traits(chosen_class):
            """
            Pull the relevent racial traits
            """
            os.system('cls' if os.name == 'nt' else 'clear')
            global yz
            try:
                trait_sheet = SHEET.worksheet(chosen_class)
                info_count = class_info[f'{chosen_class}']
                create_title()
                print(f'{chosen_class}\n'.center(80))
                global i
                i = 1
                while i < info_count:
                    def cycle_info(prompt):
                        global i
                        col_one = trait_sheet.col_values(i)
                        print(f'{col_one}')
                        i += 1
                        return input(prompt)
                    cycle_info('Click enter to cycle through info: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    create_title()
                    print(f'{chosen_class}\n'.center(80))
                yz += 1

            except Exception:
                print(f'{chosen_class} is not a playable class, please select again.')

        pull_class_traits(chosen_class)


second_choice()

# confirm the class choice, allows the the user to say No and pick again.


def confirm_class(prompt):
    """
    confirm the users chosen class
    """
    return input(prompt)


os.system('cls' if os.name == 'nt' else 'clear')
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
print('end of step two')
os.system('cls' if os.name == 'nt' else 'clear')
print("Now you that you have chosen a race and class for your chracter it's time to pick a level")
print('Please choose from a level from 1 - 20')

# choose the level of the character


def third_choice():
    """
    users third choice
    """
    def choose_level(prompt):
        """
        pick a level
        """
        return input(prompt)
    global chosen_level    
    chosen_level = choose_level('Please choose your level: ')


third_choice()

# confirm level


def confirm_level(prompt):
    """
    confirm the users chosen level
    """
    return input(prompt)


os.system('cls' if os.name == 'nt' else 'clear')
if int(chosen_level) < 0:
    print(f'{chosen_level} is not a valid character level please select again')
    third_choice()
elif int(chosen_level) > 20:
    print(f'{chosen_level} exceeds the maximun level, please pick again')
    third_choice()

confirmed_level = None
while confirmed_level != 'Yes':
    confirmed_level = confirm_level(f'Are you sure you want to choose {chosen_level}? Please answer "Yes" or "No" ')
    if confirmed_level == 'Yes':
        print(f'{chosen_level} confirmed!')
    elif confirmed_level == 'No':
        yz = 1
        print('change decision')
        third_choice()
        confirmed_level = confirm_level(f'Are you sure you want to choose {chosen_level}? Please answer "Yes" or "No" ')
        if confirmed_level == 'Yes':
            print(f'{chosen_level} confirmed!')
    else:
        print('Please only type "Yes" or "No".')
        confirmed_level = confirm_level(f'Are you sure you want to choose {chosen_level}? Please answer "Yes" or "No" ')
        if confirmed_level == 'Yes':
            print(f'{chosen_level} confirmed!')
your_character['Level'] = chosen_level
print('end of step 3')
os.system('cls' if os.name == 'nt' else 'clear')
# hit points are rolled based on the level and class of the character


def forth_choice(prompt):
    """
    roll hit points
    """
    create_title()
    hit_points = hit_dice_roller()
    your_character['Hit points'] = hit_points
    print('Lets see how your charcter is looking! \n')
    print(your_character)
    return input(prompt)


forth_choice("Please press 'Enter' to move on: ")


os.system('cls' if os.name == 'nt' else 'clear')
print("""now it's time to calculate your ability scores.
You will be shown the sum of 3 d6 rolls,
you will then be asked which ability to assign this score to.
This will be reapeated 6 times.""")

# calculate rolls and allow the user to asign the results to the 6 ability scores


def fifth_choice():
    """
    Calculate ability scores
    """
    rolls = []
    for x in range(1, 4, 1):
        x = rand_num('d6')
        rolls.append(x)
    print(rolls)
    global your_score
    your_score = sum(rolls)
    print(your_score)


while "" in your_ability_scores.values():
    fifth_choice()

    def select_ability(prompt):
        """
        add the rolled score to any ability score
        """
        return input(prompt)

    print(your_ability_scores)
    chosen_ability = select_ability("""Choose one of the abilities
    to add this score to: """)
    while chosen_ability not in your_ability_scores:
        print('please choose only one of the above abilities')
        chosen_ability = select_ability("""Choose one of the abilities to add this score to: """)
# confirm the choice of ability scores

    def confirm_ability(prompt):
        """
        confirm the ability
        """
        return input(prompt)

    def calc_prof_mod():
        if int(your_character['Level']) <= 4:
            your_skills_and_proficiencies['proficency_bonus'] = 2
        elif int(your_character['Level']) > 4 and int(your_character['Level']) <= 8:
            your_skills_and_proficiencies['proficency_bonus'] = 3
        elif int(your_character['Level']) > 8 and int(your_character['Level']) <= 12:
            your_skills_and_proficiencies['proficency_bonus'] = 4
        elif int(your_character['Level']) > 12 and int(your_character['Level']) <= 6:
            your_skills_and_proficiencies['proficency_bonus'] = 5
        else:
            your_skills_and_proficiencies['proficency_bonus'] = 6

    def calc_mods():
        if your_score % 2 == 0:
            your_ability_scores_modifiers[f'{chosen_ability}'] = int(-4 + ((your_score / 2) - 1))
        else:
            your_ability_scores_modifiers[f'{chosen_ability}'] = int(-4 + (((your_score - 1) / 2) - 1))

        your_skills_and_proficiencies['Acrobatics'] = your_ability_scores_modifiers['Dexterity']
        your_skills_and_proficiencies['Animal Handling'] = your_ability_scores_modifiers['wisdom']
        your_skills_and_proficiencies['Arcana'] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies['Athletics'] = your_ability_scores_modifiers['Strength']
        your_skills_and_proficiencies['Deception'] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies['History'] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies['Insight'] = your_ability_scores_modifiers['wisdom']
        your_skills_and_proficiencies['Intimidation'] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies['Investigation'] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies['Medicine'] = your_ability_scores_modifiers['wisdom']
        your_skills_and_proficiencies['Nature'] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies['Perception'] = your_ability_scores_modifiers['wisdom']
        your_skills_and_proficiencies['Performance'] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies['Persuasion'] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies['Religion'] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies['Sleight of Hand'] = your_ability_scores_modifiers['Dexterity']
        your_skills_and_proficiencies['Stealth'] = your_ability_scores_modifiers['Dexterity']
        your_skills_and_proficiencies['Survival'] = your_ability_scores_modifiers['wisdom']
        calc_prof_mod()

    confirmed_ability = confirm_ability(f'''Are you sure you want to add
    {your_score} to {chosen_ability}? ''')
    while confirmed_ability != 'Yes':
        if confirmed_ability == 'Yes':
            calc_mods()
            print(f'{chosen_ability} confirmed')
        elif confirmed_ability == 'No':
            print('change decision')
            chosen_ability = select_ability("""Choose one of the abilities to add the score to: """)
            confirmed_ability = confirm_ability(f'''Are you sure you want to add {your_score} to {chosen_ability}? ''')
            if confirmed_ability == 'Yes':
                calc_mods()
                print(f'{chosen_ability} confirmed!')
        else:
            print('Please only type "Yes" or "No".')
            confirmed_ability = confirm_ability(f'''Are you sure you want to add {your_score} to {chosen_ability}? ''')
            if confirmed_level == 'Yes':
                calc_mods()
                print(f'{chosen_level} confirmed!')
    calc_mods()
    your_ability_scores[f'{chosen_ability}'] = your_score
    os.system('cls' if os.name == 'nt' else 'clear')
print(your_ability_scores)

# proficiency choice to be added after ability scores


def sixth_choice():
    """
    Choose proficiencies
    """
    def select_prof(prompt):
        """
        Return the users chosen race
        """
        return input(prompt)
    os.system('cls' if os.name == 'nt' else 'clear')
    prof = SHEET.worksheet(your_character['Class'])
    prof_list = prof.get_values('h2:h8')
    print("""Now we have your ability Scores 
    it's time to Choose 2 proficiancies from the list below: \n""")
    print(prof_list)
    prof_count = 1
    while prof_count < 3:
        chosen_prof = select_prof('Choose one of the skills above as a proficency: ')
        while chosen_prof not in your_skills_and_proficiencies:
            print('Please only choose one of the skills above as a proficency: ')
            chosen_prof = select_prof("""'Choose one of the skills above as a proficency: '""")
        your_skills_and_proficiencies[f'proficient skill {prof_count}'] = chosen_prof
        prof_count += 1


sixth_choice()
os.system('cls' if os.name == 'nt' else 'clear')
print(f'{your_character}\n')
print(f'{your_ability_scores}\n')
print(f'{your_ability_scores_modifiers}\n')
print(f'{your_skills_and_proficiencies}\n')
