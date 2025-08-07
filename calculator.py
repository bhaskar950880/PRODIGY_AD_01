import tkinter as tk

# Function to update the expression
def button_click(item):
    current = entry_var.get()
    entry_var.set(current + str(item))

# Function to clear the display
def button_clear():
    entry_var.set("")

# Function to evaluate the expression
def button_equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")
#bhaskar
# Main window
root = tk.Tk()
root.title("Galaxy Calculator")
root.configure(bg="#0b0c10")  # Space-themed background
root.resizable(False, False)

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Consolas', 20), bd=10, insertwidth=2,
                 width=14, borderwidth=4, justify='right', bg="#1f2833", fg="#66fcf1")
entry.grid(row=0, column=0, columnspan=4, ipady=10)

# Button creator function
def create_button(text, row, col, command, colspan=1):
    btn = tk.Button(root, text=text, padx=20, pady=20, bd=2,
                    fg="#c5c6c7", bg="#202833", activebackground="#45a29e",
                    font=('Consolas', 16, 'bold'), command=command)
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

# Button layout
buttons = [
    ('AC', 1, 0, button_clear), ('/', 1, 1, lambda: button_click('/')), ('*', 1, 2, lambda: button_click('*')), ('-', 1, 3, lambda: button_click('-')),
    ('7', 2, 0, lambda: button_click('7')), ('8', 2, 1, lambda: button_click('8')), ('9', 2, 2, lambda: button_click('9')), ('+', 2, 3, lambda: button_click('+')),
    ('4', 3, 0, lambda: button_click('4')), ('5', 3, 1, lambda: button_click('5')), ('6', 3, 2, lambda: button_click('6')), ('=', 3, 3, button_equal),
    ('1', 4, 0, lambda: button_click('1')), ('2', 4, 1, lambda: button_click('2')), ('3', 4, 2, lambda: button_click('3')), ('.', 4, 3, lambda: button_click('.')),
    ('0', 5, 0, lambda: button_click('0')),
]
#bhaskar 



# Create all buttons
for (text, row, col, command) in buttons:
    colspan = 4 if text == '0' else 1
    create_button(text, row, col, command, colspan)




#bhaskar
# Start the app
root.mainloop()
