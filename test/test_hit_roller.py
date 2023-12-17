from attack_roller import AttackRoller

def test_hit_roll_with_adv():
    roller = AttackRoller()
    roller.advantage = False
    roller.roll_to_hit()
    roller.advantage = True
    roller.roll_to_hit()