import json
import tkinter as tk
import random

import stats_and_mods
from display_helpers import display_roll_result_generic, toggle_active_disabled


class InitiativeRoller:

    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = tk.Toplevel(main_menu.window)
        self.advantage = tk.BooleanVar()
        self.disadvantage = tk.BooleanVar()

    def display_menu(self):
        self.window.title("Roll initiative...")
        self.window.geometry("300x200")

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
            command=self.roll_initiative
        )

        # TODO: add advantage option here (use checkbox). this will update the class var above from None to whatever

        advantage_checkbutton.grid(row=0, column=0, padx=100, pady=10, sticky="w")
        disadvantage_checkbutton.grid(row=1, column=0, padx=100, pady=10, sticky="w")
        roll_button.grid(row=2, sticky="nsew", pady=10, padx=100)

    def roll_initiative(self):
        num_rolls = 2 if self.advantage else 1
        rolls = []
        for i in range(0, num_rolls):
            rolls.append(random.randint(1, 20))
        dex_mod = stats_and_mods.char_stats["dexterity"]
        roll_result = max(rolls) + dex_mod
        full_result = {"result": roll_result, "rolls": rolls, "dex modifier": dex_mod}
        self.main_menu.roll_history.append(full_result)
        display_roll_result_generic("Initiative", full_result, self.main_menu.output_box)
        self.window.destroy()
