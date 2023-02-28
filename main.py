import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    # It is global variable so we can change it inside a function.
    global calculation
    # Everything passed will e converted into string and stored in calculation
    calculation += str(symbol)
    # Everything passed in the textbox will be deleted and the calculation in which everything will be changed to string will be shown
    text_result.delete(1.0, "end")
    # String is inserted
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        # calculation = str(eval(calculation))
        # text_result.delete(1.0, "end")
        # text_result.insert(1.0, calculation)

        # or
        # This one is better
        # eval is a python function to evaluate python code
        # We are using it to evaluating calculation
        result = str(eval(calculation))
        # To reset the textbox we are doing this
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        # For example if we divide by zero it will give error
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    # Clearing the textbox
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("275x275")

# this is the text field in which the numbers are passed and the result is shown.
text_result = tk.Text(root, height=2, width=15, font=("Arial", 24))
# columnspan is used to specify the number of column it is going to use
# In this case result box is going to use all 5 columns.
text_result.grid(columnspan=5)

# We are using lambda to pass a parameter easily
# For passing a parameter use lambda
# For passing the function we don't use lambda
# ticky is used to stretch the keys so there's no space between them
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(
    1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(
    2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=1, sticky=tk.W+tk.E)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(
    3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=2, sticky=tk.W+tk.E)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(
    4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=0, sticky=tk.W+tk.E)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(
    5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=1, sticky=tk.W+tk.E)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(
    6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=2, sticky=tk.W+tk.E)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(
    7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=0, sticky=tk.W+tk.E)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(
    8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=1, sticky=tk.W+tk.E)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(
    9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=2, sticky=tk.W+tk.E)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(
    0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=1, sticky=tk.W+tk.E)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation(
    "+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=3, sticky=tk.W+tk.E)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation(
    "-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=3, sticky=tk.W+tk.E)

btn_multiplication = tk.Button(root, text="*", command=lambda: add_to_calculation(
    "*"), width=5, font=("Arial", 14))
btn_multiplication.grid(row=4, column=3, sticky=tk.W+tk.E)

btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation(
    "/"), width=5, font=("Arial", 14))
btn_division.grid(row=5, column=3, sticky=tk.W+tk.E)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation(
    "("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=0, sticky=tk.W+tk.E)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(
    ")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=2, sticky=tk.W+tk.E)

btn_equals = tk.Button(
    root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=2, columnspan=2, sticky=tk.W+tk.E)

# If we are uing parenthesis we are calling the function
# In this case we are passing the function and not calling it so no parenthesis
btn_clear = tk.Button(root, text="C",
                      command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)

root.mainloop()
