"""
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
import os
import random
import gspread
import pandas as pd
from tabulate import tabulate
from google.oauth2.service_account import Credentials
from class_info import class_hit_dice
from class_info import class_info
from class_info import race_info
from class_info import colour_scheme
from class_info import dragonborn
from class_info import bard_spell_data
from class_info import cleric_spell_data
from class_info import druid_spell_data
from class_info import paladin_spell_data
from class_info import sorcerer_spell_data
from class_info import warlock_spell_data
from class_info import wizard_spell_data
from class_info import weapon_list
from character_sheet import your_character
from character_sheet import your_ability_scores
from character_sheet import your_ability_scores_modifiers
from character_sheet import your_ability_saving_throws
from character_sheet import your_skills_and_proficiencies
from character_sheet import your_spells_and_attacks

# connection to google sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3_test_sheet')


# These first 3 functions are pre ones that are called back on later
# at specific points in the program
# This creates the red title that sits perminatly at the top of the terminal
def create_title():
    """
    Create title
    """
    print("\033[1;31m")
    print('DND Character Creator'.center(80, '-'))
    print('\n')


# the random number generator / dice roller that is used to roll HP
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


# This function calculates the charcaters hit points using their class
# and the dice selected from the function above
def hit_dice_roller():
    """
    Class specific hit dice roller
    """
    dice = class_hit_dice[(your_character['Class'])]
    y = int(your_character['Level'])
    print("\033[38;5;231mIt's time to roll hit points for your charcter!")
    print(f"{(your_character['Class'])}'s hit dice are: {dice}\n")
    x = 0
    sum_dice = []
    while x < y:
        result = rand_num(dice)
        sum_dice.append(result)
        x += 1
    print(
        f'You rolled {sum_dice}'
    )
    return sum(sum_dice)


# varibales set at the module level that get called upon later
RACES = None
RACE = None
CLASSES = None
CLASSES_VALUES = None
race_loop = None
class_loop = None
level_loop = 1
old_score = None
cantrip_loop = None


# This function creates an introduction to help the user understand
# the purpose of the application
def begin(prompt):
    """
    creates an introductory page
    """
    create_title()
    print(
        '\033[38;5;231mWelcome to '
        'the Dungeons and Dragons character creator!\n'.center(80)
    )
    print('\033[1;31mIMPORTANT INFORMATION:\n'.center(80))
    print(
        '\033[38;5;231m'
        'This application has been designed to help demonstrate and showcase '
        'the kind of character you may look to create when beginning a '
        'campaign in D&D. The Focus of the "Character Sheet" '
        'which you will be building are your ability scores and spells '
        'as they are arguably the most important and the most fun. '
        'You will be shown a lot of information when selecting '
        'a Race and a Class. This information will not affect the '
        '"character sheet" at the end of this applicatiion, '
        'but is there to show you what a charcater would look like '
        'in a real game. There are also hundreds more spells,'
        'abilities and featutres that I could not fit in this creator.'
        'However a lot are touched on when selecting a class and race'
        'so keep those things in mind. Finally be aware,'
        'if you cant see the DND Character Creator Logo,'
        'you can scroll up to see more information.\n'
    )

    return input(prompt)


begin("Please press 'Enter' to get started! \n")


# This function creates a list of playable races and 
# sets a few variables that are used later
def create_initial_conditions():
    """
    Sets a few global variables. and presents the first choice to the users
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    global RACES
    RACES = SHEET.worksheet('Races')
    global RACE
    RACE = RACES.get_all_values()
    global CLASSES
    CLASSES = SHEET.worksheet('Classes')
    global CLASSES_VALUES
    CLASSES_VALUES = CLASSES.get_all_values()
    print(
        '\033[38;5;231m'
        'To begin please choose from one of the following races.\n'.center(80)
    )
    df_race = pd.DataFrame(RACES.row_values(1))
    print(f'{df_race.to_string(index=False, header=None)}\n')
    global race_loop
    race_loop = 1
    global class_loop
    class_loop = 1
    global old_score
    old_score = None


create_initial_conditions()

# when this function is called
# it finds and displays information regarding the users chosen race


