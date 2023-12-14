from hit_roller import HitRoller

def test_hit_roll_with_adv():
    roller = HitRoller()
    roller.advantage = False
    roller.roll_to_hit()
    roller.advantage = True
    roller.roll_to_hit()