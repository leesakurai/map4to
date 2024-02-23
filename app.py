from ast import Return
from asyncore import file_dispatcher
from fileinput import filename
from os import device_encoding
from shutil import register_unpack_format
from unicodedata import name
from flask import Flask, render_template, request, url_for, redirect
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    elif request.method == 'POST':
        file = request.files['example']
        file.save(os.path.join('./static/image', file.filename))
        return redirect(url_for('uploaded_file', filename=file.filename))





@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)