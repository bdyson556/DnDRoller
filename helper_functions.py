import stats_and_mods


def combined_functions(func_list):
    for f in func_list: f()


def can_sneak(weapon, advantaged, disadvantaged, flanking):
    weapon_properties = stats_and_mods.weapons_stats[weapon]["properties"]
    return (
            not disadvantaged and
            ("ranged" in weapon_properties or "finesse" in weapon_properties) and
            (advantaged or flanking)
    )
