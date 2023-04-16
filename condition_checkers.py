import tkinter
import stats_and_mods

def can_sneak(weapon, advantaged, disadvantaged, flanking):
    weapon_properties = stats_and_mods.weapons_stats[weapon]["properties"]
    return (not disadvantaged and
            ("ranged" in weapon_properties or "finesse" in weapon_properties) and
            (advantaged or flanking)
            )

if __name__ == "__main__":
    print(can_sneak("shortsword", advantaged=True, disadvantaged=False, flanking=False))
    print(can_sneak("shortsword", advantaged=False, disadvantaged=False, flanking=False))
    print(can_sneak("shortsword", advantaged=False, disadvantaged=False, flanking=True))

