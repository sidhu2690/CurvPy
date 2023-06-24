from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file1')
def run_file1():
    subprocess.run(['python', 'ddd.py'], check=True)
    return "File 1 executed!"

@app.route('/file2')
def run_file2():
    subprocess.run(['python', 'Main.py'], check=True)
    return "File 2 executed!"

@app.route('/file3')
def run_file3():
    subprocess.run(['python', 'optimizer.py'], check=True)
    return "File 3 executed!"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
