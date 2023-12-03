import tkinter as tk

import roll
from display_helpers import toggle_active_disabled, display_skill_roll_result, display_roll_result_generic


class Initiative_Menu:
    def display(self, main_menu_instance):
        roll_initiative_menu = tk.Toplevel(self.window)
        roll_initiative_menu.title("Roll initiative...")
        roll_initiative_menu.geometry("300x200")

        output_box = tk.Text(roll_initiative_menu, width=15, height=4)
        roll_button = tk.Button(
            roll_initiative_menu,
            text="Roll!",
            command=lambda: self.roll_initiative(roll_initiative_menu)
        )

        roll_button.grid(row=0, sticky="nsew", pady=10, padx=100)
        output_box.grid(row=1, sticky="nsew", pady=20, padx=15)

        roll_initiative_menu.grid_rowconfigure(0, weight=0)
        roll_initiative_menu.grid_rowconfigure(1, weight=3)
        roll_initiative_menu.grid_columnconfigure(0, weight=1)

    def roll_initiative(self, roll_initiative_menu):

        roll_result = roll.roll_initiative(advantage=False)  # TODO: add advantage option here (use checkbox)
        self.roller.roll_history.append(roll_result)
        display_roll_result_generic("Initiative", roll_result, self.output_box)
        roll_initiative_menu.destroy()