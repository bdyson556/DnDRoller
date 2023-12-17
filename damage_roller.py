import tkinter as tk
import random
from tkinter import messagebox

import helper_functions
import stats_and_mods
from display_helpers import toggle_active_disabled, autocheck_checkboxes, depress_button, \
    release_button, display_roll_result_generic
from helper_functions import combined_functions


class DamageRoller:
    def display_menu(self):
        self.window.title("Roll for damage")
        self.window.geometry("300x300")

        weapon_label = tk.Label(self.window, text="Enter weapon used:")
        self.weapon = tk.StringVar(value="None")
        self.weapon.set("None")
        weapon_dropdown = tk.OptionMenu(self.window, self.weapon, *stats_and_mods.weapons_stats.keys())

        weapon_label.grid(row=0, pady=10, padx=15)
        weapon_dropdown.grid(row=1, column=0, padx=30)



