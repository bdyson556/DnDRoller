import random
import tkinter as tk
from tkinter import messagebox

import roll
import stats_and_mods
from roll import roll_damage, roll_to_hit, roll_skill, roll_initiative
from gui_helpers import toggle_active_disabled, autocheck_checkboxes, depress_button, \
    release_button

# TODO: main menu: display stats, check (leads to menu or dropdown menu to select skill)
# TODO: display stats

import tkinter as tk

class Menu:

    SKILLS = ["Acrobatics (Dex)", "Animal Handling (Wis)", "Arcana (Int)", "Athletics (Str)", "Deception (Cha)", "History (Int)", "Insight (Wis)", "Intimidation (Cha)", "Investigation (Int)", "Medicine (Wis)", "Nature (Int)", "Perception (Wis)", "Performance (Cha)", "Persuasion (Cha)", "Religion (Int)", "Sleight of Hand (Dex)", "Stealth (Dex)", "Survival (Wis)"]

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Main Menu")
        self.window.geometry("450x350")

        self.skill_check_button = tk.Button(self.window, text="Skill Check", command=self.skill_check_menu)
        # self.skill_check_button = tk.Button(self.window, text="Skill Check", command=self.show_option1_menu)
        self.skill_check_button.pack()

        self.roll_initiative_button = tk.Button(self.window, text="Roll Initiative", command=self.roll_initiative_menu)
        self.roll_initiative_button.pack()

        self.roll_to_hit_button = tk.Button(self.window, text="Roll to Hit", command=self.roll_to_hit_menu)
        self.roll_to_hit_button.pack()

        self.roll_for_damage_button = tk.Button(self.window, text="Roll for Damage", command=self.roll_for_damage_menu)
        self.roll_for_damage_button.pack()

        self.update_character_stats_button = tk.Button(self.window, text="Character Stats...",
                                                       command=self.character_stats_menu)
        self.update_character_stats_button.pack()

        self.current_roll_result = None
        self.roll_history = []


    def main_menu(self):
        self.window.mainloop()


    def show_option1_menu(self):
        option1_menu = tk.Toplevel(self.window)
        option1_menu.title("Option 1 Menu")
        option1_menu.geometry("200x100")

        yes_button = tk.Button(option1_menu, text="Yes")
        yes_button.pack(pady=10)

        no_button = tk.Button(option1_menu, text="No")
        no_button.pack(pady=10)


    def get_selected_skill(self, skill_var):
        selected_skill = skill_var.get()
        print(selected_skill)


    def skill_check_menu(self):
        print("Skill Check button clicked")
        skill_check_menu = tk.Toplevel(self.window)
        skill_check_menu.title("Skill Check")
        skill_check_menu.geometry("550x300")

        skill_box_label = tk.Label(skill_check_menu, text="Enter skill to check:")
        skill_box_label.pack(pady=10)
        # skill_entry = tk.Entry(skill_check_menu)
        # skill_entry.pack()
        skill_var = tk.StringVar()
        skill_var.set("None")
        skill_dropdown = tk.OptionMenu(skill_check_menu, skill_var, self.SKILLS)
        skill_dropdown.pack()
        # check_button = tk.Button(skill_check_menu, text = "Check Skill", command=self.get_selected_skill(skill_var))

        advantage_var = tk.BooleanVar()
        advantage_checkbutton = tk.Checkbutton(skill_check_menu, text="Advantage", variable=advantage_var)
        advantage_checkbutton.pack(pady=10)

        disadvantage_var = tk.BooleanVar()
        disadvantage_checkbutton = tk.Checkbutton(skill_check_menu, text="Disadvantage", variable=disadvantage_var)
        disadvantage_checkbutton.pack()

        guidance_var = tk.BooleanVar()
        guidance_checkbutton = tk.Checkbutton(skill_check_menu, text="Guidance", variable=guidance_var)
        guidance_checkbutton.pack()

        # TODO add num select widget to add custom modifier

        try:
            roll_button = tk.Button(skill_check_menu,
                                    text="Roll!",
                                    command = lambda: self.display_roll_result(skill_check_menu, lambda: roll_skill(20, skill_var.get().split(" ")[0].lower(), advantage=advantage_var.get(),
                                                       disadvantage=disadvantage_var.get(),
                                                       guidance=guidance_var.get()
                                                       ))
                                    )
            roll_button.pack(pady=20)
        except KeyError as e: # TODO test this out
            messagebox.showerror("Error", "Please enter a valid skill name.")

    def display_roll_result(self, menu, func):
        result = func()
        self.current_roll_result = result
        self.roll_history.append(result)
        print(result)
        result_label = tk.Label(menu, text=self.current_roll_result)
        result_label.pack()

    def roll_initiative_menu(self):
        print("Roll Initiative button clicked")
        roll_initiative_menu = tk.Toplevel(self.window)
        roll_initiative_menu.title("Skill Check")
        roll_initiative_menu.geometry("550x300")

        roll_button = tk.Button(
            roll_initiative_menu,
            text="Roll!",
            command = lambda: self.display_roll_result(roll_initiative_menu, lambda: roll_initiative(advantage=False))
        )
        roll_button.pack(pady=20)


    def roll_to_hit_menu(self):
        # TODO: implement with weapon field and advantage, disadvantage checkboxes
        roll_to_hit_menu = tk.Toplevel(self.window)
        roll_to_hit_menu.title("Roll to hit")
        roll_to_hit_menu.geometry("550x300")

        weapon_label = tk.Label(roll_to_hit_menu, text="Enter weapon used:")
        weapon_label.pack(pady=10)

        weapon_entry = tk.Entry(roll_to_hit_menu)
        weapon_entry.pack()

        advantage_var = tk.BooleanVar()
        advantage_checkbutton = tk.Checkbutton(roll_to_hit_menu, text="Advantage", variable=advantage_var)
        advantage_checkbutton.pack(pady=10)

        disadvantage_var = tk.BooleanVar()
        disadvantage_checkbutton = tk.Checkbutton(roll_to_hit_menu, text="Disadvantage", variable=disadvantage_var)
        disadvantage_checkbutton.pack()

        try:
            roll_button = tk.Button(roll_to_hit_menu,
                                    text="Roll!",
                                    command = lambda: self.display_roll_result(roll_to_hit_menu, lambda: roll_to_hit(weapon_entry.get(), advantage=advantage_var.get(),
                                                       disadvantage=disadvantage_var.get()
                                                       ))
                                    )
            roll_button.pack(pady=20)
        except KeyError as e: # TODO test this out
            messagebox.showerror("Error", "Please enter a valid skill name.")


    def roll_for_damage_menu(self):
        roll_for_damage_menu = tk.Toplevel(self.window)
        roll_for_damage_menu.title("Roll for damage")
        roll_for_damage_menu.geometry("550x300")

        weapon_label = tk.Label(roll_for_damage_menu, text="Enter weapon used:")
        weapon_label.pack(pady=10)
        weapon = tk.StringVar(value="None")
        weapon.set("None")
        weapon_dropdown = tk.OptionMenu(roll_for_damage_menu, weapon, *stats_and_mods.weapons_stats.keys())
        weapon_dropdown.pack()

        advantage_var = tk.BooleanVar()
        advantage_checkbutton = tk.Checkbutton(roll_for_damage_menu,
                                               text="Advantage",
                                               variable=advantage_var,
                                               command=lambda: toggle_active_disabled(advantage_var, [disadvantage_checkbutton])
                                               )
        advantage_checkbutton.pack(pady=10)

        sneak_var = tk.BooleanVar()
        sneak_checkbutton = tk.Checkbutton(roll_for_damage_menu,
                                           text="Sneak",
                                           variable=sneak_var,
                                           command=lambda: self.combined_functions([lambda: autocheck_checkboxes(sneak_var, [advantage_checkbutton]),
                                                                                    lambda: toggle_active_disabled(sneak_var, [disadvantage_checkbutton])
                                                                                    ])
                                           )
        sneak_checkbutton.pack()

        # Can I sneak attack? Opens new menu to check conditions.
        sneak_eligibility_label = tk.Label(roll_for_damage_menu, text="Can I sneak attack?", cursor="hand2", fg="blue")
        sneak_eligibility_label.bind("<Button-1>", self.sneak_eligibility_menu)
        sneak_eligibility_label.place(relx=0.9, rely=0.39, anchor="e", bordermode="outside")

        disadvantage_var = tk.BooleanVar()
        disadvantage_checkbutton = tk.Checkbutton(roll_for_damage_menu,
                                                  text="Disadvantage",
                                                  variable=disadvantage_var,
                                                  command=lambda: self.combined_functions(
                                                      [lambda: toggle_active_disabled(disadvantage_var, [advantage_checkbutton, sneak_checkbutton])]
                                                      # lambda: toggle_active_disabled(disadvantage_var, sneak_checkbutton)]
                                                  ))
        disadvantage_checkbutton.pack()

        try:
            roll_button = tk.Button(roll_for_damage_menu,
                                    text="Roll!",
                                    command = lambda: self.combined_functions([lambda: self.display_roll_result(
                                        roll_for_damage_menu,
                                        lambda: roll_damage(
                                            weapon.get(),
                                            advantage=advantage_var.get(),
                                            disadvantage=disadvantage_var.get(),
                                            sneak=sneak_var.get()
                                            )
                                    ), lambda: print(f"disadvantage_var: {disadvantage_var.get()}, advantage_var: {advantage_var.get()}, snear_var: {sneak_var.get()}")]) # TODO:   .............  /????
            )
            roll_button.pack(pady=20)
        except KeyError as e: # TODO test this out
            messagebox.showerror("Error", "Please enter a valid skill name.")


    # def sneak_eligibility_menu(self, weapon):
    def sneak_eligibility_menu(self, empty):
        sneak_menu = tk.Toplevel(self.window)
        sneak_menu.title("Can I sneak attack?")
        sneak_menu.geometry("550x300")

        weapon_label = tk.Label(sneak_menu, text="Enter weapon used:")
        weapon_label.pack(pady=10)
        weapon = tk.StringVar(value="None")
        weapon.set("None")
        weapon_dropdown = tk.OptionMenu(sneak_menu, weapon, *stats_and_mods.weapons_stats.keys())
        weapon_dropdown.pack()

        # Are you disadvantaged? Yes / No
        disadvantage_var = tk.BooleanVar()
        disadvantage_label = tk.Label(sneak_menu, text="Are you disadvantaged?")
        disadvantage_label.pack(pady=10)
        yes_disadvantaged_button = tk.Button(sneak_menu, text="Yes", command=lambda: self.combined_functions(
            # [lambda: depress_button(yes_disadvantaged_button[1], [no_disadvantaged_button]),
            [lambda: disadvantage_var.set(True),
            lambda: depress_button(empty, yes_disadvantaged_button),
            lambda: release_button(empty, no_disadvantaged_button),
            lambda: toggle_active_disabled(disadvantage_var, [yes_advantaged_button, no_advantaged_button])]
            # lambda: autodisable_checkbox(disadvantage_var, no_advantaged_button)]
        ))

        no_disadvantaged_button = tk.Button(sneak_menu, text="No", command=lambda: self.combined_functions(
            [lambda: disadvantage_var.set(False),
            lambda: depress_button(empty, no_disadvantaged_button),
            release_button(empty, yes_disadvantaged_button),
            lambda: toggle_active_disabled(disadvantage_var, [yes_advantaged_button, no_advantaged_button])]
            # lambda: autodisable_checkbox(disadvantage_var, no_advantaged_button)]
        ))
        yes_disadvantaged_button.pack(side="left")
        no_disadvantaged_button.pack(side="left")

        # Do you have advantage? Yes / No
        advantage_var = tk.BooleanVar()
        advantage_label = tk.Label(sneak_menu, text="Do you have advantage?")
        advantage_label.pack(pady=10)
        yes_advantaged_button = tk.Button(sneak_menu, text="Yes", command=lambda: self.combined_functions([lambda: depress_button(yes_advantaged_button, [no_advantaged_button]), lambda: advantage_var.set(True)]))
        no_advantaged_button = tk.Button(sneak_menu, text="No", command=lambda: self.combined_functions([lambda: depress_button(no_advantaged_button, [yes_advantaged_button]), lambda: advantage_var.set(False)]))
        yes_advantaged_button.pack(side="left")
        no_advantaged_button.pack(side="left")

        # Are you and another enemy of the target flanking the target? Yes / No
        flanking_var = tk.BooleanVar()
        flanking_label = tk.Label(sneak_menu, text="Are you and another enemy of the target flanking the target?")
        flanking_label.pack(pady=10)
        yes_flanking_button = tk.Button(sneak_menu, text="Yes", command=lambda: self.combined_functions(
            [lambda: depress_button(yes_flanking_button, [no_flanking_button]), lambda: flanking_var.set(True)]))
        no_flanking_button = tk.Button(sneak_menu, text="No", command=lambda: self.combined_functions(
            [lambda: depress_button(no_flanking_button, [yes_flanking_button]), lambda: flanking_var.set(False)]))
        yes_flanking_button.pack(side="left")
        no_flanking_button.pack(side="left")

        def display_sneak_result():
            print(roll.get_sneak_eligibility(weapon, advantage=advantage_var, disadvantage=disadvantage_var, flanking=flanking_var))

        evaluate_button = tk.Button(sneak_menu, text="Evaluate", command=display_sneak_result)
        evaluate_button.pack()


    def character_stats_menu(self):
        print("Update Character Stats button clicked")


    def combined_functions(self, func_list):
        for f in func_list: f()


if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()