def pull_racial_traits():
    """
    Pull the relevent racial traits
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    # firstly it tries to find a sheet that matches what the user inputs
    try:
        trait_sheet = SHEET.worksheet(chosen_race)
        info_count = race_info[f'{chosen_race}']
        text_colour = colour_scheme[f'{chosen_race}']
        create_title()
        print(f'{text_colour}{chosen_race}'.center(80))
        global i
        i = 1
        # after finding a sheet this funcyion allows the user to cycle through
        # the information
        while i < info_count:
            def cycle_info(prompt):
                global i
                df_race_info = pd.DataFrame(
                    trait_sheet.col_values(i)
                ).iloc[1:2]
                print(
                    f'{text_colour}'
                    f'{df_race_info.to_string(index=False, header=None)}\n'
                )
                i += 1
                if i == 10 and chosen_race == 'Dragonborn':
                    print(dragonborn)
                return input(prompt)
            cycle_info('Click enter to cycle through info: ')
            os.system('cls' if os.name == 'nt' else 'clear')
            create_title()
            print(f'{text_colour}{chosen_race}'.center(80))
        global race_loop
        race_loop += 1
# if the users input is not find in a sheet they are asked to choose again.
    except Exception:
        print(
            f'{chosen_race} is not a playable Race,'
            ' please select again.'
        )
        df_race = pd.DataFrame(RACES.row_values(1))
        print(f'{df_race.to_string(index=False, header=None)}\n')


def first_choice():
    """
    users first choice
    """
    while race_loop == 1:
        def select_race(prompt):
            """
            Return the users chosen race
            """
            return input(prompt).capitalize()
        global chosen_race
        chosen_race = select_race(
            'Type a race here to see their traits and starting abilities: \n'
        )
# connects to google sheets to pull the information about each race
        pull_racial_traits()


first_choice()

# The first confirmation that allows the user to confirm their chosen race
#  or go back and select again


def confirm_race(prompt):
    """
    get the user to manually confirm or deny the chosen race
    """
    return input(prompt).capitalize()


def race_confirmation():
    """
    Test the users input to either move on or allow the user to choose again.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    confirmed_race = None
    while confirmed_race != 'Yes':
        confirmed_race = confirm_race(
            f'Are you sure you want to choose {chosen_race}?'
            ' Please answer "Yes" or "No" \n'
        )
        if confirmed_race == 'Yes':
            print(f'{chosen_race} confirmed! \n')
        elif confirmed_race == 'No':
            global race_loop
            race_loop = 1
            print('change decision')
            df_race = pd.DataFrame(RACES.row_values(1))
            print(f'{df_race.to_string(index=False, header=None)}\n')
            first_choice()
        else:
            print('Please only type "Yes" or "No".')
    os.system('cls' if os.name == 'nt' else 'clear')
    your_character['Race'] = chosen_race
    print(your_character)
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    print(
        "\033[38;5;231mNow that you have chosen a race for your character"
        " it's time to pick a class"
    )
    print('Please choose from one of the following classes.\n')
    df_class = pd.DataFrame(CLASSES.row_values(1))
    print(f'{df_class.to_string(index=False, header=None)}\n')


race_confirmation()
# Second choice that allows the user to choose a class for the charcter
#  this acts in the same way as the first function


def pull_class_traits():
    """
    Pull the relevent class traits
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    global class_loop
    try:
        trait_sheet = SHEET.worksheet(chosen_class)
        info_count = class_info[f'{chosen_class}']
        global class_colour
        class_colour = colour_scheme[f'{chosen_class}']
        create_title()
        print(f'{class_colour}{chosen_class}\n'.center(80))
        global i
        i = 1
        while i < info_count:
            def cycle_info(prompt):
                global i
                df_class_info = pd.DataFrame(
                    trait_sheet.col_values(i)
                ).iloc[1:2]
                print(
                    f'{class_colour}'
                    f'{df_class_info.to_string(index=False, header=None)}\n'
                )
                i += 1
                return input(prompt)
            cycle_info('Click enter to cycle through info: ')
            os.system('cls' if os.name == 'nt' else 'clear')
            create_title()
            print(f'{class_colour}{chosen_class}\n'.center(80))
        class_loop += 1

    except Exception:
        print(
            f'{chosen_class}'
            ' is not a playable class, please select again.'
        )
        df_class = pd.DataFrame(CLASSES.row_values(1))
        print(f'{df_class.to_string(index=False, header=None)}\n')


def second_choice():
    """
    users second choice
    """
    while class_loop == 1:
        def select_class(prompt):
            """
            Return the users chosen class
            """
            return input(prompt).capitalize()
        global chosen_class
        chosen_class = select_class(
            'Type a class here to see their description and abilities: \n'
        )

        pull_class_traits()


second_choice()

# confirm the class choice, allows the the user to say No and pick again.


def confirm_class(prompt):
    """
    Get the users to manually confirm or deny the chosen class
    """
    return input(prompt).capitalize()


def class_confirmation():
    """
    Test the users input to either move on or allow the user to choose again.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    confirmed_class = None
    while confirmed_class != 'Yes':
        confirmed_class = confirm_class(
            f'Are you sure you want to choose {chosen_class}? '
            'Please answer "Yes" or "No" \n'
        )
        if confirmed_class == 'Yes':
            print(f'{chosen_class} confirmed!')
        elif confirmed_class == 'No':
            global class_loop
            class_loop = 1
            print('change decision')
            df_class = pd.DataFrame(CLASSES.row_values(1))
            print(f'{df_class.to_string(index=False, header=None)}\n')
            second_choice()
        else:
            print('Please only type "Yes" or "No".')
    your_character['Class'] = chosen_class
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    print(
        "\033[38;5;231mNow that you have chosen a race and class"
        " for your character it's time to pick a level"
    )
    print('Please choose from a level from 1 - 20')


class_confirmation()
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
    chosen_level = choose_level('Please choose your level: \n')


third_choice()

# confirm level


