from flask import Flask, render_template, request, url_for, redirect, g, session
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from functools import wraps
import os
import cloudinary.uploader

cloudinary.config(cloud_name='drezt4si4', api_key="264118375198766", api_secret="ENJyiF-pECeilBaLYwhQY1SE06A")

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
db = SQLAlchemy(app)

from configs.base_config import Development, Production, Staging

from models.Client import Client
from models.ExternalLink import ExternalLink
from models.News import News

app.config.from_object(Production)

@app.before_first_request
def create_tables():
    db.create_all()

# create a login required wrapper for user
def user_login_required(f): #define a function whose first parameter is f, which is convention for the fact that it wraps a function
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            print("Authorized to login")
            return f(*args, **kwargs)
        else:
            # flash('Unauthorized! Please log in','danger')
            print("Unauthorized")
            return redirect(url_for('login',next=request.url))
    return wrap

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print("email", email)
        print("password", password)

        if email == "admin@gmail.com" and password == "admin001":
            session['email'] = email
            # session['password'] = password
            session['logged_in'] = True
            return redirect(url_for('admin_news'))
        else:
            return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/admin_news', methods = ['GET', 'POST'])
@user_login_required
def admin_news():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        news = News(title = title, description = description)
        db.session.add(news)
        db.session.commit()
    
    news_items = News.query.all()

    return render_template("admin_news.html", news_items = news_items)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/admin_images', methods = ['GET', 'POST'])
@user_login_required
def admin_images():
    if request.method == 'POST':        
        image = request.files['file']
        link = request.form['link']

        # check if the post request has the file part
        # if 'image' not in image:
            # flash('No file part','danger')
        print("image", type(image))
        # return redirect(request.url)
        # print(image)

        file = image

        if file.filename == '':
            # flash('No selected file','danger')
            print("No file selected")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # upload the file to cloudinary
            upload_data = cloudinary.uploader.upload(file)


        data = ExternalLink(image=upload_data['secure_url'], link=link)
        db.session.add(data)
        db.session.commit()
        # flash("External link added successfully")
        print("External link added successfully")
    
    images = ExternalLink.query.all()

    return render_template("admin_external_links.html", images = images)

@app.route('/admin_clients', methods = ['GET', 'POST'])
@user_login_required
def admin_clients():
    if request.method == 'POST':
        title = request.form['title']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        marital_status = request.form['marital_status']
        occupation = request.form['occupation']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        email = request.form['email']

        clients = Client(title = title, first_name = first_name, last_name = last_name, marital_status = marital_status, occupation = occupation, address = address, city = city, state = state, zip_code = zip_code, phone_number = phone_number, email = email)
        print(clients)
        db.session.add(clients)
        db.session.commit()

    clients = Client.query.all()

    return render_template("clients.html", clients = clients)

@app.route('/high_commission')
def high_commision():
    return render_template("high_commision.html")

@app.route('/whats-new')
def whats_new():

    news_items = News.query.all()

    return render_template("whatsNew.html", news_items=news_items)

@app.route('/office_hours')
def office_hours():
    return render_template('officeHours.html')

@app.route('/sri_lanka_and_kenya')
def sri_lanka():
    return render_template("/srilanka_kenya.html")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        title = request.form['title']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        marital_status = request.form['marital_status']
        occupation = request.form['occupation']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        email = request.form['email']

        clients = Client(title = title, first_name = first_name, last_name = last_name, marital_status = marital_status, occupation = occupation, address = address, city = city, state = state, zip_code = zip_code, phone_number = phone_number, email = email)
        print(clients)
        db.session.add(clients)
        db.session.commit()

    return render_template("register.html")

@app.route('/consular')
def consular():
    return render_template("consular.html")

@app.route('/tourism')
def tourism():
    return render_template("tourism.html")

@app.route('/contact')
def contact():
    if request.method == 'POST':
        title = request.form['title']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        marital_status = request.form['marital_status']
        occupation = request.form['occupation']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        email = request.form['email']

        clients = Client(title = title, first_name = first_name, last_name = last_name, marital_status = marital_status, occupation = occupation, address = address, city = city, state = state, zip_code = zip_code, phone_number = phone_number, email = email)
        db.session.add(clients)
        db.session.commit()
        
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()