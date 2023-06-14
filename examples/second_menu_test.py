import tkinter as tk


class MainMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Main Menu")
        self.window.geometry("400x300")

        self.option1_button = tk.Button(self.window, text="Option 1", command=self.show_option1_menu)
        self.option1_button.pack(pady=50)

    def show_option1_menu(self):
        option1_menu = tk.Toplevel(self.window)
        option1_menu.title("Option 1 Menu")
        option1_menu.geometry("200x100")

        yes_button = tk.Button(option1_menu, text="Yes")
        yes_button.pack(pady=10)

        no_button = tk.Button(option1_menu, text="No")
        no_button.pack(pady=10)


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.window.mainloop()
