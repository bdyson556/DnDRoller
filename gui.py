import random
import tkinter as tk
from tkinter import messagebox
import stats_and_mods

# initialize dict with char's stats

def roll_die(die_size):
    if die_size == 100:
        return random.randint(0, die_size)
    else: return random.randint(1, die_size)

def roll_die_with_advantage(die_size):
    roll1 = roll_die(die_size)
    roll2 = roll_die(die_size)
    return {"roll1": roll1, "roll2": roll2, "max": max([roll1, roll2])}

def roll_initiative(advantage = None):
    if advantage:
        return roll_die_with_advantage(20)["max"] + stats_and_mods.DEX # TODO
    else:
        return roll_die(20) + stats_and_mods.DEX

def roll():
    print()

print(roll_die_with_advantage(20)[0])

exit()

# Define a list of options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create a new tkinter window
window = tk.Tk()
window.withdraw()  # hide the main window

# Create an OptionMenu widget with the list of options
var = tk.StringVar(window)
var.set(options[0])  # set the default option
option_menu = tk.OptionMenu(window, var, *options)
option_menu.pack()

# Display a message box with an OK button
messagebox.showinfo("Choose an Option", "Please choose an option.")

# Process the user's response
user_choice = var.get()
print(f"User chose option: {user_choice}")

# Close the window
window.destroy()
