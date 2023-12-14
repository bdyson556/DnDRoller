import tkinter as tk
import random

import stats_and_mods
from display_helpers import display_roll_result_generic


class InitiativeRoller:

    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = tk.Toplevel(main_menu.window)
        self.advantage = None

    def display_menu(self):
        self.window.title("Roll initiative...")
        self.window.geometry("300x200")

        roll_button = tk.Button(
            self.window,
            text="Roll!",
            command=self.roll_initiative
        )

        # TODO: add advantage option here (use checkbox). this will update the class var above from None to whatever

        roll_button.grid(row=0, sticky="nsew", pady=10, padx=100)

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

    def display_roll_result(self, roll_result):
        print(roll_result)
        text_output = "\n\t" + json.dumps(roll_result) + "\n\n"
        box.insert(tk.END, text_output)
