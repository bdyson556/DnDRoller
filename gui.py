from tkinter import messagebox

import roll
import stats_and_mods
from roll import Roller, roll_skill, roll_initiative, roll_damage, roll_to_hit
from gui_helpers import toggle_active_disabled, autocheck_checkboxes, depress_button, \
    release_button, display_roll_result
import skill_check

# TODO: main menu: display stats, check (leads to menu or dropdown menu to select skill)
# TODO: display stats

import tkinter as tk

class Menu:

    roller = Roller()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Main Menu")
        self.window.geometry("450x350")

        self.skill_check_menu = skill_check.Skill_Check_Menu()
        # self.roll_menu = roll.Roll_Menu()
        # etc...

        self.skill_check_button = tk.Button(
            self.window,
            text="Skill Check",
            command=lambda: self.skill_check_menu.display(self.window, self.roller)  # TODO: remove lambda if no params?
        )

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

    def main_menu(self):
        self.window.mainloop()

    def get_selected_skill(self, skill_var):
        selected_skill = skill_var.get()
        print(selected_skill)

    def roll_initiative_menu(self):
        print("Roll Initiative button clicked")
        roll_initiative_menu = tk.Toplevel(self.window)
        roll_initiative_menu.title("Skill Check")
        roll_initiative_menu.geometry("550x300")

        roll_button = tk.Button(
            roll_initiative_menu,
            text="Roll!",
            command = lambda: display_roll_result(roll_initiative_menu, lambda: roll_initiative(advantage=False), self.roller)
        )
        roll_button.grid(pady=20)   # changed from pack to grid


    def roll_to_hit_menu(self):
        # TODO: implement with weapon field and advantage, disadvantage checkboxes
        roll_to_hit_menu = tk.Toplevel(self.window)
        roll_to_hit_menu.title("Roll to hit")
        roll_to_hit_menu.geometry("550x300")

        weapon_label = tk.Label(roll_to_hit_menu, text="Enter weapon used:")
        weapon = tk.StringVar(value="None")
        weapon.set("None")
        weapon_dropdown = tk.OptionMenu(roll_to_hit_menu, weapon, *stats_and_mods.weapons_stats.keys())

        advantage_var = tk.BooleanVar()
        advantage_checkbutton = tk.Checkbutton(
            roll_to_hit_menu,
            text="Advantage",
            variable=advantage_var,
            command=lambda: toggle_active_disabled(advantage_var, [disadvantage_checkbutton])
        )

        disadvantage_var = tk.BooleanVar()
        disadvantage_checkbutton = tk.Checkbutton(
            roll_to_hit_menu,
            text="Disadvantage",
            variable=disadvantage_var,
            command=lambda: toggle_active_disabled(disadvantage_var, [advantage_checkbutton])
        )

        output_box = tk.Text(roll_to_hit_menu, width=40, height=15)
        try:
            roll_button = tk.Button(
                roll_to_hit_menu,
                text="Roll!",
                command = lambda: display_roll_result(
                    output_box,
                    lambda: roll_to_hit(
                        weapon.get(),
                        advantage=advantage_var.get(),
                        disadvantage=disadvantage_var.get()
                    ),
                    self.roller
                )
            )
        except KeyError as e: # TODO test this out
            messagebox.showerror("Error", "Please enter a valid skill name.")

        weapon_label.grid(row=0, pady=10)
        weapon_dropdown.grid(row=1, column=0, padx=10, pady=15, sticky="w")
        advantage_checkbutton.grid(row=2, column=0, pady=10, sticky="w")
        disadvantage_checkbutton.grid(row=3, column=0, pady=10, sticky="w")
        roll_button.grid(row=4, column=0, pady=20, sticky="w")
        output_box.grid(row=0, rowspan=6, column=1)

    def roll_for_damage_menu(self):
        roll_for_damage_menu = tk.Toplevel(self.window)
        roll_for_damage_menu.title("Roll for damage")
        roll_for_damage_menu.geometry("550x300")

        weapon_label = tk.Label(roll_for_damage_menu, text="Enter weapon used:")
        weapon = tk.StringVar(value="None")
        weapon.set("None")
        weapon_dropdown = tk.OptionMenu(roll_for_damage_menu, weapon, *stats_and_mods.weapons_stats.keys())

        advantage_var = tk.BooleanVar()
        advantage_checkbutton = tk.Checkbutton(
            roll_for_damage_menu,
            text="Advantage",
            variable=advantage_var,
            command=lambda: toggle_active_disabled(
                advantage_var,
                [disadvantage_checkbutton]
            )
        )

        sneak_var = tk.BooleanVar()
        sneak_checkbutton = tk.Checkbutton(
            roll_for_damage_menu,
            text="Sneak",
            variable=sneak_var,
            command=lambda: self.combined_functions([
                lambda: autocheck_checkboxes(
                    sneak_var,
                    [advantage_checkbutton]
                ),
                lambda: toggle_active_disabled(
                    sneak_var,
                    [disadvantage_checkbutton]
                )
            ])
        )

        disadvantage_var = tk.BooleanVar()
        disadvantage_checkbutton = tk.Checkbutton(
            roll_for_damage_menu,
            text="Disadvantage",
            variable=disadvantage_var,
            command=lambda: toggle_active_disabled(disadvantage_var, [advantage_checkbutton, sneak_checkbutton])
        )

        output_box = tk.Text(roll_for_damage_menu, width=40, height=15)
        roll_button = tk.Button(roll_for_damage_menu,
                                text="Roll!",
                                command = lambda: self.combined_functions([lambda: display_roll_result(
                                    output_box,
                                    lambda: roll_damage(
                                        weapon.get(),
                                        advantage=advantage_var.get(),
                                        disadvantage=disadvantage_var.get(),
                                        sneak=sneak_var.get()
                                        ),
                                    self.roller
                                ), lambda: print(f"disadvantage_var: {disadvantage_var.get()}, advantage_var: {advantage_var.get()}, snear_var: {sneak_var.get()}")]) # TODO:   .............  /????
        )

        weapon_dropdown.grid()
        advantage_checkbutton.grid()
        disadvantage_checkbutton.grid()
        roll_button.grid()

        weapon_label.grid(row=0, pady=10)
        weapon_dropdown.grid(row=1, column=0, padx=15)
        advantage_checkbutton.grid(row=2, column=0, padx=15, pady=10, sticky="w")
        sneak_checkbutton.grid(row=3, column=0, padx=15, pady=10, sticky="w")
        disadvantage_checkbutton.grid(row=4, column=0, padx=15, pady=10, sticky="w")
        roll_button.grid(row=5, column=0)
        output_box.grid(row=0, rowspan=6, column=1, padx=15)

        # Can I sneak attack? Opens new menu to check conditions.
        sneak_eligibility_label = tk.Label(roll_for_damage_menu, text="Can I sneak attack?", cursor="hand2", fg="blue")
        sneak_eligibility_label.bind("<Button-1>", self.sneak_eligibility_menu)
        sneak_eligibility_label.place(relx=0.22, rely=0.9, anchor="e", bordermode="outside")


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


