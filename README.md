# CurvPy
CurvPy
CurvPy is a powerful data analysis tool that specializes in fitting curves to your data in CSV format. With CurvPy, you can easily analyze and visualize your data to gain insights into the underlying mathematical functions that best describe your dataset.

## Usage
Input Files in CSV Format: CurvPy accepts data files in CSV format, allowing you to seamlessly work with your tabular data. You can import your CSV files directly into CurvPy for analysis and curve fitting.
CurvPy provides the following three main tools to help you analyze and fit curves to your data:

## DataSleuth: Guess the Function
The DataSleuth tool in CurvPy leverages advanced algorithms to automatically analyze your data and provide a best-guess estimate of the underlying mathematical function that describes your dataset. By examining the trends and patterns in your data, DataSleuth intelligently suggests potential functions that may fit your data.

## FuncPlot: Test the Function
Once you have a guess about the mathematical function that describes your data, you can use the FuncPlot tool to test the function and visualize its fit to your dataset. Simply input the mathematical expression of the function, and CurvPy will generate a graph that compares the function to your data. This visual representation allows you to inspect and evaluate the quality of the fit.

## OptiFit: Optimize Parameters
The OptiFit tool in CurvPy empowers you to fine-tune the parameters of the chosen mathematical function to optimize the fit to your data. By adjusting the equation parameters, you can achieve precise and efficient data modeling. CurvPy utilizes powerful optimization algorithms to find the optimal values for the equation parameters, resulting in an improved fit between the function and your dataset.

CurvPy provides an intuitive web interface that allows you to interact with these tools seamlessly. You can upload your CSV files, select the desired tool, and navigate through the various features to perform curve fitting and analysis on your data.

With CurvPy, you can unlock the power of curve fitting and gain deeper insights into your data. Whether you are exploring scientific data, conducting research, or performing data analysis tasks, CurvPy provides a user-friendly and efficient solution to fit curves to your CSV data.

## Installation
To use CurvPy, you need to have Python and the following dependencies installed:
- pip
- Flask
- pandas
- NumPy
- matplotlib
- scipy
- scikit-learn

You can install the required dependencies using pip:

```shell
pip install -r requirements.txt
```

- Otherwise, you can individually install all these packages.
- For Linux-based systems, you may need to use pip3 instead of pip.

## Usage
1. Clone the repository:
```shell
git clone https://github.com/your-username/CurvPy.git
```
Note for Windows Users: If you are using a Windows machine, download the project as a ZIP file from the GitHub repository. Extract the ZIP file to a location of your choice and open the command prompt or PowerShell. Navigate to the extracted directory using the cd command and list the files using the dir command. Here's an example:
```shell
cd C:\path\to\CurvPy
dir
```
2. Navigate to the project directory:
```shell
cd CurvPy
```
3. Install the required dependencies:
```shell
pip install -r requirements.txt
```
For Linux-based systems, use pip3 instead of pip.

4. Launch CurvPy:
```shell
python app.py
```
5.Open your web browser and paste the following URL:
```shell
http://localhost:5000
```
6.Start using CurvPy by selecting one of the three main functionalities: DataSleuth, FuncPlot, or OptiFit.

## Screenshots
![Screenshot 2023-06-24 153541](https://github.com/sidhu2690/CurvPy/assets/136654152/f43a91d2-295c-4b35-ab7e-119ffaac3d8e)

## Contributing
Contributions are welcome! If you'd like to contribute to CurvPy, please fork the repository and create a pull request with your changes.