def confirm_level(prompt):
    """
    confirm the users chosen level
    """
    return input(prompt).capitalize()


def level_confirmation():
    """
    confirm level
    """
    global level_loop
    while level_loop == 1:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            create_title()
            if int(chosen_level) <= 0:
                print(
                    f'{chosen_level} is not a valid character level'
                    ' please select again'
                )
                third_choice()
            elif int(chosen_level) > 20:
                print(
                    f'{chosen_level} exceeds the maximun level, '
                    'please pick again'
                )
                third_choice()
            else:
                level_loop += 1
        except Exception:
            print('Please only choose a number between 1 and 20')
            third_choice()

    confirmed_level = None
    while confirmed_level != 'Yes':
        confirmed_level = confirm_level(
            f'Are you sure you want to choose {chosen_level}? '
            'Please answer "Yes" or "No" \n'
        )
        if confirmed_level == 'Yes':
            print(f'{chosen_level} confirmed!')
        elif confirmed_level == 'No':
            level_loop = 1
            print('change decision')
            third_choice()
            level_confirmation()
        else:
            print('Please only type "Yes" or "No".')
    your_character['Level'] = chosen_level
    os.system('cls' if os.name == 'nt' else 'clear')


level_confirmation()
# hit points are rolled based on the level and class of the character


def forth_choice(prompt):
    """
    roll hit points
    """
    create_title()
    hit_points = hit_dice_roller()
    your_character['Hit points'] = hit_points
    print('Lets see how your charcter is looking! \n')
    print(f'{class_colour}{your_character}')
    return input(prompt)


forth_choice("Please press 'Enter' to move on: ")


