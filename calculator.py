import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        expression = display.get()

        # Replace symbols with Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")

    except:
        messagebox.showerror("Error", "Invalid calculation!")


def clear():
    display.delete(0, tk.END)


def add(value):
    display.insert(tk.END, value)


# Main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x500")
window.resizable(False, False)


# Display
display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    bd=10
)
display.pack(
    padx=10,
    pady=20,
    fill="x"
)


# Button frame
button_frame = tk.Frame(window)
button_frame.pack()


buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("÷", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("×", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("+", 3, 2),
    ("=", 3, 3),
]


for text, row, column in buttons:

    if text == "=":
        command = calculate

    else:
        command = lambda value=text: add(value)

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# Clear button
clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 18),
    width=20,
    height=2,
    command=clear
)

clear_button.pack(pady=15)


window.mainloop()