import tkinter as tk

def autocheck_checkbox(actor_checkbox_state, object_checkbox):
    if actor_checkbox_state.get():
        object_checkbox.configure(state="disabled", fg="gray")
        if isinstance(object_checkbox, tk.Checkbutton):
            object_checkbox.select()
    else:
        object_checkbox.configure(state="normal", fg="black")
        if isinstance(object_checkbox, tk.Checkbutton):
            object_checkbox.deselect()

def toggle_active_disabled(actor_button_state, object_buttons):
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



