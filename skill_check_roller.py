import tkinter as tk
from tkinter import messagebox

import stats_and_mods
from display_helpers import toggle_active_disabled, display_skill_roll_result
import random


class SkillCheckRoller:
    SKILLS = ["Acrobatics (Dex)", "Animal Handling (Wis)", "Arcana (Int)", "Athletics (Str)", "Deception (Cha)",
              "History (Int)", "Insight (Wis)", "Intimidation (Cha)", "Investigation (Int)", "Medicine (Wis)",
              "Nature (Int)", "Perception (Wis)", "Performance (Cha)", "Persuasion (Cha)", "Religion (Int)",
              "Sleight of Hand (Dex)", "Stealth (Dex)", "Survival (Wis)", "Thieves' Tools (Dex)"]

    def __init__(self):
        self.skill = tk.StringVar()
        self.skill.set("None")
        self.dropdown_var = tk.StringVar(value='')
        self.advantage = tk.BooleanVar()
        self.disadvantage = tk.BooleanVar()
        self.guidance = tk.BooleanVar()
        self.window = None
        # TODO add num select widget to add custom modifier

    def display_menu(self, main_menu_instance):
        self.window = tk.Toplevel(main_menu_instance.window)
        main_menu_instance.window.title("Skill Check")
        main_menu_instance.window.title("Skill Check")
        self.window.geometry("550x300")
        skill_box_label = tk.Label(self.window, text="Enter skill to check:")

        skill_dropdown = tk.OptionMenu(
            self.window,
            self.skill,
            *self.SKILLS,
        )
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

        guidance_checkbutton = tk.Checkbutton(self.window, text="Guidance", variable=self.guidance)
        roll_button = tk.Button(
            self.window,
            text="Roll!",
            command=lambda: self.finish(main_menu_instance)
        )

        skill_box_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")
        skill_dropdown.grid(row=1, column=0, padx=10)
        advantage_checkbutton.grid(row=2, column=0, padx=15, pady=10, sticky="w")
        disadvantage_checkbutton.grid(row=3, column=0, padx=15, pady=5, sticky="w")
        guidance_checkbutton.grid(row=4, column=0, padx=15, pady=5, sticky="w")
        roll_button.grid(row=5, column=0, padx=15, pady=20, sticky="w")

    def roll(self, main_menu_instance):
        roll_result = self.roll_skill(
            20,
            self.skill.get().lower()
        )
        main_menu_instance.roll_history.append(roll_result)
        display_skill_roll_result(
            self.skill.get(),
            roll_result,
            main_menu_instance.output_box
        )
        self.window.destroy()

    def finish(self, main_menu_instance):
        if self.skill.get() == "None":
            messagebox.showinfo("", "Oops! Please select a skill.", parent=self.window)
        else: self.roll(main_menu_instance)

    def roll_skill(self, die_size, skill):
        num_rolls = 1
        is_adv = self.advantage.get()
        is_disadv = self.disadvantage.get()
        condition = {}
        if is_adv or is_disadv:
            num_rolls = 2
            if is_adv: condition["condition"] = "advantaged"
            else: condition["condition"] = "disadvantaged"
        rolls = []
        roll_min = 0 if die_size == 100 else 1
        for i in range(0, num_rolls):
            rolls.append(random.randint(roll_min, die_size))
        proficiency = stats_and_mods.char_stats[skill]["proficient"]
        modifier = stats_and_mods.char_stats[skill]["modifier"]
        guidance_roll = random.randint(1, 4) if self.guidance.get() else 0
        selected_roll = min(rolls) if is_disadv else max(rolls)
        result = selected_roll + modifier + guidance_roll
        full_result = {"skill": skill, "result": result, "rolls": rolls, "proficiency": proficiency, "modifier": modifier, "guidance": guidance_roll}
        full_result.update(condition)
        return full_result

