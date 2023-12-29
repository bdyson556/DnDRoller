from tkinter import messagebox

from attack_roller import AttackRoller
from skill_check_roller import SkillCheckRoller
from initiative_roller import InitiativeRoller
from damage_roller import DamageRoller

# TODO: main menu: display stats, check (leads to menu or dropdown menu to select skill)
# TODO: display stats

import tkinter as tk


class Menu:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Main Menu")
        self.window.geometry("550x350")
        self.roll_history = []

        self.skill_check_button = tk.Button(
            self.window,
            text="Skill Check",
            command=self.run_skill_check
        )

        self.roll_initiative_button = tk.Button(self.window, text="Roll Initiative", command=self.run_initiative)

        self.roll_attack_button = tk.Button(self.window, text="Attack", command=self.run_attack)

        # self.roll_for_damage_button = tk.Button(self.window, text="Roll for Damage", command=self.run_roll_for_damage)
        # self.roll_for_damage_button.pack()

        self.update_character_stats_button = tk.Button(self.window, text="Character Stats...",
                                                       command=self.character_stats_menu)

        self.current_roll_result = None

        self.output_box = tk.Text(self.window, width=45, height=15)
        # self.output_box.grid(row=1, sticky="e")

        self.skill_check_button.grid(row=0, column=0, padx=15)
        self.roll_initiative_button.grid(row=1, column=0, padx=15)
        self.roll_attack_button.grid(row=2, column=0, padx=15)
        self.update_character_stats_button.grid(row=3, column=0, padx=15)
        self.output_box.grid(row=0, column=1, padx=25, rowspan=8)

    def main_menu(self):
        self.window.mainloop()

    def get_selected_skill(self, skill_var):
        selected_skill = skill_var.get()
        print(selected_skill)

    def character_stats_menu(self):
        messagebox.showinfo("Update Character Stats button clicked!")

    def show_roll_history(self):
        print("Roll history button clicked")

    # def combined_functions(self, func_list)
    #     for f in func_list: f()

    def run_skill_check(self):
        sc_menu = SkillCheckRoller()
        sc_menu.display_menu(self)

    def run_initiative(self):
        initiative_menu = InitiativeRoller(self)
        initiative_menu.display_menu()

    def run_attack(self):
        attack_menu = AttackRoller(self)
        attack_menu.display_menu()

    def run_roll_for_damage(self):      # TODO: remove?
        rfd_menu = DamageRoller(self)
        rfd_menu.display_menu()


