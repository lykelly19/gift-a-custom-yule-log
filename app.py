from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/yule_log', methods=['POST'])
def yule_log():
    return render_template('yule_log.html')

@app.route('/generate_lyrics', methods=['POST'])
def generate_lyrics():
    return render_template('generate_lyrics.html')



if __name__ == '__main__':
    app.run()
