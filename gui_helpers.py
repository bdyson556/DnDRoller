import tkinter

def enable_disable_checkbox(actor_checkbox_state, object_checkbox, ):
    if actor_checkbox_state.get():
        object_checkbox.configure(state="disabled", fg="gray")
        object_checkbox.select()
    else:
        object_checkbox.configure(state="normal", fg="black")
        object_checkbox.deselect()
