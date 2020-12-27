from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import random
import smtplib
import os
from email.mime.text import MIMEText

app = Flask(__name__)
BASE_URL = os.environ['BASE_URL']
GMAIL_USER = os.environ['GMAIL_USER']
GMAIL_PASSWORD = os.environ['GMAIL_PASSWORD']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def return_to_index():
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

@app.route('/share_yule_log')
def share_yule_log_default():
    return render_template('share_yule_log.html')

@app.route('/share_yule_log', methods=['POST', 'GET'])
def share_yule_log():
    return render_template('share_yule_log.html')

@app.route('/send_email', methods=['POST'])
def send_yule_log_email():

    sender_name = request.form['sender-name'].strip()
    recipient_name = request.form['recipient-name'].strip()
    recipient_email = request.form['recipient-email'].strip()
    email_message = request.form['email-message'].strip()
    playlist_link = request.form['log-link'].strip()

    subject = "A Customized Yule Log for You!"

    body = "Hi " + sender_name
    body += "\nI customized this Yule Log for you: " + playlist_link
    body += "\n\n" +  email_message
    body += "\n-" + recipient_name

    to = []
    to.append(recipient_email)

    message = """\From: %s\nTo: %s\nSubject: %s\n%s
    """ % (gmail_user, ", ".join(to), subject, body)

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(gmail_user, gmail_password)

        print(message)

        s.sendmail(gmail_user, to, message)
        s.quit()
        print("Email sent!")
    except:
        print("Email failed to send")

    return render_template('email_sent.html')


@app.route('/send_yule_log', methods=['POST', 'GET'])
def send_yule_log():
    playlist_id = request.form['playlist-string']
    playlist_html = ""
    shareable_link_html = ""
    link_form_html = ""
    if playlist_id is not None:
        params = playlist_id.split(':')
        if len(params) == 3:
            link = "{}{}{}".format(BASE_URL, '/yule_log?playlist_id=', playlist_id)
            shareable_link_html = '<input type="text" value=' + link + ' id=playlist-link>'
            playlist_html = '<iframe src="https://open.spotify.com/embed/{}/{}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" id="spotify-playlist"></iframe>'.format(params[1], params[2])
            link_form_html = '<input type="text" name="log-link" value={}><br>'.format(link)

    return render_template('send_yule_log.html', html_playlist_string=playlist_html, shareable_link_html=shareable_link_html, link_form_html=link_form_html)

@app.route('/faq')
def display_faq_page_default():
    return render_template('faq.html')

@app.route('/faq', methods=['POST', 'GET'])
def display_faq_page():
    return render_template('faq.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
