import json

char_file = "char_stats.json"
weapons_file = "weapons.json"

char_stats = None
with open(char_file, "r") as f:
    char_stats = json.load(f)

weapons_stats = None
with open(weapons_file, "r") as f:
    weapons_stats = json.load(f)

def update_ability(ability, value):
    pass

def update_proficiency(proficiency, value):
    pass
    # TODO update char_stats.json, AND recalculate proficiency

def update_skill(proficiency):
    pass
    # TODO update skill modifiers based on abilities and proficiencies

def level_up():
    pass
    # TODO update proficiencies, recalculate skill mods, etc. (check docs), proficiency bonus