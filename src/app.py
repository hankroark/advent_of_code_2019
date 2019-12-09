import os
import logging

from flask import Flask

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

@app.route('/day04/<int:start_password>/<int:end_password>')
def day04(start_password, end_password):
    results = day04_get_results(start_password, end_password)
    return { 'part1': results[0],
             'part2': results[1] }


if __name__ == '__main__':
    server_port = os.environ.get('PORT')
    if server_port is None:
        print("error: PORT environment variable not set")
        exit(1)

    app.run(debug=True, port=server_port, host='0.0.0.0')
