import tkinter as tk

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

def release_button(self, button, other_buttons=None):
    button.configure(bg="light gray")
    button.configure("relief")[-1] == "raised"
    # if other_buttons:
    #     for b in other_buttons:
    #         b.configure(bg="original_color")



