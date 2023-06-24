import tkinter as tk
import subprocess

def execute_code():
    # Get the code from the text widget
    code = code_text.get("1.0", tk.END)

    # Execute the code
    exec(code)

# Create the main window
root = tk.Tk()
root.title("Execute Code Example")
root.geometry("500x400")

# Hide the main window
root.withdraw()

# Create the text widget
code_text = tk.Text(root, height=20, width=60)
code_text.pack()

# Example code to print "hello"
example_code = '''
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import filedialog, messagebox

# Function to update the plot
def update_plot():
    # Get the selected labels for x and y
    x_label = x_variable.get()
    y_label = y_variable.get()

    # Check if valid labels are selected
    if x_label and y_label:
        try:
            # Get the column indices for x and y labels
            x_index = column_labels.index(x_label)
            y_index = column_labels.index(y_label)

            # Read the data from the CSV file
            data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

            # Extract the x and y values based on the selected labels
            x = data[:, x_index]
            y = data[:, y_index]

            # Clear the plot
            ax.clear()

            # Plot the data
            ax.plot(x, y)

            # Plot the function if entered
            if function_entry.get():
                x_values = np.linspace(min(x), max(x), 100)
                function_str = function_entry.get()

                # Apply filters to the function string
                function_str = function_str.replace('sin', 'np.sin')
                function_str = function_str.replace('cos', 'np.cos')
                function_str = function_str.replace('tan', 'np.tan')
                function_str = function_str.replace('arcsin', 'np.arcsin')
                function_str = function_str.replace('arccos', 'np.arccos')
                function_str = function_str.replace('arctan', 'np.arctan')
                function_str = function_str.replace('log', 'np.log')
                function_str = function_str.replace('^', '**')
                function_str = function_str.replace('e', 'np.e')

                try:
                    y_values = eval(function_str, {'np': np, 'x': x_values})
                    ax.plot(x_values, y_values)
                except Exception as e:
                    print("Error:", str(e))

            # Update the plot
            canvas.draw()
        except ValueError:
            messagebox.showerror("Error", "Invalid labels selected!")
    else:
        messagebox.showerror("Error", "Please select labels for both x and y variables.")

# Function to refresh column labels
def refresh_labels():
    global column_labels

    # Clear the existing labels
    x_dropdown['menu'].delete(0, 'end')
    y_dropdown['menu'].delete(0, 'end')

    # Read the labels from the CSV file
    with open(file_path, 'r') as file:
        first_row = file.readline().strip()
        column_labels = first_row.split(',')

    # Populate the drop-down menus with column labels
    for label in column_labels:
        x_dropdown['menu'].add_command(label=label, command=tk._setit(x_variable, label))
        y_dropdown['menu'].add_command(label=label, command=tk._setit(y_variable, label))

# Function to accept the CSV file
def accept_csv_file():
    global file_path

    # Open file dialog to select the CSV file
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    # Refresh column labels
    refresh_labels()

# Function to show instructions
def show_instructions():
    instructions = """Instructions:
    - Enter the function in terms of 'x' in the function input field.
    - Trigonometric functions: sin(x), cos(x), tan(x)
    - Inverse trigonometric functions: arcsin(x), arccos(x), arctan(x)
    - Logarithmic function: log(x)
    - Constant: e
    - Use '**' instead of '^' for exponentiation.
    - Example: sin(2*x) + log(x)"""
    messagebox.showinfo("Instructions", instructions)

# Create the main window
window = tk.Tk()
window.title("CSV Plotter")

# Create a frame for the file selection
file_frame = tk.Frame(window)
file_frame.pack(pady=10)

# Create a button to accept the CSV file
accept_button = tk.Button(file_frame, text="Accept CSV File", command=accept_csv_file)
accept_button.pack(pady=5)

# Create a button to refresh labels
refresh_button = tk.Button(window, text="Refresh Labels", command=refresh_labels)
refresh_button.pack(pady=5)

# Create a label frame to display the column labels
label_frame = tk.Frame(window)
label_frame.pack()

# Create a drop-down menu for x variable selection
x_variable = tk.StringVar()
x_dropdown = tk.OptionMenu(label_frame, x_variable, '')
x_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

# Create a drop-down menu for y variable selection
y_variable = tk.StringVar()
y_dropdown = tk.OptionMenu(label_frame, y_variable, '')
y_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

# Create a frame for the function input
function_frame = tk.Frame(window)
function_frame.pack(pady=10)

# Create a label and an entry widget for the function input
function_label = tk.Label(function_frame, text="Function:")
function_label.pack(side=tk.LEFT)
function_entry = tk.Entry(function_frame, width=40)
function_entry.pack(side=tk.LEFT)

# Create a button to update the plot
plot_button = tk.Button(window, text="Plot", command=update_plot)
plot_button.pack(pady=5)

# Create a button to show instructions
instructions_button = tk.Button(window, text="Instructions", command=show_instructions)
instructions_button.pack(pady=5)

# Create a figure and canvas for the plot
fig = plt.figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(pady=5)

# Create a navigation toolbar
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.pack()

# Create the main loop
tk.mainloop()

'''

# Insert the example code into the text widget
code_text.insert(tk.END, example_code)

# Execute the code
exec(example_code)

root.mainloop()