def ability_score_intro():
    """
    print a paragraph to the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    print(
        "\033[38;5;231mNow it's time to calculate your ability scores. "
        "You will be shown the sum of 3 d6 rolls, "
        "you will then be asked which ability to assign this score to. "
        "This will be reapeated 6 times."
    )


ability_score_intro()
# calculate rolls and allow the user to asign the results to the 6 abilities


def fifth_choice():
    """
    Calculate ability scores
    """
    rolls = []
    for x in range(1, 4, 1):
        x = rand_num('d6')
        rolls.append(x)
    print(f'\033[38;5;231m{rolls}')
    global your_score
    your_score = sum(rolls)
    print(f'\033[38;5;118m{your_score}')


while "" in your_ability_scores.values():
    if old_score is None:
        global reassign_check
        reassign_check = None
        fifth_choice()
    else:
        your_score = old_score
        print(f'Please Re-assign {your_score}')
        reassign_check = 1

    def select_ability(prompt):
        """
        add the rolled score to any ability score
        """
        return input(prompt).capitalize()

    print(f'\033[38;5;231m{your_ability_scores}')
    chosen_ability = select_ability(
        "\033[38;5;231mChoose one of the abilities to add this score to: \n"
    )
    while chosen_ability not in your_ability_scores:
        print('please choose only one of the above abilities')
        chosen_ability = select_ability(
            "Choose one of the abilities to add this score to: \n"
        )
    if your_ability_scores[f'{chosen_ability}'] != "":
        old_score = your_ability_scores[f'{chosen_ability}']
        if reassign_check == 1:
            reassign_check = 2
# confirm the choice of ability scores

    def confirm_ability(prompt):
        """
        confirm the ability
        """
        return input(prompt).capitalize()

    def calc_prof_mod():
        """
        calculate ability score modifiers
        """
        if int(your_character['Level']) <= 4:
            your_skills_and_proficiencies['proficency_bonus'] = 2
        elif int(your_character[
            'Level'
        ]) > 4 and int(your_character['Level']) <= 8:
            your_skills_and_proficiencies['proficency_bonus'] = 3
        elif int(your_character[
            'Level'
        ]) > 8 and int(your_character['Level']) <= 12:
            your_skills_and_proficiencies['proficency_bonus'] = 4
        elif int(your_character[
            'Level'
        ]) > 12 and int(your_character['Level']) <= 6:
            your_skills_and_proficiencies['proficency_bonus'] = 5
        else:
            your_skills_and_proficiencies['proficency_bonus'] = 6

    def calc_mods():
        """
        calculate ability score modifiers
        """
        if your_score % 2 == 0:
            your_ability_scores_modifiers[
                f'{chosen_ability}'
            ] = int(-4 + ((your_score / 2) - 1))
        else:
            your_ability_scores_modifiers[
                f'{chosen_ability}'
            ] = int(-4 + (((your_score - 1) / 2) - 1))

        your_skills_and_proficiencies[
            'Acrobatics'
        ] = your_ability_scores_modifiers['Dexterity']
        your_skills_and_proficiencies[
            'Animal Handling'
        ] = your_ability_scores_modifiers['Wisdom']
        your_skills_and_proficiencies[
            'Arcana'
        ] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies[
            'Athletics'
        ] = your_ability_scores_modifiers['Strength']
        your_skills_and_proficiencies[
            'Deception'
        ] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies[
            'History'
        ] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies[
            'Insight'
        ] = your_ability_scores_modifiers['Wisdom']
        your_skills_and_proficiencies[
            'Intimidation'
        ] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies[
            'Investigation'
        ] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies[
            'Medicine'
        ] = your_ability_scores_modifiers['Wisdom']
        your_skills_and_proficiencies[
            'Nature'
        ] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies[
            'Perception'
        ] = your_ability_scores_modifiers['Wisdom']
        your_skills_and_proficiencies[
            'Performance'
        ] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies[
            'Persuasion'
        ] = your_ability_scores_modifiers['Charisma']
        your_skills_and_proficiencies[
            'Religion'
        ] = your_ability_scores_modifiers['Intellegence']
        your_skills_and_proficiencies[
            'Sleight of Hand'
        ] = your_ability_scores_modifiers['Dexterity']
        your_skills_and_proficiencies[
            'Stealth'
        ] = your_ability_scores_modifiers['Dexterity']
        your_skills_and_proficiencies[
            'Survival'
        ] = your_ability_scores_modifiers['Wisdom']
        your_ability_saving_throws[
            'Strength'
        ] = your_ability_scores_modifiers['Strength']
        your_ability_saving_throws[
            'Dexterity'
        ] = your_ability_scores_modifiers['Dexterity']
        your_ability_saving_throws[
            'Constitution'
        ] = your_ability_scores_modifiers['Constitution']
        your_ability_saving_throws[
            'Intellegence'
        ] = your_ability_scores_modifiers['Intellegence']
        your_ability_saving_throws[
            'Wisdom'
        ] = your_ability_scores_modifiers['Wisdom']
        your_ability_saving_throws[
            'Charisma'
        ] = your_ability_scores_modifiers['Charisma']
        calc_prof_mod()

    confirmed_ability = confirm_ability(
        f'Are you sure you want to add'
        f' {your_score} to {chosen_ability}? '
    )
    while confirmed_ability != 'Yes':
        if confirmed_ability == 'Yes':
            calc_mods()
            print(f'{chosen_ability} confirmed')
        elif confirmed_ability == 'No':
            reassign_check = 1
            print('change decision')
            chosen_ability = select_ability(
                "Choose one of the abilities to add the score to: \n"
            )
            confirmed_ability = confirm_ability(
                f'Are you sure you want to add {your_score}'
                f' to {chosen_ability}? '
                )
            if confirmed_ability == 'Yes':
                calc_mods()
                print(f'{chosen_ability} confirmed!')
        else:
            print('Please only type "Yes" or "No".')
            confirmed_ability = confirm_ability(
                f'Are you sure you want to add {your_score}'
                f' to {chosen_ability}? '
            )
            if confirmed_ability == 'Yes':
                calc_mods()
                print(f'{chosen_level} confirmed!')
    calc_mods()
    your_ability_scores[f'{chosen_ability}'] = your_score
    if reassign_check == 1:
        old_score = None
        reassign_check = None
    elif reassign_check == 2:
        reassign_check = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
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
        return input(prompt).capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')
    prof = SHEET.worksheet(your_character['Class'])
    create_title()
    print(
        "\033[38;5;231mNow we have your ability Scores"
        "it's time to Choose 2 proficiancies from the list below: \n"
    )
    global df_prof_info
    df_prof_info = pd.DataFrame(prof.col_values(26))
    print(f'{df_prof_info.to_string(index=False, header=None)}\n')
    prof_count = 1
    while prof_count < 3:
        chosen_prof = select_prof(
            'Choose one of the skills above as a proficency: \n'
        )
        while chosen_prof.capitalize() not in str(df_prof_info):
            print(
                'Please only choose one of the skills above as a proficency: '
            )
            chosen_prof = select_prof(
                "Choose one of the skills above as a proficency: \n"
            )
            if chosen_prof in your_skills_and_proficiencies[
                'proficient skills'
            ]:
                print(
                    f'You have akready picked {chosen_prof}'
                    ' please choose a different skill'
                )
                chosen_prof = select_prof(
                    'Type a skill here: '
                )
        your_skills_and_proficiencies[
            'proficient skills'
        ].append(chosen_prof)
        prof_count += 1


sixth_choice()


def confirm_prof(prompt):
    """
    confirm the users chosen proficiency
    """
    return input(prompt).capitalize()


def prof_confirmation():
    """
    confirm profiencies
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    confirmed_prof = None
    while confirmed_prof != 'Yes':
        your_prof = your_skills_and_proficiencies['proficient skills']
        confirmed_prof = confirm_prof(
            f'Are you sure you want to choose {your_prof}? '
            'Please answer "Yes" or "No" \n'
            'Please check your spelling here, if wrong choose "No" '
            'And retype your choices.\n'
        )
        if confirmed_prof == 'Yes':
            print('confirmed!')
        elif confirmed_prof == 'No':
            print('change decision')
            your_skills_and_proficiencies['proficient skills'] = []
            print(f'{df_prof_info.to_string(index=False, header=None)}\n')
            sixth_choice()
        else:
            print('Please only type "Yes" or "No".')
    os.system('cls' if os.name == 'nt' else 'clear')


