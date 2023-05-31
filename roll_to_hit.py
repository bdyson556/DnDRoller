import tkinter as tk
from tkinter import messagebox

import stats_and_mods
from gui_helpers import toggle_active_disabled, display_roll_result
from roll import roll_to_hit


class RollToHitMenu:
    def __init__(self):
        self.weapon = tk.StringVar(value="None")


def roll_to_hit_menu(self):
    # TODO: implement with weapon field and advantage, disadvantage checkboxes
    roll_to_hit_menu = tk.Toplevel(self.window)
    roll_to_hit_menu.title("Roll to hit")
    roll_to_hit_menu.geometry("550x300")

    weapon_label = tk.Label(roll_to_hit_menu, text="Enter weapon used:")
    weapon_label.pack(pady=10)
    weapon = tk.StringVar(value="None")
    # self.weapon.set("None")
    # weapon_dropdown = tk.OptionMenu(roll_to_hit_menu, self.weapon, *stats_and_mods.weapons_stats.keys())
    weapon_dropdown = tk.OptionMenu(roll_to_hit_menu, weapon, *stats_and_mods.weapons_stats.keys())
    weapon_dropdown.pack()

    advantage_var = tk.BooleanVar()
    advantage_checkbutton = tk.Checkbutton(
        roll_to_hit_menu,
        text="Advantage",
        variable=advantage_var,
        command=lambda: toggle_active_disabled(advantage_var, [disadvantage_checkbutton])
    )
    advantage_checkbutton.pack(pady=10)

    disadvantage_var = tk.BooleanVar()
    disadvantage_checkbutton = tk.Checkbutton(
        roll_to_hit_menu,
        text="Disadvantage",
        variable=disadvantage_var,
        command=lambda: toggle_active_disabled(disadvantage_var, [advantage_checkbutton])
    )
    disadvantage_checkbutton.pack(pady=10)

    try:
        roll_button = tk.Button(
            roll_to_hit_menu,
            text="Roll!",
            command=lambda: display_roll_result(
                roll_to_hit_menu,
                lambda: roll_to_hit(
                    weapon.get(),
                    advantage=advantage_var.get(),
                    disadvantage=disadvantage_var.get()
                ),
                self.roller
            )
        )
        roll_button.pack(pady=20)
    except KeyError as e:  # TODO test this out
        messagebox.showerror("Error", "Please enter a valid skill name.")