from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import random

app = Flask(__name__)
BASE_URL = '127.0.0.1:5000'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yule_log', methods=['GET'])
def yule_log_get():

    playlist_id = request.args.get('playlist_id')

    if playlist_id is not None:
        params = playlist_id.split(':')
        if len(params) == 3:

            default_playlist = '<iframe src="https://open.spotify.com/embed/{}/{}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" id="spotify-playlist"></iframe>'.format(params[1], params[2])
            return render_template('yule_log.html', html_playlist_string=default_playlist)

    yule_log_post()


@app.route('/yule_log', methods=['POST'])
def yule_log_post():
    default_playlist = '<iframe src="https://open.spotify.com/embed/playlist/3CLNJhCOjntppUuW3xUR9s" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" id="spotify-playlist"></iframe>'
    return render_template('yule_log.html', html_playlist_string=default_playlist)


@app.route('/generate_lyrics', methods=['POST', 'GET'])
def generate_lyrics():
    return render_template('generate_lyrics.html')


@app.route('/share_yule_log', methods=['POST', 'GET'])
def share_yule_log():
    return render_template('share_yule_log.html')


@app.route('/send_yule_log', methods=['POST', 'GET'])
def send_yule_log():
    playlist_id = request.form['playlist-string']
    if playlist_id is not None:
        params = playlist_id.split(':')
        if len(params) == 3:
            shareable_link = BASE_URL + "/yule_log?playlist_id=" + playlist_id
            playlist_html = '<iframe src="https://open.spotify.com/embed/{}/{}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" id="spotify-playlist"></iframe>'.format(params[1], params[2])

    return render_template('send_yule_log.html', html_playlist_string=playlist_html, shareable_link=shareable_link)

@app.route('/faq', methods=['POST', 'GET'])
def display_faq_page():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run()
