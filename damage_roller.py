import tkinter as tk
import random
from tkinter import messagebox

import helper_functions
import stats_and_mods
from display_helpers import toggle_active_disabled, autocheck_checkboxes, depress_button, \
    release_button, display_roll_result_generic
from helper_functions import combined_functions


class DamageRoller:

    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = tk.Toplevel(main_menu.window)
        # self.window = None
        self.weapon = None
        self.advantage = None
        self.disadvantage = None
        self.flanking = None
        self.sneak = None
        self.critical = None

    def display_menu(self):
        self.window.title("Roll for damage")
        self.window.geometry("300x300")

        weapon_label = tk.Label(self.window, text="Enter weapon used:")
        self.weapon = tk.StringVar(value="None")
        self.weapon.set("None")
        weapon_dropdown = tk.OptionMenu(self.window, self.weapon, *stats_and_mods.weapons_stats.keys())

        self.sneak = tk.BooleanVar()
        sneak_checkbutton = tk.Checkbutton(
            self.window,
            text="Sneak",
            variable=self.sneak,
            command=lambda: helper_functions.combined_functions([]))

        roll_button = tk.Button(self.window, text="Roll!", command=lambda: self.finish())

        weapon_dropdown.grid()
        roll_button.grid()

        weapon_label.grid(row=0, pady=10, padx=15)
        weapon_dropdown.grid(row=1, column=0, padx=30)
        sneak_checkbutton.grid(row=3, column=0, padx=30, pady=10, sticky="w")
        roll_button.grid(row=5, column=0)

        # Can I sneak attack? Opens new menu to check conditions.
        sneak_eligibility_label = tk.Label(self.window, text="Can I sneak attack?", cursor="hand2", fg="blue")
        sneak_eligibility_label.bind("<Button-1>", self.sneak_eligibility_menu)
        sneak_eligibility_label.place(relx=0.5, rely=0.9, anchor="e", bordermode="outside")

    def finish(self):
        if self.weapon.get() == "None":
            messagebox.showinfo("", "Oops! Please select a weapon.", parent=self.window)
        else: self.roll_damage()


    def roll_damage(self):
        weapon = self.weapon.get()
        die = stats_and_mods.weapons_stats[weapon]["die"]
        num_base_rolls = stats_and_mods.weapons_stats[weapon]["num rolls"]
        attack_type = stats_and_mods.weapons_stats[weapon]["type"]
        # ability_mod = stats_and_mods.weapons[weapon][""]
        damage_ability = stats_and_mods.char_stats["damage ability"]
        ability_mod = stats_and_mods.char_stats[damage_ability]
        critical_mod = 0

        rolls = [random.randint(1, die) for i in range(0, num_base_rolls)]

        if self.sneak.get():
            num_sneak_rolls = stats_and_mods.char_stats["num sneak dice"]
            for i in range(0, num_sneak_rolls):
                rolls.append(random.randint(1, 6))
            critical_mod = 6 * num_sneak_rolls if self.critical else 0
        else:
            if self.critical: critical_mod = die

        roll_result = sum(rolls) + ability_mod + critical_mod
        full_result = {
            "result": roll_result,
            "rolls": f"{rolls} (= {sum(rolls)})",
            "sneak": self.sneak.get(),
            "critical mod": f"{critical_mod}",
            "ability modifier": f"{ability_mod} ({damage_ability})",
            "attack type": attack_type
        }

        display_roll_result_generic(
            # roll_type, roll_result, box
            "Damage roll",
            full_result,
            self.main_menu.output_box
        )

        self.window.destroy()

    def sneak_eligibility_menu(self, empty):
        sneak_menu = tk.Toplevel(self.window)
        sneak_menu.title("Can I sneak attack?")
        sneak_menu.geometry("550x300")

        weapon_label = tk.Label(sneak_menu, text="Enter weapon used:")
        weapon_label.pack(pady=10)
        weapon = tk.StringVar(value="None")
        weapon.set("None")
        weapon_dropdown = tk.OptionMenu(sneak_menu, weapon, *stats_and_mods.weapons_stats.keys())
        weapon_dropdown.pack()

        # Are you disadvantaged? Yes / No
        disadvantage_var = tk.BooleanVar()
        disadvantage_label = tk.Label(sneak_menu, text="Are you disadvantaged?")
        disadvantage_label.pack(pady=10)
        yes_disadvantaged_button = tk.Button(sneak_menu, text="Yes", command=lambda: combined_functions(
            # [lambda: depress_button(yes_disadvantaged_button[1], [no_disadvantaged_button]),
            [lambda: disadvantage_var.set(True),
             lambda: depress_button(empty, yes_disadvantaged_button),
             lambda: release_button(empty, no_disadvantaged_button),
             lambda: toggle_active_disabled(disadvantage_var, [yes_advantaged_button, no_advantaged_button])]
        ))

        no_disadvantaged_button = tk.Button(sneak_menu, text="No", command=lambda: combined_functions(
            [lambda: disadvantage_var.set(False),
             lambda: depress_button(empty, no_disadvantaged_button),
             release_button(empty, yes_disadvantaged_button),
             lambda: toggle_active_disabled(disadvantage_var, [yes_advantaged_button, no_advantaged_button])]
        ))
        yes_disadvantaged_button.pack(side="left")
        no_disadvantaged_button.pack(side="left")

        # Do you have advantage? Yes / No
        advantage_var = tk.BooleanVar()
        advantage_label = tk.Label(sneak_menu, text="Do you have advantage?")
        advantage_label.pack(pady=10)
        yes_advantaged_button = tk.Button(sneak_menu, text="Yes", command=lambda: combined_functions(
            [lambda: depress_button(yes_advantaged_button, [no_advantaged_button]), lambda: advantage_var.set(True)]))
        no_advantaged_button = tk.Button(sneak_menu, text="No", command=lambda: combined_functions(
            [lambda: depress_button(no_advantaged_button, [yes_advantaged_button]), lambda: advantage_var.set(False)]))
        yes_advantaged_button.pack(side="left")
        no_advantaged_button.pack(side="left")

        # Are you and another enemy of the target flanking the target? Yes / No
        self.flanking = tk.BooleanVar()
        flanking_label = tk.Label(sneak_menu, text="Are you and another enemy of the target flanking the target?")
        flanking_label.pack(pady=10)
        yes_flanking_button = tk.Button(sneak_menu, text="Yes", command=lambda: combined_functions(
            [lambda: depress_button(yes_flanking_button, [no_flanking_button]), lambda: self.flanking.set(True)]))
        no_flanking_button = tk.Button(sneak_menu, text="No", command=lambda: combined_functions(
            [lambda: depress_button(no_flanking_button, [yes_flanking_button]), lambda: self.flanking.set(False)]))
        yes_flanking_button.pack(side="left")
        no_flanking_button.pack(side="left")

        def display_sneak_result():
            print(self.get_sneak_eligibility())

        evaluate_button = tk.Button(sneak_menu, text="Evaluate", command=display_sneak_result)
        evaluate_button.pack()

    def get_sneak_eligibility(self):
        finesse_or_ranged = stats_and_mods.weapons_stats[self.weapon]["type"] in ["finesse", "ranged"]
        return (not self.disadvantage.get()) and finesse_or_ranged and (self.advantage.get() or self.flanking.get())
