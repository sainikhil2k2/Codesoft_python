import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_choice.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operation"

    result_label.config(text="Result: " + str(result))


app = tk.Tk()
app.title("Simple Calculator")


entry_num1 = tk.Entry(app, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

operation_choice = tk.StringVar()
operation_choice.set("+")
operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(app, operation_choice, *operations)
operation_menu.grid(row=0, column=1, padx=5, pady=5)

entry_num2 = tk.Entry(app, width=10)
entry_num2.grid(row=0, column=2, padx=5, pady=5)


calculate_btn = tk.Button(app, text="Calculate", command=calculate)
calculate_btn.grid(row=1, column=0, columnspan=3, padx=5, pady=10)


result_label = tk.Label(app, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)


app.mainloop()