prof_confirmation()

##############################################################################


def find_cantrip_list():
    """
    Find the correct dictionary for the chosen class
    """
    global cantrip_count
    cantrip_count = None
    global df_cantrip_col
    df_cantrip_col = None
    global df_cantrip_info_col
    df_cantrip_info_col = None
    global spell_sheet
    spell_sheet = SHEET.worksheet('Cantrips')
    if your_character['Class'] == 'Bard':
        your_spell_list = pd.DataFrame.from_dict(bard_spell_data)
        cantrip_count = your_spell_list.iloc[
            0, int(your_character['Level']) - 1
        ]
        df_cantrip_col = pd.DataFrame(spell_sheet.col_values(1))
        df_cantrip_info_col = pd.DataFrame(spell_sheet.col_values(2))
    elif your_character['Class'] == 'Cleric':
        your_spell_list = pd.DataFrame.from_dict(bard_spell_data)
        cantrip_count = your_spell_list.iloc[
            0, int(your_character['Level']) - 1
        ]
        df_cantrip_col = pd.DataFrame(spell_sheet.col_values(3))
        df_cantrip_info_col = pd.DataFrame(spell_sheet.col_values(4))
    elif your_character['Class'] == 'Druid':
        your_spell_list = pd.DataFrame.from_dict(bard_spell_data)
        cantrip_count = your_spell_list.iloc[
            0, int(your_character['Level']) - 1
        ]
        df_cantrip_col = pd.DataFrame(spell_sheet.col_values(5))
        df_cantrip_info_col = pd.DataFrame(spell_sheet.col_values(6))
    elif your_character['Class'] == 'Sorcerer':
        your_spell_list = pd.DataFrame.from_dict(bard_spell_data)
        cantrip_count = your_spell_list.iloc[
            0, int(your_character['Level']) - 1
        ]
        df_cantrip_col = pd.DataFrame(spell_sheet.col_values(9))
        df_cantrip_info_col = pd.DataFrame(spell_sheet.col_values(10))
    elif your_character['Class'] == 'Warlock':
        your_spell_list = pd.DataFrame.from_dict(bard_spell_data)
        cantrip_count = your_spell_list.iloc[
            0, int(your_character['Level']) - 1
        ]
        df_cantrip_col = pd.DataFrame(spell_sheet.col_values(11))
        df_cantrip_info_col = pd.DataFrame(spell_sheet.col_values(12))
    elif your_character['Class'] == 'Wizard':
        your_spell_list = pd.DataFrame.from_dict(bard_spell_data)
        cantrip_count = your_spell_list.iloc[
            0, int(your_character['Level']) - 1
        ]
        df_cantrip_col = pd.DataFrame(spell_sheet.col_values(9))
        df_cantrip_info_col = pd.DataFrame(spell_sheet.col_values(10))
    print(your_spell_list)
    print(cantrip_count)


if your_character['Class'] in [
    'Barbarian', 'Rogue', 'Fighter', 'Monk', 'Paladin'
]:
    print('no spells')
elif your_character['Class'] in [
    'Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard'
]:
    find_cantrip_list()


def choose_cantrips():
    """
    Choose cantrips to add to character sheet
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    global cantrip_loop
    cantrip_loop = 1
    print(
        'To begin please choose from one of the following spells.\n'.center(80)
    )
    df_cantrip = df_cantrip_col
    print(f'\033[38;5;63m{df_cantrip.to_string(index=False, header=None)}\n')


def pull_cantrip_traits(chosen_cantrip):
    """
    Pull the relevent spell information
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        create_title()
        print(f'{chosen_cantrip}'.center(80))
        c = 1
        df_cantrip_name = None
        while df_cantrip_name != f'{chosen_cantrip}':
            df_cantrip = df_cantrip_col.iloc[c]
            df_cantrip_name = df_cantrip.to_string(index=False, header=None)
            c += 1
        df_cantrip_info = df_cantrip_info_col.iloc[c - 1]
        df_cantrip_desc = df_cantrip_info
        print(f'\033[38;5;231m{df_cantrip_desc.values}')
        global cantrip_loop
        cantrip_loop += 1

    except Exception:
        print(
            f'{chosen_cantrip} is not a cantrip,'
            ' please select again.'
        )
        df_cantrip = df_cantrip_col
        print(
            f'\033[38;5;63m{df_cantrip.to_string(index=False, header=None)}\n'
        )


if your_character['Class'] in [
    'Barbarian', 'Rogue', 'Fighter', 'Monk', 'Paladin'
]:
    cantrip_count = 0
