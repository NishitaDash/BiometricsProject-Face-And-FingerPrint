from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from collections import defaultdict
import sys
import random
import matplotlib
import os
matplotlib.use('Agg')
from flask import Markup
PEOPLE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
#TEMPLATES_AUTO_RELOAD=True
@app.route('/')
def view_home():
    return render_template('Welcome.html')
@app.route('/upload')
def upload_file():
    return render_template('Upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'DONE'
#@app.route('/AUpload', methods = ['GET', 'POST'])
#def AUpload():
    #if request.method == 'POST':
 
if __name__ == '__main__':
    app.run(debug=True)