import stats_and_mods
import random


def combined_functions(func_list):
    for f in func_list: f()


def can_sneak(weapon, advantaged, disadvantaged, flanking):
    weapon_properties = stats_and_mods.weapons_stats[weapon]["properties"]
    return (
            not disadvantaged and
            ("ranged" in weapon_properties or "finesse" in weapon_properties) and
            (advantaged or flanking)
    )

def roll_dice(die, num_rolls):
    return [random.randint(1, die) for _ in range(0, num_rolls)]