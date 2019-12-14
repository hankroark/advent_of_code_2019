import os
import logging

from flask import Flask, request

from day01.fuel_counter import day01_get_results
from day02.day02 import day02_get_results
from day04.day04 import day04_get_results

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    html = """
<html>
 <head>
  <title>
   Advent of Code 2019 
  </title>
 </head>
 <body>
  <h1>Advent of Code 2019</h1>
  <p>Welcome to Advent of Code 2019.  This implementation is done in Python, with Flask as the web server.
  The code is then deployed into Google Cloud Run.  The source repository contains a button so you can deploy this
  to your Google Cloud Platform organization, as well as documentation on how to use the APIs.</p>
  <a href="https://adventofcode.com/2019" target="_blank">Advent of Code 2019 Webside</a><br>
  <a href="https://github.com/hankroark/advent_of_code_2019" target="_blank">API Docs and Source Code by Hank Roark</a><br>
  <a href="https://cloud.google.com/run/" target="_blank">Google Cloud Run</a>
 </body>
</html>
"""
    return html


"""
Example of use
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@input_fuel_counter.txt" http://localhost:8080/day01
"""
@app.route('/day01', methods=['GET', 'POST'])
def day01():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return {'error': 'No file part' }
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return {'error': 'No selected file'}
        if file:
            data = [int(s) for s in file.read().splitlines()]
            results = day01_get_results(data)
            return {'part1': results[0],
                    'part2': results[1]}
    return '''
    <!doctype html>
    <title>Upload input File</title>
    <h1>Upload input File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/day02/<string:program>/<int:target>')
def day02(program, target):
    results = day02_get_results(program, target)
    return {'part1': results[0],
            'part2': results[1]}

@app.route('/day04/<int:start_password>/<int:end_password>')
def day04(start_password, end_password):
    results = day04_get_results(start_password, end_password)
    return {'part1': results[0],
            'part2': results[1]}


if __name__ == '__main__':
    server_port = os.environ.get('PORT')
    if server_port is None:
        print("error: PORT environment variable not set")
        exit(1)

    app.run(debug=True, port=server_port, host='0.0.0.0')
