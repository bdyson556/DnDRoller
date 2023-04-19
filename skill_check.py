import tkinter as tk
from gui_helpers import toggle_active_disabled, autocheck_checkboxes
from roll import roll_skill

class Skill_Check_Menu:
    
    SKILLS = ["Acrobatics (Dex)", "Animal Handling (Wis)", "Arcana (Int)", "Athletics (Str)", "Deception (Cha)", "History (Int)", "Insight (Wis)", "Intimidation (Cha)", "Investigation (Int)", "Medicine (Wis)", "Nature (Int)", "Perception (Wis)", "Performance (Cha)", "Persuasion (Cha)", "Religion (Int)", "Sleight of Hand (Dex)", "Stealth (Dex)", "Survival (Wis)", "Thieves' Tools (Dex)"]

    def __init__(self, window):
        self.window = window
        self.menu = tk.Toplevel(self.window)
        self.window.title("Skill Check")
        self.menu.geometry("550x300")
        self.skill_box_label = tk.Label(self.menu, text="Enter skill to check:")
        self.skill_var = tk.StringVar()
        self.skill_var.set("None")
        self.dropdown_var = tk.StringVar(value='')
        self.roll_button = tk.Button(
            self.menu,
            text="Roll!",
            command=lambda: self.display_roll_result(
                self.menu, lambda: roll_skill(
                    20,
                    self.skill_var.get().lower(),
                    advantage=self.advantage_var.get(),
                    disadvantage=self.disadvantage_var.get(),
                    guidance=self.guidance_var.get()
                )
            )
        )
        self.skill_dropdown = tk.OptionMenu(
            self.menu,
            self.skill_var,
            *self.SKILLS,
            command=toggle_active_disabled(self.dropdown_var, [self.roll_button])
        )
        self.advantage_var = tk.BooleanVar()
        self.advantage_checkbutton = tk.Checkbutton(
            self.menu,
            text="Advantage",
            variable=self.advantage_var,
            command=lambda: toggle_active_disabled(
                self.advantage_var,
                [self.disadvantage_checkbutton]
            )
        )
        self.disadvantage_var = tk.BooleanVar()
        self.disadvantage_checkbutton = tk.Checkbutton(
            self.menu,
            text="Disadvantage",
            variable=self.disadvantage_var,
            command=lambda: toggle_active_disabled(
                self.disadvantage_var, [self.advantage_checkbutton])
        )
        self.guidance_var = tk.BooleanVar()
        self.guidance_checkbutton = tk.Checkbutton(self.menu, text="Guidance", variable=self.guidance_var)

        # TODO add num select widget to add custom modifier

    def display(self):
        print("clicked!")
        self.skill_box_label.pack(pady=10)
        self.skill_dropdown.pack()
        self.advantage_checkbutton.pack(pady=10)
        self.disadvantage_checkbutton.pack()
        self.guidance_checkbutton.pack()
        self.roll_button.pack(pady=20)


        
