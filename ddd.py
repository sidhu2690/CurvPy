import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        # Read CSV file
        data = pd.read_csv(file_path)
        
        # Extract labels from the first row
        labels = data.columns.values.tolist()
        
        # Create a new window
        label_window = tk.Toplevel()
        label_window.title("CSV Labels")
        label_window.geometry("600x500")  # Set window size
        
        # Create label for description
        description_label = tk.Label(label_window, text="Select any two variables from the labels for regression analysis")
        description_label.pack()
        
        # Create option menus for label selection
        var1_label = tk.Label(label_window, text="Variable 1:")
        var1_label.pack()
        var1_option = tk.OptionMenu(label_window, tk.StringVar(), *labels)
        var1_option.pack()
        
        var2_label = tk.Label(label_window, text="Variable 2:")
        var2_label.pack()
        var2_option = tk.OptionMenu(label_window, tk.StringVar(), *labels)
        var2_option.pack()
        
        # Create a column of options
        option_var = tk.StringVar()
        options = ["Linear", "Polynomial", "Exponential", "Logarithmic", "Power-law"]
        
        for option in options:
            tk.Radiobutton(label_window, text=option, variable=option_var, value=option).pack(anchor=tk.W)
        
        # Create submit button
        submit_button = tk.Button(label_window, text="Submit", command=lambda: submit(option_var.get(), var1_option.cget("text"), var2_option.cget("text"), data))
        submit_button.pack()

