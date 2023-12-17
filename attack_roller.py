import tkinter as tk
import random
from tkinter import messagebox

import helper_functions
import stats_and_mods
from display_helpers import toggle_active_disabled, display_roll_result_generic, depress_button, release_button


class AttackRoller:

    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = tk.Toplevel(main_menu.window)
        self.weapon = None
        self.advantage = tk.BooleanVar()
        self.disadvantage = tk.BooleanVar()
        self.flanking = tk.BooleanVar()
        self.sneak = tk.BooleanVar()
        self.critical = False

        self.output_box = tk.Text(self.window, width=40, height=15)
        self.output_box.grid(row=0, column=1, pady=30, rowspan=5)


    def display_menu(self):
        # TODO: implement with weapon field and advantage, disadvantage checkboxes
        self.window.title("Roll to hit")
        self.window.geometry("700x450")

        weapon_label = tk.Label(self.window, text="Enter weapon used:")
        self.weapon = tk.StringVar(value="None")
        self.weapon.set("None")
        weapon_dropdown = tk.OptionMenu(self.window, self.weapon, *stats_and_mods.weapons_stats.keys())
        # TODO: Maybe when selecting weapon from dropdown, assign JSON contents of weapon to dictionary? Then they can be accessed in roll_to_hit() and elsewhere. You might need to somehow add a lambda to the dropdown for this and create a method to handle the assignment.

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

        roll_button = tk.Button(
            self.window,
            text="Roll to attack!",
            command= self.finish
        )

        sneak_checkbutton = tk.Checkbutton(
            self.window,
            text="Sneak",
            variable=self.sneak,
            command=lambda: helper_functions.combined_functions([]))

        roll_damage_button = tk.Button(self.window, text="Roll for damage!", command=lambda: self.finish_damage())

        weapon_dropdown.grid()
        roll_button.grid()

        weapon_label.grid(row=0, pady=10)
        weapon_dropdown.grid(row=1, column=0, padx=100, pady=0, sticky="w")
        advantage_checkbutton.grid(row=2, column=0, padx=100, pady=10, sticky="w")
        disadvantage_checkbutton.grid(row=3, column=0, padx=100, pady=10, sticky="w")
        sneak_checkbutton.grid(row=4, column=0, padx=100, pady=10, sticky="w")
        roll_button.grid(row=5, column=0, padx=100)
        roll_damage_button.grid(row=6, column=0, padx=100, pady=20, sticky="w")

        # Can I sneak attack? Opens new menu to check conditions.
        sneak_eligibility_label = tk.Label(self.window, text="Can I sneak attack?", cursor="hand2", fg="blue")
        sneak_eligibility_label.bind("<Button-1>", self.sneak_eligibility_menu)
        sneak_eligibility_label.place(relx=0.5, rely=0.9, anchor="e", bordermode="outside")

    def finish(self):
        if self.weapon.get() == "None":
            messagebox.showinfo("", "Oops! Please select a weapon.", parent=self.window)
        else: self.roll_to_hit()

    def finish_damage(self):
        if self.weapon.get() == "None":
            messagebox.showinfo("", "Oops! Please select a weapon.", parent=self.window)
        else: self.roll_damage()

    def roll_to_hit(self):
        self.critical = False
        is_adv = self.advantage.get()
        is_disadv = self.disadvantage.get()
        condition = {}
        num_rolls = 1
        if is_adv or is_disadv:
            num_rolls = 2
            if is_adv: condition["condition"] = "advantaged"
            else: condition["condition"] = "disadvantaged"
        weapon = self.weapon.get()
        # TODO: implement disadvantage logic
        rolls = []
        weapon_type = stats_and_mods.weapons_stats[weapon]["ability"]
        modifier = stats_and_mods.char_stats[weapon_type]
        proficiency_bonus = int(stats_and_mods.char_stats["proficiency bonus"]) if stats_and_mods.weapons_stats[weapon]["proficiency"] else 0
        for i in range(0, num_rolls):
            rolls.append(random.randint(1, 20))
        selected_roll = min(rolls) if self.disadvantage.get() else max(rolls)
        roll_result = selected_roll + modifier + proficiency_bonus
        full_result = {"result": roll_result, "rolls": rolls, f"{weapon_type} modifier": modifier,
                       "proficiency bonus": proficiency_bonus}
        full_result.update(condition)
        if selected_roll == 20:
            self.critical = True
            full_result["Critical hit!"] = ""

        print(full_result)
        display_roll_result_generic(
            "Roll to hit",
            full_result,
            self.output_box
        )
        display_roll_result_generic(
            "Roll to hit",
            full_result,
            self.main_menu.output_box
        )

    def roll_damage(self):
        weapon = self.weapon.get()
        die = stats_and_mods.weapons_stats[weapon]["die"]
        num_base_rolls = stats_and_mods.weapons_stats[weapon]["num rolls"]
        attack_type = stats_and_mods.weapons_stats[weapon]["type"]
        # ability_mod = stats_and_mods.weapons[weapon][""]
        damage_ability = stats_and_mods.char_stats["damage ability"]
        ability_mod = stats_and_mods.char_stats[damage_ability]
        critical_mod = 0

        rolls = [random.randint(1, die) for i in range(0, num_base_rolls)]

        if self.sneak.get():
            num_sneak_rolls = stats_and_mods.char_stats["num sneak dice"]
            for i in range(0, num_sneak_rolls):
                rolls.append(random.randint(1, 6))
            critical_mod = 6 * num_sneak_rolls if self.critical else 0
        else:
            if self.critical: critical_mod = die

        roll_result = sum(rolls) + ability_mod + critical_mod
        full_result = {
            "result": roll_result,
            "rolls": f"{rolls} (= {sum(rolls)})",
            "sneak": self.sneak.get(),
            "critical mod": f"{critical_mod}",
            "ability modifier": f"{ability_mod} ({damage_ability})",
            "attack type": attack_type
        }

        display_roll_result_generic(
            # roll_type, roll_result, box
            "Damage roll",
            full_result,
            self.main_menu.output_box
        )

        self.window.destroy()

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
        yes_disadvantaged_button = tk.Button(sneak_menu, text="Yes", command=lambda: helper_functions.combined_functions(
            # [lambda: depress_button(yes_disadvantaged_button[1], [no_disadvantaged_button]),
            [lambda: disadvantage_var.set(True),
             lambda: depress_button(empty, yes_disadvantaged_button),
             lambda: release_button(empty, no_disadvantaged_button),
             lambda: toggle_active_disabled(disadvantage_var, [yes_advantaged_button, no_advantaged_button])]
        ))

        no_disadvantaged_button = tk.Button(sneak_menu, text="No", command=lambda: helper_functions.combined_functions(
            [lambda: disadvantage_var.set(False),
             lambda: depress_button(empty, no_disadvantaged_button),
             release_button(empty, yes_disadvantaged_button),
             lambda: toggle_active_disabled(disadvantage_var, [yes_advantaged_button, no_advantaged_button])]
        ))
        yes_disadvantaged_button.pack(side="left")
        no_disadvantaged_button.pack(side="left")

        # Do you have advantage? Yes / No
        advantage_var = tk.BooleanVar()
        advantage_label = tk.Label(sneak_menu, text="Do you have advantage?")
        advantage_label.pack(pady=10)
        yes_advantaged_button = tk.Button(sneak_menu, text="Yes", command=lambda: helper_functions.combined_functions(
            [lambda: depress_button(yes_advantaged_button, [no_advantaged_button]), lambda: advantage_var.set(True)]))
        no_advantaged_button = tk.Button(sneak_menu, text="No", command=lambda: helper_functions.combined_functions(
            [lambda: depress_button(no_advantaged_button, [yes_advantaged_button]), lambda: advantage_var.set(False)]))
        yes_advantaged_button.pack(side="left")
        no_advantaged_button.pack(side="left")

        # Are you and another enemy of the target flanking the target? Yes / No
        self.flanking = tk.BooleanVar()
        flanking_label = tk.Label(sneak_menu, text="Are you and another enemy of the target flanking the target?")
        flanking_label.pack(pady=10)
        yes_flanking_button = tk.Button(sneak_menu, text="Yes", command=lambda: helper_functions.combined_functions(
            [lambda: depress_button(yes_flanking_button, [no_flanking_button]), lambda: self.flanking.set(True)]))
        no_flanking_button = tk.Button(sneak_menu, text="No", command=lambda: helper_functions.combined_functions(
            [lambda: depress_button(no_flanking_button, [yes_flanking_button]), lambda: self.flanking.set(False)]))
        yes_flanking_button.pack(side="left")
        no_flanking_button.pack(side="left")

        def display_sneak_result():
            print(self.get_sneak_eligibility())

        evaluate_button = tk.Button(sneak_menu, text="Evaluate", command=display_sneak_result)
        evaluate_button.pack()

    def get_sneak_eligibility(self):
        finesse_or_ranged = stats_and_mods.weapons_stats[self.weapon]["type"] in ["finesse", "ranged"]
        return (not self.disadvantage.get()) and finesse_or_ranged and (self.advantage.get() or self.flanking.get())
