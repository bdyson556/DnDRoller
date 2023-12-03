from tkinter import messagebox

import roll
import stats_and_mods
from roll import Roller
from display_helpers import toggle_active_disabled, autocheck_checkboxes, depress_button, \
    release_button, display_skill_roll_result, display_roll_result_generic
from rolltohitmenu import RollToHitMenu
from skill_check_menu import Skill_Check_Menu
from initiative_menu import Initiative_Menu
from roll_for_damage_menu import RollForDamageMenu

# TODO: main menu: display stats, check (leads to menu or dropdown menu to select skill)
# TODO: display stats

import tkinter as tk


class Menu:
    roller = Roller()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Main Menu")
        self.window.geometry("450x350")

        self.skill_check_button = tk.Button(
            self.window,
            text="Skill Check",
            command=self.run_skill_check
        )

        self.skill_check_button.pack()

        # self.roll_initiative_button = tk.Button(self.window, text="Roll Initiative", command=self.display_roll_initiative_menu)
        self.roll_initiative_button = tk.Button(self.window, text="Roll Initiative", command=self.run_initiative)
        self.roll_initiative_button.pack()

        self.roll_to_hit_button = tk.Button(self.window, text="Roll to Hit", command=self.run_roll_to_hit)
        self.roll_to_hit_button.pack()

        self.roll_for_damage_button = tk.Button(self.window, text="Roll for Damage", command=self.run_roll_for_damage)
        self.roll_for_damage_button.pack()

        self.update_character_stats_button = tk.Button(self.window, text="Character Stats...",
                                                       command=self.character_stats_menu)
        self.update_character_stats_button.pack()

        self.current_roll_result = None

        self.output_box = tk.Text(self.window, width=40, height=15)
        self.output_box.pack()
        # self.output_box.grid(row=1, sticky="e")

    # EXAMPLES OF "GRID()"
    # skill_box_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")
    # skill_dropdown.grid(row=1, column=0, padx=10)
    # advantage_checkbutton.grid(row=2, column=0, padx=15, pady=10, sticky="w")
    # disadvantage_checkbutton.grid(row=3, column=0, padx=15, pady=5, sticky="w")
    # guidance_checkbutton.grid(row=4, column=0, padx=15, pady=5, sticky="w")
    # roll_button.grid(row=5, column=0, padx=15, pady=20, sticky="w")
    # output_box.grid(row=0, rowspan=6, column=1, padx=50)

    def main_menu(self):
        self.window.mainloop()

    def get_selected_skill(self, skill_var):
        selected_skill = skill_var.get()
        print(selected_skill)

    # def sneak_eligibility_menu(self, weapon):

    def character_stats_menu(self):
        print("Update Character Stats button clicked")

    def show_roll_history(self):
        print("Roll history button clicked")
        # roll_initiative_menu = tk.Toplevel(self.window)
        # roll_initiative_menu.title("Skill Check")
        # roll_initiative_menu.geometry("550x300")
        #
        # roll_button = tk.Button(
        #     roll_initiative_menu,
        #     text="Roll!",
        #     command=lambda: self.display_roll_result(roll_initiative_menu, lambda: roll_initiative(advantage=False))
        # )
        # roll_button.pack(pady=20)

    def combined_functions(self, func_list):
        for f in func_list: f()

    def run_skill_check(self):
        scm = Skill_Check_Menu()
        scm.display(self)

    def run_initiative(self):
        im = Initiative_Menu(self)
        im.display()

    def run_roll_to_hit(self):
        rthm = RollToHitMenu(self)
        rthm.display()

    def run_roll_for_damage(self):
        rfdm = RollForDamageMenu(self)
        rfdm.display()


