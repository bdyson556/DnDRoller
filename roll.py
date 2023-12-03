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