import tkinter as tk
import json

def autocheck_checkboxes(actor_checkbox_state, object_checkboxes):
    for obj in object_checkboxes:
        if actor_checkbox_state.get():
            obj.configure(state="disabled", fg="gray")
            if isinstance(obj, tk.Checkbutton):
                obj.select()
        else:
            obj.configure(state="normal", fg="black")
            if isinstance(obj, tk.Checkbutton):
                obj.deselect()

def toggle_active_disabled(actor_button_state, object_buttons: list):
    if actor_button_state.get() == True:
        for obj in object_buttons:
            obj.configure(state="disabled", fg="gray")
    else:
        for obj in object_buttons:
            obj.configure(state="normal", fg="black")
            if isinstance(obj, tk.Checkbutton):
                obj.deselect()

# def toggle_active_disabled(actor_button_state, object_button):
#     if actor_button_state.get():
#         object_button.configure(state="disabled", fg="gray")
#     else:
#         object_button.configure(state="normal", fg="black")
#         if isinstance(object_button, tk.Checkbutton):
#             object_button.deselect()

def depress_button(self, button):
    button.configure(bg="green")
    button.configure("relief")[-1] == "sunken"

def release_button(self, button):
    button.configure(bg="light gray")
    button.configure("relief")[-1] == "raised"

def display_skill_roll_result(roll_type, roll_result, box):
    print(roll_result)
    text_output = roll_type + "\n" \
                  + f"\tRoll result: {str(roll_result.get('result'))}\t\trolls: {str(roll_result.get('rolls'))}\n" \
                  + f"\tAbility modifier: +{str(roll_result.get('modifier'))}\n" \
                  + f"\tProficient: {str(roll_result.get('proficiency'))}\n" \
                  + f"\tGuidance: +{str(roll_result.get('guidance'))}\n"
    try:
        text_output += f"\tCondition: {roll_result['condition']}"
    except: pass
    text_output += "\n\n"
    box.insert(tk.END, text_output)
    box.see("end")


def display_roll_result_generic(roll_type, roll_result, box):
    text_output = "\n" + str(roll_type)
    # del roll_result["result"]
    for key in roll_result:
        text_output += "\n\t" + key + ": " + str(roll_result[key])
    text_output += "\n"
    box.insert(tk.END, text_output)
    box.see("end")
