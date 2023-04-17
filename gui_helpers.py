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

def autodisable_checkbox(actor_checkbox_state, object_checkbox):
    if actor_checkbox_state.get():
        object_checkbox.configure(state="disabled", fg="gray")
    else:
        object_checkbox.configure(state="normal", fg="black")
        if isinstance(object_checkbox, tk.Checkbutton):
            object_checkbox.deselect()


def depress_button(self, button, other_buttons=None):
    button.configure(bg="green")
    button.configure("relief")[-1] == "sunken"
    if other_buttons:
        for b in other_buttons:
            b.configure(bg="light gray")
def release_button(self, button, other_buttons=None):
    button.configure(bg="white")
    button.configure("relief")[-1] == "raised"
    # if other_buttons:
    #     for b in other_buttons:
    #         b.configure(bg="original_color")



