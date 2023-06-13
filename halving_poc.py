import tkinter as tk

def show_output():
    output_text = "Hello, World!" # Replace with your desired output
    output_box.delete('1.0', tk.END) # Clear previous output
    output_box.insert(tk.END, output_text) # Insert new output

# Create the Tkinter window
window = tk.Tk()
window.title("Dividing Window")

# Create a button on the left
button = tk.Button(window, text="Click Me", command=show_output)
button.grid(row=0, column=0, padx=10, pady=10)

# Create an output box on the right
output_box = tk.Text(window, width=40, height=10)
output_box.grid(row=0, column=1, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()


