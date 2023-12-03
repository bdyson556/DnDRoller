import random
import stats_and_mods

class Roller:
    def __init__(self):
        self.roll_history = []

def roll_skill(die_size, skill, advantage=False, disadvantage=False, guidance=False, misc_mod=0):
    num_rolls = 2 if advantage else 1
    rolls = []
    roll_min = 0 if die_size == 100 else 1
    for i in range(0, num_rolls):
        rolls.append(random.randint(roll_min, die_size))
    proficiency = stats_and_mods.char_stats[skill]["proficient"]
    modifier = stats_and_mods.char_stats[skill]["modifier"]
    guidance_roll = random.randint(1, 4) if guidance else 0
    result = max(rolls) + modifier + guidance_roll

    return {"skill": skill, "result": result, "rolls": rolls, "proficiency": proficiency, "modifier": modifier,
            "guidance": guidance_roll}

    # TODO test this function


def roll_damage(weapon, advantage=False, disadvantage=False, sneak=False, critical=False):    # TODO use adv/disadv
    die = stats_and_mods.weapons_stats[weapon]["die"]
    attack_type = stats_and_mods.weapons_stats[weapon]["type"]
    # ability_mod = stats_and_mods.weapons[weapon][""]
    damage_ability = stats_and_mods.char_stats["damage ability"]
    ability_mod = stats_and_mods.char_stats[damage_ability]
    print(ability_mod)
    advantage = sneak
    num_rolls = 1 + stats_and_mods.char_stats["num sneak dice"]
    critical_mod = die * num_rolls if critical else 0
    rolls = []
    for i in range(0, num_rolls):
        rolls.append(random.randint(1, die))
    result = sum(rolls) + ability_mod + critical_mod
    return {"result": result,
            "sneak": sneak,
            "advantage": advantage,
            "critical mod": f"{critical_mod} ({num_rolls} roll * d{die})",
            "rolls": f"{rolls} (= {sum(rolls)})",
            "attack type": attack_type,
            "ability modifier": f"{ability_mod} ({damage_ability})"
            }


def get_sneak_eligibility(weapon, advantage=False, disadvantage=False, flanking=False):
    finesse_or_ranged = stats_and_mods.weapons_stats[weapon]["type"] in ["finesse", "ranged"]
    return (not disadvantage) and finesse_or_ranged and (advantage or flanking)


# print(
#     roll_damage("shortsword", advantage=True, sneak=True, critical=True)
# )
# print(
#     roll_die(20, "perception", True, True)
# )

# def roll_die_with_advantage(die_size):
#     roll1 = roll_die(die_size)
#     roll2 = roll_die(die_size)
#     return {"roll1": roll1, "roll2": roll2, "max": max([roll1, roll2])}