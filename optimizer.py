import numpy as np
from scipy.optimize import curve_fit
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Create a tkinter window
window = tk.Tk()
df = None
x = None
y = None
equation_entry = None
guess_entry = None

# Function to handle the 'x' button click event
def select_x():
    global x
    x = select_label()

# Function to handle the 'y' button click event
def select_y():
    global y
    y = select_label()

# Function to open a file dialog and select a CSV file
def select_csv_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch the CSV file.")

# Function to display a label selection dialog
def select_label():
    selected_label = None

    # Create a tkinter dialog window
    label_window = tk.Toplevel(window)
    label_window.geometry("400x300")  # Set a larger size for the window

    # Function to handle label selection
    def select(label):
        nonlocal selected_label
        selected_label = label
        label_window.destroy()

    try:
        # Get the labels from the CSV file
        labels = df.columns.tolist()

        # Create buttons for each label
        for label in labels:
            button = tk.Button(label_window, text=label, command=lambda l=label: select(l))
            button.pack()
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch the labels from the CSV file.")

    # Wait for the label selection
    label_window.wait_window()

    return selected_label

# Function to handle the analyze button click event
def analyze():
    # Check if 'x' and 'y' are selected
    if x is None or y is None:
        return

    # Get the equation structure and initial guesses from the input fields
    equation = equation_entry.get()
    guesses = [float(guess.strip()) for guess in guess_entry.get().split(",")]

    # Modify the equation structure
    equation = equation.replace("log", "np.log")
    equation = equation.replace("sin", "np.sin")
    equation = equation.replace("cos", "np.cos")

    # Extract the parameters from the equation structure
    parameters = re.findall(r'\b[a-df-wyz]\b', equation)

    # Create the user-defined function based on the equation structure
    def user_function(x, *params):
        param_dict = {param: val for param, val in zip(parameters, params)}
        return eval(equation, {'np': np, 'exp': np.exp, 'power': np.power}, {'x': x, **param_dict})

    # Get the selected columns as NumPy arrays
    x_data = df[x].values
    y_data = df[y].values

    try:
        # Perform the optimization using curve_fit with increased maxfev
        optimized_params, covariance = curve_fit(user_function, x_data, y_data, p0=guesses, maxfev=1000)

        # Print the optimized parameters
        print("Optimized Parameters:")
        for param, value in zip(parameters, optimized_params):
            print(f"{param}: {value}")

        # Generate the fitted curve using the optimized parameters
        x_fit = np.linspace(min(x_data), max(x_data), 100)
        y_fit = user_function(x_fit, *optimized_params)

        # Plot the data and the fitted curve
        plt.figure()
        plt.scatter(x_data, y_data, label='Data')
        plt.plot(x_fit, y_fit, label='Fitted Curve')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", "An error occurred during analysis.")

# Function to handle the upload button click event
def upload():
    global df
    df = select_csv_file()

    # Create a tkinter dialog window
    label_selection_window = tk.Toplevel(window)
    label_selection_window.geometry("400x300")  # Set a larger size for the window

    # Create 'x' and 'y' buttons
    x_button = tk.Button(label_selection_window, text="x", command=select_x)
    x_button.pack()

    y_button = tk.Button(label_selection_window, text="y", command=select_y)
    y_button.pack()

    # Create equation label and entry
    equation_label = tk.Label(label_selection_window, text="Equation Structure:")
    equation_label.pack()
    global equation_entry
    equation_entry = tk.Entry(label_selection_window)
    equation_entry.pack()

    # Create initial guesses label and entry
    guess_label = tk.Label(label_selection_window, text="Initial Guesses (comma-separated):")
    guess_label.pack()
    global guess_entry
    guess_entry = tk.Entry(label_selection_window)
    guess_entry.pack()

    # Create 'Analyze' button
    analyze_button = tk.Button(label_selection_window, text="Analyze", command=analyze)
    analyze_button.pack()

# Function to handle the 'Instructions' button click event
def show_instructions():
    instructions = '''
    Instructions:
    1. Click 'Upload CSV' to select a CSV file.
    2. Click 'x' and 'y' buttons to select the respective columns.
    3. Enter the equation structure in the 'Equation Structure' field.
       - Use 'log' for logarithm (base e).
       - Use 'sin' for sine function.
       - Use 'cos' for cosine function.
       - Use 'exp()' for exponential function.
       - Example: 'a * log(b * x) + c * sin(d * x) + e'
     4. Enter initial guesses for the parameters in the 'Initial Guesses' field, separated by commas.
     5. Click 'Analyze' to perform the optimization and plot the graph.
    '''
    messagebox.showinfo("Instructions", instructions)

# Create 'Upload CSV' button
upload_button = tk.Button(window, text="Upload CSV", command=upload)
upload_button.pack()

# Create 'Instructions' button
instructions_button = tk.Button(window, text="Instructions", command=show_instructions)
instructions_button.pack()

# Start the tkinter event loop
window.mainloop()
