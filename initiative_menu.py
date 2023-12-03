import tkinter as tk
import random

import roll
import stats_and_mods
from display_helpers import toggle_active_disabled, display_skill_roll_result, display_roll_result_generic


class Initiative_Menu:

    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = main_menu.window
        self.advantage = None


    def display(self):
        roll_initiative_menu = tk.Toplevel(self.window)
        roll_initiative_menu.title("Roll initiative...")
        roll_initiative_menu.geometry("300x200")

        roll_button = tk.Button(
            roll_initiative_menu,
            text="Roll!",
            command=lambda: self.roll_initiative(roll_initiative_menu, False) # TODO:
        )

        # TODO: add advantage option here (use checkbox). this will update the class var above from None to whatever

        roll_button.grid(row=0, sticky="nsew", pady=10, padx=100)

        roll_initiative_menu.grid_rowconfigure(0, weight=0)
        roll_initiative_menu.grid_rowconfigure(1, weight=3)
        roll_initiative_menu.grid_columnconfigure(0, weight=1)

    def roll_initiative(self, roll_initiative_menu, advantage):
        num_rolls = 2 if advantage else 1
        rolls = []
        for i in range(0, num_rolls):
            rolls.append(random.randint(1, 20))
        dex_mod = stats_and_mods.char_stats["dexterity"]
        roll_result = max(rolls) + dex_mod
        full_result = {"result": roll_result, "rolls": rolls, "dex modifier": dex_mod}
        self.main_menu.roller.roll_history.append(full_result)
        display_roll_result_generic("Initiative", full_result, self.main_menu.output_box)
        roll_initiative_menu.destroy()