cantrips_chosen = 0
while cantrips_chosen != cantrip_count:
    def seventh_choice():
        """
        users seventh choice
        """
        choose_cantrips()
        while cantrip_loop == 1:
            def select_cantrip(prompt):
                """
                Return the users chosen spell
                """
                return input(prompt).capitalize()
            global chosen_cantrip
            chosen_cantrip = select_cantrip(
                'Type a spell here: \n'
            )
            if chosen_cantrip in your_spells_and_attacks['cantrips']:
                print(
                    f'You have akready picked {chosen_cantrip}'
                    ' please choose a different spell'
                    )
                chosen_cantrip = select_cantrip(
                    'Type a spell here: \n'
                )
            pull_cantrip_traits(chosen_cantrip)

    if your_character['Class'] in [
        'Barbarian', 'Rogue', 'Fighter', 'Monk', 'Paladin'
    ]:
        print('no spells')
    elif your_character['Class'] in [
        'Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard'
    ]:
        seventh_choice()

    def confirm_cantrip(prompt):
        """
        get the user to manually confirm or deny the chosen race
        """
        return input(prompt).capitalize()

    def cantrip_confirmation():
        """
        Test the users input to either move on or
        allow the user to choose again.
        """
        confirmed_cantrip = None
        while confirmed_cantrip != 'Yes':
            confirmed_cantrip = confirm_cantrip(
                f'Are you sure you want to choose {chosen_cantrip}?'
                ' Please answer "Yes" or "No" \n'
            )
            if confirmed_cantrip == 'Yes':
                print(f'{chosen_cantrip} confirmed! \n')
                global cantrips_chosen
                cantrips_chosen += 1
            elif confirmed_cantrip == 'No':
                global cantrip_loop
                cantrip_loop = 1
                print('change decision')
                df_cantrip = df_cantrip_col
                print(
                    f'\033[38;5;63mf'
                    f'{df_cantrip.to_string(index=False, header=None)}\n'
                )
                seventh_choice()
            else:
                print('Please only type "Yes" or "No".')
        your_spells_and_attacks['cantrips'].append(chosen_cantrip)
        print(your_spells_and_attacks)
        os.system('cls' if os.name == 'nt' else 'clear')

    if your_character['Class'] in [
        'Barbarian', 'Rogue', 'Fighter', 'Monk', 'Paladin'
    ]:
        print('you have no spells')
    elif your_character['Class'] in [
        'Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard'
    ]:
        cantrip_confirmation()
##############################################################################
##############################################################################


def find_spell_list():
    """
    Find the correct dictionary for the chosen class
    """
    global spell_count
    spell_count = None
    global df_spell_col
    df_spell_col = None
    global df_spell_info_col
    df_spell_info_col = None
    global levelled_spells_allowed
    levelled_spells_allowed = 4
    global total_spell_count
    total_spell_count = None
    global your_spell_list
    your_spell_list = None
    global spell_row_name
    spell_row_name = None
    global spell_row_desc
    spell_row_desc = None
    global spell_level
    spell_level = 1
    global spell_sheet
    spell_sheet = SHEET.worksheet('Spells')
    if your_character['Class'] == 'Bard':
        spell_row_name = 1
        spell_row_desc = 2
        your_spell_list = pd.DataFrame.from_dict(bard_spell_data)
        total_spell_count = your_spell_list.iloc[
            1, int(your_character['Level']) - 1
        ]
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(spell_sheet.row_values(spell_row_name))
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )
    elif your_character['Class'] == 'Cleric':
        spell_row_name = 1
        spell_row_desc = 2
        your_spell_list = pd.DataFrame.from_dict(cleric_spell_data)
        total_spell_count = your_spell_list.iloc[
            1, int(your_character['Level']) - 1
        ]
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(spell_sheet.row_values(spell_row_name))
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )
    elif your_character['Class'] == 'Druid':
        spell_row_name = 1
        spell_row_desc = 2
        your_spell_list = pd.DataFrame.from_dict(druid_spell_data)
        total_spell_count = your_spell_list.iloc[
            1, int(your_character['Level']) - 1
        ]
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(spell_sheet.row_values(spell_row_name))
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )
    elif your_character['Class'] == 'Paladin':
        spell_row_name = 1
        spell_row_desc = 2
        your_spell_list = pd.DataFrame.from_dict(paladin_spell_data)
        total_spell_count = your_spell_list.iloc[
            1, int(your_character['Level']) - 1
        ]
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(spell_sheet.row_values(spell_row_name))
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )
    elif your_character['Class'] == 'Sorcerer':
        spell_row_name = 1
        spell_row_desc = 2
        your_spell_list = pd.DataFrame.from_dict(sorcerer_spell_data)
        total_spell_count = your_spell_list.iloc[
            1, int(your_character['Level']) - 1
        ]
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(spell_sheet.row_values(spell_row_name))
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )
    elif your_character['Class'] == 'Warlock':
        spell_row_name = 1
        spell_row_desc = 2
        your_spell_list = pd.DataFrame.from_dict(warlock_spell_data)
        total_spell_count = your_spell_list.iloc[
            1, int(your_character['Level']) - 1
        ]
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(spell_sheet.row_values(spell_row_name))
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )
    elif your_character['Class'] == 'Wizard':
        spell_row_name = 1
        spell_row_desc = 2
        your_spell_list = pd.DataFrame.from_dict(wizard_spell_data)
        total_spell_count = your_spell_list.iloc[
            1, int(your_character['Level']) - 1
        ]
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(spell_sheet.row_values(spell_row_name))
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )


if your_character['Class'] in ['Barbarian', 'Rogue', 'Fighter', 'Monk']:
    print('no spells')
elif your_character['Class'] in [
    'Bard', 'Cleric', 'Druid', 'Paladin', 'Sorcerer', 'Warlock', 'Wizard'
]:
    find_spell_list()

if your_character['Class'] in ['Barbarian', 'Rogue', 'Fighter', 'Monk']:
    total_spell_count = 0
global total_chosen_spell
total_chosen_spell = 0
while total_chosen_spell != total_spell_count:

    def choose_spell():
        """
        Choose spells to add to character sheet
        """
        global spell_loop
        spell_loop = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        create_title()
        print(
            'To begin'
            ' please choose from one of the following spells.\n'.center(80)
        )
        df_spell = df_spell_col
        print(
            f'\033[38;5;129m{df_spell.to_string(index=False, header=None)}\n'
        )

    def pull_spell_traits(chosen_spell):
        """
        Pull the relevent racial traits
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            create_title()
            print(f'{chosen_spell}'.center(80))
            c = 0
            df_spell_name = None
            while df_spell_name != f'{chosen_spell}':
                df_spell = df_spell_col.iloc[c]
                df_spell_name = df_spell.to_string(index=False, header=None)
                c += 1
            df_spell_info = df_spell_info_col.iloc[c - 1]
            df_spell_desc = df_spell_info
            print(f'\033[38;5;231m{df_spell_desc.values}')
            global spell_loop
            spell_loop += 1

        except Exception:
            print(
                f'{chosen_spell} is not a spell,'
                ' please select again.'
            )
            df_spell = df_spell_col
            print(
                f'\033[38;5;129m'
                f'{df_spell.to_string(index=False, header=None)}\n'
            )

    spell_chosen = 0
    while spell_chosen != spell_count:
        def eighth_choice():
            """
            users first choice
            """
            choose_spell()
            while spell_loop == 1:
                def select_spell(prompt):
                    """
                    Return the users chosen race
                    """
                    return input(prompt).capitalize()
                global chosen_spell
                chosen_spell = select_spell(
                    'Type a spell here: \n'
                )
                if chosen_spell in your_spells_and_attacks[spell_level]:
                    print(
                        f'You have akready picked {chosen_spell}'
                        ' please choose a different spell'
                    )
                    chosen_spell = select_spell(
                        'Type a spell here: \n'
                    )
                pull_spell_traits(chosen_spell)

        if your_character['Class'] in [
            'Barbarian', 'Rogue', 'Fighter', 'Monk'
        ]:
            print('no spells')
        elif your_character['Class'] in [
            'Bard', 'Cleric', 'Druid', 'Paladin',
            'Sorcerer', 'Warlock', 'Wizard'
        ]:
            eighth_choice()

        def confirm_spell(prompt):
            """
            get the user to manually confirm or deny the chosen race
            """
            return input(prompt).capitalize()

        def spell_confirmation():
            """
            Test the users input to either move on or
            allow the user to choose again.
            """
            confirmed_spell = None
            while confirmed_spell != 'Yes':
                confirmed_spell = confirm_spell(
                    f'Are you sure you want to choose {chosen_spell}?'
                    ' Please answer "Yes" or "No" \n'
                )
                if confirmed_spell == 'Yes':
                    print(f'{chosen_spell} confirmed! \n')
                    global spell_chosen
                    spell_chosen += 1
                    global total_chosen_spell
                    total_chosen_spell += 1
                elif confirmed_spell == 'No':
                    global spell_loop
                    spell_loop = 1
                    print('change decision')
                    df_spell = df_spell_col
                    print(
                        f'\033[38;5;129m'
                        f'{df_spell.to_string(index=False, header=None)}\n'
                    )
                    eighth_choice()
                else:
                    print('Please only type "Yes" or "No".')
            your_spells_and_attacks[spell_level].append(chosen_spell)
            print(your_spells_and_attacks)
            os.system('cls' if os.name == 'nt' else 'clear')

        if your_character['Class'] in [
            'Barbarian', 'Rogue', 'Fighter', 'Monk'
        ]:
            print('you have no spells')
            total_chosen_spell = 1
            total_spell_count = 1
        elif your_character['Class'] in [
            'Bard', 'Cleric', 'Druid', 'Paladin', 'Sorcerer',
            'Warlock', 'Wizard'
        ]:
            spell_confirmation()
    if int(your_character['Level']) >= 3:
        levelled_spells_allowed += 1
        spell_row_name += 2
        spell_row_desc += 2
        spell_level += 1
        spell_count = your_spell_list.iloc[
            levelled_spells_allowed, int(your_character['Level']) - 1
        ]
        df_spell_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_name)
        )
        df_spell_info_col = pd.DataFrame(
            spell_sheet.row_values(spell_row_desc)
        )
##############################################################################


def select_equipment(prompt):

    return input(prompt).capitalize()


def equipment_list():
    print('Please choose two weapons from the list below.')
    if your_character['Class'] in ['Barbarian', 'Fighter', 'Paladin']:
        for i in weapon_list['Martial']:
            print(i)
        equipment_count = 1
        while equipment_count < 3:
            chosen_equipment = select_equipment(
                'Type one of the weapons to take it: \n'
            )
            while chosen_equipment.capitalize() not in str(
                weapon_list['Martial']
            ):
                print(
                    'Please only choose one of the weapons above as: '
                )
                chosen_equipment = select_equipment(
                    "Type one of the weapons to take it: \n"
                )
            your_spells_and_attacks[
                'weapons'
            ].append(chosen_equipment)
            equipment_count += 1
    elif your_character['Class'] in [
        'Bard', 'Druid', 'Monk', 'Sorcerer', 'Warlock', 'Wizard'
    ]:
        for i in weapon_list['Simple']:
            print(i)
        equipment_count = 1
        while equipment_count < 2:
            chosen_equipment = select_equipment(
                'Type one of the weapons to take it: \n'
            )
            while chosen_equipment.capitalize() not in str(
                weapon_list['Simple']
            ):
                print(
                    'Please only choose one of the weapons above as: '
                )
                chosen_equipment = select_equipment(
                    "Type one of the weapons to take it: \n"
                )
            your_spells_and_attacks[
                'weapons'
            ].append(chosen_equipment)
            equipment_count += 1
    elif your_character['Class'] == 'Cleric':
        for i in weapon_list['Martial']:
            print(i)
        equipment_count = 1
        while equipment_count < 2:
            chosen_equipment = select_equipment(
                'Type one of the weapons to take it: \n'
            )
            while chosen_equipment.capitalize() not in str(
                weapon_list['Martial']
            ):
                print(
                    'Please only choose one of the weapons above as: '
                )
                chosen_equipment = select_equipment(
                    "Type one of the weapons to take it: \n"
                )
            your_spells_and_attacks[
                'weapons'
            ].append(chosen_equipment)
            equipment_count += 1
    elif your_character['Class'] == 'Rogue':
        for i in weapon_list['Simple']:
            print(i)
        equipment_count = 1
        while equipment_count < 3:
            chosen_equipment = select_equipment(
                'Type one of the weapons to take it: \n'
            )
            while chosen_equipment.capitalize() not in str(
                weapon_list['Simple']
            ):
                print(
                    'Please only choose one of the weapons above as: '
                )
                chosen_equipment = select_equipment(
                    "Type one of the weapons to take it: \n"
                )
            your_spells_and_attacks[
                'weapons'
            ].append(chosen_equipment)
            equipment_count += 1


equipment_list()


def confirm_equipment(prompt):
    """
    confirm the users chosen level
    """
    return input(prompt).capitalize()


def equipment_confirmation():
    """
    confirm equipment
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    confirmed_equipment = None
    while confirmed_equipment != 'Yes':
        your_equipment = your_spells_and_attacks['weapons']
        confirmed_equipment = confirm_equipment(
            f'Are you sure you want to choose {your_equipment}? '
            'Please answer "Yes" or "No" \n'
            'Please check your spelling here, if wrong choose "No" '
            'And retype your choices.\n'
        )
        if confirmed_equipment == 'Yes':
            print('confirmed!')
        elif confirmed_equipment == 'No':
            print('change decision')
            your_spells_and_attacks['weapons'] = []
            equipment_list()
        else:
            print('Please only type "Yes" or "No".')
    os.system('cls' if os.name == 'nt' else 'clear')