def submit(regression_type, var1, var2, data):
    # Get the data for the selected variables
    x = data[var1]
    y = data[var2]
    
    # Define the regression functions
    def linear_func(x, m, c):
        return m * x + c
    
    def polynomial_func(x, a, b, c):
        return a * x**2 + b * x + c
    
    def logarithmic_func(x, a, b):
        return a * np.log(x) + b
    
    def exponential_func(x, a, b):
        return a * np.exp(b * x)
    
    def power_law_func(x, a, b):
        return a * np.power(x, b)
    
    # Perform linear regression
    if regression_type == "Linear":
        try:
            linear_coeffs, _ = curve_fit(linear_func, x, y)
            linear_eq = f"y = {linear_coeffs[0]:.2f}x + {linear_coeffs[1]:.2f}"
            r_squared = r2_score(y, linear_func(x, *linear_coeffs))
            r_squared_text = f"R-squared: {r_squared:.2f}"
        except:
            linear_eq = "Error: Unable to fit linear regression"
            r_squared_text = "R-squared: Infinity"
        print("Linear Regression:")
        print(linear_eq)
        print(r_squared_text)
        print()
    
    # Perform polynomial regression (degree=2)
    elif regression_type == "Polynomial":
        try:
            poly_coeffs, _ = curve_fit(polynomial_func, x, y, p0=(1, 1, 1))
            poly_eq = f"y = {poly_coeffs[0]:.2f}x^2 + {poly_coeffs[1]:.2f}x + {poly_coeffs[2]:.2f}"
            r_squared = r2_score(y, polynomial_func(x, *poly_coeffs))
            r_squared_text = f"R-squared: {r_squared:.2f}"
        except:
            poly_eq = "Error: Unable to fit polynomial regression"
            r_squared_text = "R-squared: Infinity"
        print("Polynomial Regression:")
        print(poly_eq)
        print(r_squared_text)
        print()
    
    # Perform logarithmic regression
    elif regression_type == "Logarithmic":
        try:
            log_coeffs, _ = curve_fit(logarithmic_func, x, y)
            log_eq = f"y = {log_coeffs[0]:.2f}ln(x) + {log_coeffs[1]:.2f}"
            r_squared = r2_score(y, logarithmic_func(x, *log_coeffs))
            r_squared_text = f"R-squared: {r_squared:.2f}"
        except:
            log_eq = "Error: Unable to fit logarithmic regression"
            r_squared_text = "R-squared: Infinity"
        print("Logarithmic Regression:")
        print(log_eq)
        print(r_squared_text)
        print()
    
    # Perform exponential regression
    elif regression_type == "Exponential":
        try:
            exp_coeffs, _ = curve_fit(exponential_func, x, y)
            exp_eq = f"y = {exp_coeffs[0]:.2f}e^({exp_coeffs[1]:.2f}x)"
            r_squared = r2_score(y, exponential_func(x, *exp_coeffs))
            r_squared_text = f"R-squared: {r_squared:.2f}"
        except:
            exp_eq = "Error: Unable to fit exponential regression"
            r_squared_text = "R-squared: Infinity"
        print("Exponential Regression:")
        print(exp_eq)
        print(r_squared_text)
        print()
    
    # Perform power law regression
    elif regression_type == "Power-law":
        try:
            power_coeffs, _ = curve_fit(power_law_func, x, y)
            power_eq = f"y = {power_coeffs[0]:.2f}x^{power_coeffs[1]:.2f}"
            r_squared = r2_score(y, power_law_func(x, *power_coeffs))
            r_squared_text = f"R-squared: {r_squared:.2f}"
        except:
            power_eq = "Error: Unable to fit power law regression"
            r_squared_text = "R-squared: Infinity"
        print("Power Law Regression:")
        print(power_eq)
        print(r_squared_text)
        print()
    
    # Generate points for plotting
    x_plot = np.linspace(min(x), max(x), 100)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 8))
    
    if regression_type == "Linear":
        try:
            y_linear = linear_func(x_plot, *linear_coeffs)
            ax.scatter(x, y, label="Data")
            ax.plot(x_plot, y_linear, label=f"Linear")
            ax.set_xlabel(var1)
            ax.set_ylabel(var2)
            ax.legend()
            ax.text(0.05, -0.15, linear_eq, fontsize=10, transform=ax.transAxes)
            ax.text(0.05, -0.2, r_squared_text, fontsize=10, transform=ax.transAxes)
        except:
            ax.text(0.05, -0.15, "Error: Unable to plot linear regression", fontsize=10, transform=ax.transAxes)
    
    elif regression_type == "Polynomial":
        try:
            y_poly = polynomial_func(x_plot, *poly_coeffs)
            ax.scatter(x, y, label="Data")
            ax.plot(x_plot, y_poly, label=f"Polynomial")
            ax.set_xlabel(var1)
            ax.set_ylabel(var2)
            ax.legend()
            ax.text(0.35, -0.15, poly_eq, fontsize=10, transform=ax.transAxes)
            ax.text(0.35, -0.2, r_squared_text, fontsize=10, transform=ax.transAxes)
        except:
            ax.text(0.35, -0.15, "Error: Unable to plot polynomial regression", fontsize=10, transform=ax.transAxes)
    
    elif regression_type == "Logarithmic":
        try:
            y_log = logarithmic_func(x_plot, *log_coeffs)
            ax.scatter(x, y, label="Data")
            ax.plot(x_plot, y_log, label=f"Logarithmic")
            ax.set_xlabel(var1)
            ax.set_ylabel(var2)
            ax.legend()
            ax.text(0.65, -0.15, log_eq, fontsize=10, transform=ax.transAxes)
            ax.text(0.65, -0.2, r_squared_text, fontsize=10, transform=ax.transAxes)
        except:
            ax.text(0.65, -0.15, "Error: Unable to plot logarithmic regression", fontsize=10, transform=ax.transAxes)
    
    elif regression_type == "Exponential":
        try:
            y_exp = exponential_func(x_plot, *exp_coeffs)
            ax.scatter(x, y, label="Data")
            ax.plot(x_plot, y_exp, label=f"Exponential")
            ax.set_xlabel(var1)
            ax.set_ylabel(var2)
            ax.legend()
            ax.text(0.05, -0.4, exp_eq, fontsize=10, transform=ax.transAxes)
            ax.text(0.05, -0.45, r_squared_text, fontsize=10, transform=ax.transAxes)
        except:
            ax.text(0.05, -0.4, "Error: Unable to plot exponential regression", fontsize=10, transform=ax.transAxes)
    
    elif regression_type == "Power-law":
        try:
            y_power = power_law_func(x_plot, *power_coeffs)
            ax.scatter(x, y, label="Data")
            ax.plot(x_plot, y_power, label=f"Power Law")
            ax.set_xlabel(var1)
            ax.set_ylabel(var2)
            ax.legend()
            ax.text(0.35, -0.4, power_eq, fontsize=10, transform=ax.transAxes)
            ax.text(0.35, -0.45, r_squared_text, fontsize=10, transform=ax.transAxes)
        except:
            ax.text(0.35, -0.4, "Error: Unable to plot power law regression", fontsize=10, transform=ax.transAxes)
    
    plt.tight_layout()
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Regression Analysis")
root.geometry("300x200")

# Create open button
open_button = tk.Button(root, text="Choose CSV File", command=open_file_dialog)
open_button.pack()

root.mainloop()
