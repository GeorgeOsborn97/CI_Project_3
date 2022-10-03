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
from character_sheet import your_character
from character_sheet import your_ability_scores
from character_sheet import your_ability_scores_modifiers
from character_sheet import your_ability_saving_throws
from character_sheet import your_skills_and_proficiencies
from character_sheet import your_feats_and_traits
from character_sheet import your_spells_and_attacks


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
    print("\033[1;31m")
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
        ' your constituation modifier will be added to this soon.\n'
    )
    return sum(sum_dice)


def create_initial_conditions():
    """
    Creates the title and sets a few global variables.
    """
    create_title()
    global races
    races = SHEET.worksheet('Races')
    global race
    race = races.get_all_values()
    global classes
    classes = SHEET.worksheet('Classes')
    global classes_values
    classes_values = classes.get_all_values()
    print(
        '\033[38;5;231mWelcome to'
        ' the Dungeons and Drgaons character creator!'.center(80)
    )
    print(
        'To begin please choose from one of the following races.\n'.center(80)
    )
    df_race = pd.DataFrame(races.row_values(1))
    print(f'{df_race.to_string(index=False, header=None)}\n')
    global race_loop
    race_loop = 1
    global class_loop
    class_loop = 1
    global old_score
    old_score = None


create_initial_conditions()

# The users first choice that will define the characters race


def pull_racial_traits(chosen_race):
    """
    Pull the relevent racial traits
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        trait_sheet = SHEET.worksheet(chosen_race)
        info_count = race_info[f'{chosen_race}']
        text_colour = colour_scheme[f'{chosen_race}']
        create_title()
        print(f'{text_colour}{chosen_race}'.center(80))
        global i
        i = 1
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

    except Exception:
        print(
            f'{chosen_race} is not a playable Race,'
            ' please select again.'
        )
        df_race = pd.DataFrame(races.row_values(1))
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
            'Type a race here to see their traits and starting abilities: '
        )
# connects to google sheets to pull the information about each race
        pull_racial_traits(chosen_race)


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
    confirmed_race = None
    while confirmed_race != 'Yes':
        confirmed_race = confirm_race(
            f'Are you sure you want to choose {chosen_race}?'
            ' Please answer "Yes" or "No" '
        )
        if confirmed_race == 'Yes':
            print(f'{chosen_race} confirmed! \n')
        elif confirmed_race == 'No':
            global race_loop
            race_loop = 1
            print('change decision')
            df_race = pd.DataFrame(races.row_values(1))
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
        "\033[38;5;231mNow that you have chosen a race for your chracter"
        " it's time to pick a class"
    )
    print('Please choose from one of the following classes.\n')
    df_class = pd.DataFrame(classes.row_values(1))
    print(f'{df_class.to_string(index=False, header=None)}\n')


race_confirmation()
# Second choice that allows the user to choose a class for the charcter
#  this acts in the same way as the first function


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
            'Type a class here to see their description and abilities: '
        )

        def pull_class_traits(chosen_class):
            """
            Pull the relevent racial traits
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
                print(classes_values)

        pull_class_traits(chosen_class)


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
    confirmed_class = None
    while confirmed_class != 'Yes':
        confirmed_class = confirm_class(
            f'Are you sure you want to choose {chosen_class}? '
            'Please answer "Yes" or "No" '
        )
        if confirmed_class == 'Yes':
            print(f'{chosen_class} confirmed!')
        elif confirmed_class == 'No':
            global class_loop
            class_loop = 1
            print('change decision')
            df_class = pd.DataFrame(classes.row_values(1))
            print(f'{df_class.to_string(index=False, header=None)}\n')
            second_choice()
        else:
            print('Please only type "Yes" or "No".')
    your_character['Class'] = chosen_class
    os.system('cls' if os.name == 'nt' else 'clear')
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
    chosen_level = choose_level('Please choose your level: ')


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
    level_loop = 1
    while level_loop == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        if int(chosen_level) <= 0:
            print(
                f'{chosen_level} is not a valid character level'
                ' please select again'
            )
            third_choice()
        elif int(chosen_level) > 20:
            print(
                f'{chosen_level} exceeds the maximun level, please pick again'
            )
            third_choice()
        else:
            level_loop += 1

    confirmed_level = None
    while confirmed_level != 'Yes':
        confirmed_level = confirm_level(
            f'Are you sure you want to choose {chosen_level}? '
            'Please answer "Yes" or "No" '
        )
        if confirmed_level == 'Yes':
            print(f'{chosen_level} confirmed!')
        elif confirmed_level == 'No':
            level_loop = 1
            print('change decision')
            third_choice()
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
    print(rolls)
    global your_score
    your_score = sum(rolls)
    print(your_score)


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

    print(your_ability_scores)
    chosen_ability = select_ability("""Choose one of the abilities
    to add this score to: """)
    while chosen_ability not in your_ability_scores:
        print('please choose only one of the above abilities')
        chosen_ability = select_ability(
            "Choose one of the abilities to add this score to: "
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
            print('change decision')
            chosen_ability = select_ability(
                "Choose one of the abilities to add the score to: "
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
    df_prof_info = pd.DataFrame(prof.col_values(26))
    print(f'{df_prof_info.to_string(index=False, header=None)}\n')
    prof_count = 1
    while prof_count < 3:
        chosen_prof = select_prof(
            'Choose one of the skills above as a proficency: '
        )
        while chosen_prof.capitalize() not in str(df_prof_info):
            print(
                'Please only choose one of the skills above as a proficency: '
            )
            chosen_prof = select_prof(
                "Choose one of the skills above as a proficency: "
            )
        your_skills_and_proficiencies[
            f'proficient skill {prof_count}'
        ] = chosen_prof
        prof_count += 1


sixth_choice()
os.system('cls' if os.name == 'nt' else 'clear')
create_title()
character_header = ['Your Character', '']
character_header = ['Your Ability Scores', '']
character_header = ['Your Modifiers', '']
character_header = ['Your Saving throws', '']
character_header = ['Your Skills', '']
character = tabulate(
    your_character.items(), headers=character_header, tablefmt='grid'
)
abiliity_header = ['Your ability scores', '']
character_ability = tabulate(
    your_ability_scores.items(), headers=character_header, tablefmt='grid'
)
abiility_mods_header = ['Your ability score modifiers', '']
character_mods = tabulate(
    your_ability_scores_modifiers.items(),
    headers=character_header, tablefmt='grid'
)
saving_throws = ['Your ability score modifiers', '']
character_saves = tabulate(
    your_ability_saving_throws.items(),
    headers=character_header, tablefmt='grid'
)
prof_header = ['Your skills and profs', '']
character_prof = tabulate(
    your_skills_and_proficiencies.items(),
    headers=character_header, tablefmt='grid'
)
print(
    f'{character}{character_ability}'
    f'{character_mods}{character_saves}{character_prof}'
)
