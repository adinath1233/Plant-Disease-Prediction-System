from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import csv
from datetime import datetime
from werkzeug.utils import secure_filename
from model import predict_image
import utils
from markupsafe import Markup


app = Flask(__name__)
app.secret_key = 'your_secret_key'


UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            name = request.form['name']
            city = request.form['city']
            file = request.files['file']
            
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            filename = secure_filename(f"{name}_{timestamp}.jpg")
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            with open(filepath, 'rb') as img_file:
                img = img_file.read()
                prediction = predict_image(img)
            
            result = Markup(utils.disease_dic[prediction])

            csv_file = 'results.csv'
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, city, prediction, filename])

            return render_template('display.html', status=200, result=result)
        except Exception as e:
            print(f"Error: {e}")
            return render_template('index.html', status=500, result="Internal Server Error")
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

    users = []
    city_counts = {}
    prediction_counts = {}
    csv_file = 'results.csv'
    if os.path.exists(csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    user = {
                        'name': row[0],
                        'city': row[1],
                        'prediction': row[2],
                        'filename': row[3]
                    }
                    users.append(user)


                    if row[1] in city_counts:
                        city_counts[row[1]] += 1
                    else:
                        city_counts[row[1]] = 1


                    if row[2] in prediction_counts:
                        prediction_counts[row[2]] += 1
                    else:
                        prediction_counts[row[2]] = 1

    return render_template('admin_dashboard.html', users=users, city_data=city_counts, prediction_data=prediction_counts)

if __name__ == "__main__":
    app.run(debug=True)