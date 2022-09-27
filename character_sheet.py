"""
Character sheet
"""
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
    'Barbarian': 4,
    'Bard': 4,
    'Cleric': 4,
    'Druid': 4,
    'Fighter': 4,
    'Monk': 4,
    'Paladin': 4,
    'Rogue': 4,
    'Sorcerer': 4,
    'Warlock': 6,
    'Wizard': 4,
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
your_character = {
    'Race': '',
    'Class': '',
    'Level': '',
    'Hit points': '',
}
# Ability scores that will be calculated in the fifth choice,
# these will affect the skill values
your_ability_scores = {
    'Strength': '',
    'Dexterity': '',
    'Constitution': '',
    'Intellegence': '',
    'Wisdom': '',
    'Charisma': '',
}
your_ability_saving_throws = {
    'Strength': '',
    'Dexterity': '',
    'Constitution': '',
    'Intellegence': '',
    'wisdom': '',
    'Charisma': '',
}
your_ability_scores_modifiers = {
    'Strength': '',
    'Dexterity': '',
    'Constitution': '',
    'Intellegence': '',
    'wisdom': '',
    'Charisma': '',
}
# skills and proficencies that will be assigned in the sixth choice
your_skills_and_proficiencies = {
    'proficency_bonus': '',
    'proficient skill 1': '',
    'proficient skill 2': '',
    'Acrobatics': '',
    'Animal Handling': '',
    'Arcana': '',
    'Athletics': '',
    'Deception': '',
    'History': '',
    'Insight': '',
    'Intimidation': '',
    'Investigation': '',
    'Medicine': '',
    'Nature': '',
    'Perception': '',
    'Performance': '',
    'Persuasion': '',
    'Religion': '',
    'Sleight of Hand': '',
    'Stealth': '',
    'Survival': '',
}
your_feats_and_traits = {

}
your_spells_and_attacks = {

}