equipment_confirmation()

####################
#####################


def choose_name(prompt):
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    print("Finally its time to name your character!".center(80))
    return input(prompt).capitalize()


character_name = choose_name('Type your characters name here: \n')
your_character['Name'] = character_name


def final_print():
    os.system('cls' if os.name == 'nt' else 'clear')
    create_title()
    character_header1 = ['Your Character', '']
    character_header2 = ['Your Ability Scores', '']
    character_header3 = ['Your Modifiers', '']
    character_header4 = ['Your Saving throws', '']
    character_header5 = ['Your Skills', '']
    character_header6 = ['Your Spells', '']
    character = tabulate(
        your_character.items(), headers=character_header1, tablefmt='grid'
    )
    character_ability = tabulate(
        your_ability_scores.items(), headers=character_header2, tablefmt='grid'
    )
    character_mods = tabulate(
        your_ability_scores_modifiers.items(),
        headers=character_header3, tablefmt='grid'
    )
    character_saves = tabulate(
        your_ability_saving_throws.items(),
        headers=character_header4, tablefmt='grid'
    )
    character_prof = tabulate(
        your_skills_and_proficiencies.items(),
        headers=character_header5, tablefmt='grid'
    )
    character_spells = tabulate(
        your_spells_and_attacks.items(),
        headers=character_header6, tablefmt='grid'
    )
    print(
        f'{class_colour}{character}\n{character_ability}\n{character_mods}\n'
        f'{class_colour}{character_saves}\n{character_prof}\n'
        f'{character_spells}\n'.center(80)
    )
    print('If you wish to create another Character please press "RUN PROGRAM"')


final_print()
