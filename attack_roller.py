import tkinter as tk
from tkinter import messagebox

import helper_functions
from helper_functions import *
import stats_and_mods
from display_helpers import toggle_active_disabled, display_roll_result_generic, depress_button, release_button


class AttackRoller:

    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = tk.Toplevel(main_menu.window)
        self.weapon = None
        self.advantage = tk.BooleanVar()
        self.disadvantage = tk.BooleanVar()
        self.flanking = tk.BooleanVar()
        self.sneak = tk.BooleanVar()
        self.critical = False

        self.output_box = tk.Text(self.window, width=45, height=15)
        self.output_box.grid(row=0, column=1, pady=30, rowspan=5)

        self.sneak_window = None


    def display_menu(self):
        # TODO: implement with weapon field and advantage, disadvantage checkboxes
        self.window.title("Roll to hit")
        self.window.geometry("700x450")

        weapon_label = tk.Label(self.window, text="Enter weapon used:")
        self.weapon = tk.StringVar(value="None")
        self.weapon.set("None")
        weapon_dropdown = tk.OptionMenu(self.window, self.weapon, *stats_and_mods.weapons_stats.keys())
        # TODO: Maybe when selecting weapon from dropdown, assign JSON contents of weapon to dictionary? Then they can be accessed in roll_to_hit() and elsewhere. You might need to somehow add a lambda to the dropdown for this and create a method to handle the assignment.

        advantage_checkbutton = tk.Checkbutton(
            self.window,
            text="Advantage",
            variable=self.advantage,
            command=lambda: toggle_active_disabled(self.advantage, [disadvantage_checkbutton])
        )

        disadvantage_checkbutton = tk.Checkbutton(
            self.window,
            text="Disadvantage",
            variable=self.disadvantage,
            command=lambda: toggle_active_disabled(self.disadvantage, [advantage_checkbutton])
        )

        roll_button = tk.Button(
            self.window,
            text="Roll to attack!",
            command= self.finish
        )

        sneak_checkbutton = tk.Checkbutton(
            self.window,
            text="Sneak",
            variable=self.sneak,
            command=lambda: helper_functions.combined_functions([]))

        roll_damage_button = tk.Button(self.window, text="Roll for damage!", command=lambda: self.finish_damage())

        weapon_dropdown.grid()
        roll_button.grid()

        weapon_label.grid(row=0, pady=10)
        weapon_dropdown.grid(row=1, column=0, padx=100, pady=0, sticky="w")
        advantage_checkbutton.grid(row=2, column=0, padx=100, pady=10, sticky="w")
        disadvantage_checkbutton.grid(row=3, column=0, padx=100, pady=10, sticky="w")
        sneak_checkbutton.grid(row=4, column=0, padx=100, pady=10, sticky="w")
        roll_button.grid(row=5, column=0, padx=100)
        roll_damage_button.grid(row=6, column=0, padx=100, pady=20, sticky="w")

        # Can I sneak attack? Opens new menu to check conditions.
        sneak_eligibility_label = tk.Label(self.window, text="Can I sneak attack?", cursor="hand2", fg="blue")
        sneak_eligibility_label.bind("<Button-1>", self.sneak_eligibility_menu)
        sneak_eligibility_label.place(relx=0.5, rely=0.9, anchor="e", bordermode="outside")

    def finish(self):
        if self.weapon.get() == "None":
            messagebox.showinfo("", "Oops! Please select a weapon.", parent=self.window)
        else: self.roll_to_hit()

    def finish_damage(self):
        if self.weapon.get() == "None":
            messagebox.showinfo("", "Oops! Please select a weapon.", parent=self.window)
        else: self.roll_damage()

    def roll_to_hit(self):
        self.critical = False
        is_adv = self.advantage.get()
        is_disadv = self.disadvantage.get()
        condition = {}
        num_rolls = 1
        if is_adv or is_disadv:
            num_rolls = 2
            if is_adv: condition["condition"] = "advantaged"
            else: condition["condition"] = "disadvantaged"
        weapon = self.weapon.get()
        # TODO: implement disadvantage logic
        weapon_type = stats_and_mods.weapons_stats[weapon]["ability"]
        modifier = stats_and_mods.char_stats[weapon_type]
        proficiency_bonus = int(stats_and_mods.char_stats["proficiency bonus"]) if stats_and_mods.weapons_stats[weapon]["proficiency"] else 0
        # rolls = [random.randint(1, 20) for _ in range(0, num_rolls)]
        rolls = roll_dice(20, num_rolls)
        selected_roll = max(rolls) if not self.disadvantage.get() else min(rolls)
        roll_result = selected_roll + modifier + proficiency_bonus
        full_result = {"result": roll_result, "roll": str(selected_roll) + str(f"\t {rolls} "), f"{weapon_type} modifier": modifier,
                       "proficiency bonus": proficiency_bonus}
        full_result.update(condition)
        if selected_roll == 20:
            self.critical = True
            full_result["Critical hit! "] = ""

        print(full_result)
        display_roll_result_generic(
            "Roll to hit",
            full_result,
            self.output_box
        )
        display_roll_result_generic(
            f"Roll to hit: {self.weapon.get()}",
            full_result,
            self.main_menu.output_box
        )

    def roll_damage(self):
        weapon = self.weapon.get()
        die = stats_and_mods.weapons_stats[weapon]["die"]
        attack_type = stats_and_mods.weapons_stats[weapon]["type"]
        damage_ability = stats_and_mods.char_stats["damage ability"]
        ability_mod = stats_and_mods.char_stats[damage_ability]
        num_rolls = stats_and_mods.weapons_stats[weapon]["num rolls"]  # Number of base rolls.

        num_sneak_rolls = 0
        if self.sneak.get():
            num_sneak_rolls = stats_and_mods.char_stats["num sneak dice"]
            num_rolls += num_sneak_rolls  # If sneak, add EXTRA rolls.

        critical_mod = 0 if not self.critical else die * num_rolls  # If crit, crit mod = auto max out on all dice.
        rolls = roll_dice(die, num_rolls)
        roll_result = sum(rolls) + ability_mod + critical_mod

        sneak_info = "" if not self.sneak.get() else f"     ( +{num_sneak_rolls} D{die} )"
        crit_info = "" if not self.critical else f"     ( +{num_rolls} D{die} )"

        full_result = {
            "result": roll_result,
            "rolls": f"{rolls} ( = {sum(rolls)} )",
            "sneak": str(self.sneak.get()) + sneak_info,
            "critical mod": f"{critical_mod}" + crit_info,
            "ability modifier": f"{ability_mod} ({damage_ability})",
            "attack type": attack_type
        }

        display_roll_result_generic(
            # roll_type, roll_result, box
            f"Damage roll: {weapon}",
            full_result,
            self.main_menu.output_box
        )

        self.window.destroy()

    def sneak_eligibility_menu(self, empty):
        # sneak_window = tk.Toplevel(self.window)
        self.sneak_window = tk.Toplevel(self.window)
        self.sneak_window.title("Can I sneak attack?")
        self.sneak_window.geometry("550x350")

        weapon_label = tk.Label(self.sneak_window, text="Enter weapon used:")
        weapon = tk.StringVar(value="None")
        weapon.set("None")
        weapon_dropdown = tk.OptionMenu(self.sneak_window, self.weapon, *stats_and_mods.weapons_stats.keys())

        # ADVANTAGE BUTTONS
        advantage_label = tk.Label(self.sneak_window, text="Do you have advantage?")
        yes_advantaged_button = tk.Button(
            self.sneak_window,
            text="Yes",
            command=lambda: helper_functions.combined_functions(
                [
                    lambda: self.advantage.set(True),
                    lambda: self.disadvantage.set(False),
                    lambda: depress_button(empty, yes_advantaged_button),
                    lambda: depress_button(empty, no_disadvantaged_button),
                    lambda: release_button(empty, no_advantaged_button),
                    lambda: release_button(empty, yes_disadvantaged_button),
                ]
            )
        )
        no_advantaged_button = tk.Button(
            self.sneak_window,
            text="No",
            command=lambda: helper_functions.combined_functions(
                [
                    lambda: depress_button(empty, no_advantaged_button),
                    lambda: release_button(empty, yes_advantaged_button),
                    lambda: self.advantage.set(False)
                ]
            )
        )

        # DISADVANTAGE BUTTONS
        disadvantage_label = tk.Label(self.sneak_window, text="Are you disadvantaged?")
        yes_disadvantaged_button = tk.Button(
            self.sneak_window,
            text="Yes",
            command=lambda: combined_functions(
                [
                    lambda: self.disadvantage.set(True),
                    lambda: self.advantage.set(False),
                    lambda: depress_button(empty, yes_disadvantaged_button),
                    lambda: depress_button(empty, no_advantaged_button),
                    lambda: release_button(empty, no_disadvantaged_button),
                    lambda: release_button(empty, yes_advantaged_button)
                ]
            )
        )
        no_disadvantaged_button = tk.Button(self.sneak_window, text="No", command=lambda: combined_functions(
            [
                lambda: self.disadvantage.set(False),
                lambda: depress_button(empty, no_disadvantaged_button),
                lambda: release_button(empty, yes_disadvantaged_button),
            ]
        ))

        # Are you and another enemy of the target flanking the target? Yes / No
        self.flanking = tk.BooleanVar()
        flanking_label = tk.Label(self.sneak_window, text="Are you and another enemy of the target flanking the target?")
        yes_flanking_button = tk.Button(
            self.sneak_window, text="Yes", command=lambda: combined_functions(
                [
                    lambda: self.flanking.set(True),
                    lambda: depress_button(empty, yes_flanking_button),
                    lambda: release_button(empty, no_flanking_button)
                ]
            )
        )
        no_flanking_button = tk.Button(
            self.sneak_window, text="No", command=lambda: combined_functions(
                [
                    lambda: self.flanking.set(False),
                    lambda: depress_button(empty, no_flanking_button),
                    lambda: release_button(empty, yes_flanking_button)
                ]
            )
        )

        evaluate_button = tk.Button(self.sneak_window, text="Evaluate", command=self.evaluate)

        # PLACEMENT OF BUTTONS

        weapon_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")
        weapon_dropdown.grid(row=1, column=0, padx=10, pady=15, sticky="w")

        advantage_label.grid(row=2, column=0, padx=10, pady=15, sticky="w")
        yes_advantaged_button.grid(row=2, column=1, padx=10, pady=15, sticky="w")
        no_advantaged_button.grid(row=2, column=2, padx=10, pady=15, sticky="w")

        disadvantage_label.grid(row=4, column=0, padx=10, pady=15, sticky="w")
        yes_disadvantaged_button.grid(row=4, column=1, padx=10, pady=15, sticky="w")
        no_disadvantaged_button.grid(row=4, column=2, padx=10, pady=15, sticky="w")

        flanking_label.grid(row=6, column=0, padx=10, pady=15, sticky="w")
        yes_flanking_button.grid(row=6, column=1, padx=10, pady=15, sticky="w")
        no_flanking_button.grid(row=6, column=2, padx=10, pady=15, sticky="w")

        evaluate_button.grid(row=7, padx=10, pady=15, sticky="nesw")


    def get_sneak_eligibility(self):
        types = stats_and_mods.weapons_stats[self.weapon.get()]["properties"]
        finesse_or_ranged = ("finesse" in types) or ("ranged" in types)
        can_sneak = (not self.disadvantage.get()) and finesse_or_ranged and (self.advantage.get() or self.flanking.get())
        # result = "Able to sneak!" if can_sneak else "NOT able to sneak."
        return "Able to sneak!\n" if can_sneak else "NOT able to sneak.\n"

    def evaluate(self):
        can_sneak = self.get_sneak_eligibility()
        self.output_box.insert(tk.END, str(can_sneak))
        self.sneak_window.destroy()

