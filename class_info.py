"""
table test
"""
from tabulate import tabulate
class_hit_dice = {
    'Barbarian': 'd12',
    'Bard': 'd8',
    'Cleric': 'd8',
    'Druid': 'd8',
    'Fighter': 'd10',
    'Monk': 'd8',
    'Paladin': 'd10',
    'Rogue': 'd8',
    'Sorcerer': 'd6',
    'Warlock': 'd8',
    'Wizard': 'd6',
}
race_info = {
    'Human': 6,
    'Dwarf': 11,
    'Elf': 10,
    'Half elf': 9,
    'Half orc': 10,
    'Dragonborn': 10,
    'Tiefling': 9,
    'Gnome': 8,
}
class_info = {
    'Barbarian': 26,
    'Bard': 22,
    'Cleric': 16,
    'Druid': 18,
    'Fighter': 18,
    'Monk': 22,
    'Paladin': 23,
    'Rogue': 19,
    'Sorcerer': 20,
    'Warlock': 18,
    'Wizard': 15,
}
colour_scheme = {
    'Human': '\033[38;5;3m',
    'Dwarf': '\033[38;5;8m',
    'Elf': '\033[38;5;106m',
    'Half elf': '\033[38;5;94m',
    'Half orc': '\033[38;5;64m',
    'Dragonborn': '\033[38;5;197m',
    'Tiefling': '\033[38;5;160m',
    'Gnome': '\033[38;5;118m',
    'Barbarian': '\033[38;5;130m',
    'Bard': '\033[38;5;213m',
    'Cleric': '\033[38;5;220m',
    'Druid': '\033[38;5;34m',
    'Fighter': '\033[38;5;147m',
    'Monk': '\033[38;5;179m',
    'Paladin': '\033[38;5;226m',
    'Rogue': '\033[38;5;101m',
    'Sorcerer': '\033[38;5;129m',
    'Warlock': '\033[38;5;63m',
    'Wizard': '\033[38;5;4m',
}


warlock_data1 = [['1st', 2, 'Otherworldly Patron, Pact Magic'],
                 ['2nd', 2, 'Eldritch Invocations'],
                 ['3rd', 2, 'Pact Boon'],
                 ['4th', 2, 'Ability Score Improvement'],
                 ['5th', 3, '--'],
                 ['6th', 3, 'Otherworldly Patron Feature'],
                 ['7th', 3, '--'],
                 ['8th', 3, 'Ability Score Improvement'],
                 ['9th', 4, '--'],
                 ['10th', 4, 'Otherworldly Patron feature'],
                 ['11th', 4, 'Mystic Arcanum (6th Level)'],
                 ['12th', 4, 'Ability Score Improvement'],
                 ['13th', 5, 'Mystic Arcanum (7th Level)'],
                 ['14th', 5, 'Otherworldly Patron feature'],
                 ['15th', 5, 'Mystic Arcanum (8th Level)'],
                 ['16th', 5, 'Ability Score Improvement'],
                 ['17th', 6, 'Mystic Arcanum (9th Level)'],
                 ['18th', 6, '--'],
                 ['19th', 6, 'Ability Score Improvement'],
                 ['20th', 6, 'Eldritch Master'],
                 ]
warlock_data2 = [[2, 2, 1, '1st', 0],
                 [2, 3, 2, '1st', 2],
                 [2, 4, 2, '2nd', 2],
                 [3, 5, 2, '2nd', 2],
                 [3, 6, 2, '3rd', 3],
                 [3, 7, 2, '3rd', 3],
                 [3, 8, 2, '4th', 4],
                 [3, 9, 2, '4th', 4],
                 [3, 10, 2, '5th', 5],
                 [4, 10, 2, '5th', 5],
                 [4, 11, 3, '5th', 5],
                 [4, 11, 3, '5th', 6],
                 [4, 12, 3, '5th', 6],
                 [4, 12, 3, '5th', 6],
                 [4, 13, 3, '5th', 7],
                 [4, 13, 3, '5th', 7],
                 [4, 14, 4, '5th', 7],
                 [4, 14, 4, '5th', 8],
                 [4, 15, 4, '5th', 8],
                 [4, 15, 4, '5th', 8],
                 ]

warlock_col_names1 = ['Level', 'Proficiency Bonus', 'Features']
warlock_col_names2 = ['Cantrips', 'Spells Known', 'Spell Slots', 'Slot Level', 'Invocations']
warlock1 = tabulate(warlock_data1, headers=warlock_col_names1, tablefmt='grid')
warlock2 = tabulate(warlock_data2, headers=warlock_col_names2, tablefmt='grid')
Warlock = f'{warlock1}{warlock2}'
