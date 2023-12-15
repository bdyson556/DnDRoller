import tkinter as tk
import random
from tkinter import messagebox

import stats_and_mods
from display_helpers import toggle_active_disabled, display_roll_result_generic


class HitRoller:

    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = tk.Toplevel(main_menu.window)
        self.advantage = tk.BooleanVar()
        self.disadvantage = tk.BooleanVar()
        self.weapon = None

    def display_menu(self):
        # TODO: implement with weapon field and advantage, disadvantage checkboxes
        self.window.title("Roll to hit")
        self.window.geometry("550x300")

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
            text="Roll!",
            command= self.finish
        )

        weapon_label.grid(row=0, pady=10)
        weapon_dropdown.grid(row=1, column=0, padx=10, pady=15, sticky="w")
        advantage_checkbutton.grid(row=2, column=0, pady=10, sticky="w")
        disadvantage_checkbutton.grid(row=3, column=0, pady=10, sticky="w")
        roll_button.grid(row=4, column=0, pady=20, sticky="w")

    def finish(self):
        if self.weapon.get() == "None":
            messagebox.showinfo("", "Oops! Please select a weapon.", parent=self.window)
        else: self.roll_to_hit()

    def roll_to_hit(self):
        num_rolls = 2 if self.advantage.get() else 1
        weapon = self.weapon.get()
        # TODO: implement disadvantage logic
        rolls = []
        weapon_type = stats_and_mods.weapons_stats[weapon]["ability"]
        modifier = stats_and_mods.char_stats[weapon_type]
        proficiency_bonus = int(stats_and_mods.char_stats["proficiency bonus"]) if stats_and_mods.weapons_stats[weapon]["proficiency"] else 0
        # proficiency_bonus = 0
        for i in range(0, num_rolls):
            rolls.append(random.randint(1, 20))
        roll_result = max(rolls) + modifier + proficiency_bonus
        full_result = {"result": roll_result, "rolls": rolls, f"{weapon_type} modifier": modifier, "proficiency bonus": proficiency_bonus}

        display_roll_result_generic(
            "Roll to hit",
            full_result,
            self.main_menu.output_box
        )

        self.window.destroy()

