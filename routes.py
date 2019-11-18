from flask import Flask, render_template, flash, redirect, url_for, request, session, send_from_directory
from app import app
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId


mongo = PyMongo(app)
client = MongoClient('mongodb://localhost:27017/')
db = client.mydatabase
bcrypt = Bcrypt(app) 

@app.route('/login', methods=['POST'])
def login():
    login_user = db.customers.find_one({'username' : request.form['username']})
    if login_user:
        if bcrypt.check_password_hash(login_user['password'], request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('menu'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':

        existing_user = db.customers.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form['password'])
            db.customers.insert({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/studentform', methods =['GET', 'POST'])
def studentform():
    if 'username' in session:
        if request.method == "POST":
            image = request.files['pic']
            #image.save( image.filename)
            image.save('app/images/'+ image.filename)
            info ={ 'first name': request.form['firstname'],
            'middle name': request.form['middlename'],
            'last name': request.form['lastname'],
            'gender': request.form['gender'],
            'image' : image.filename,
            'email id': request.form['emailid'],
            'address': request.form['address'],
            'phone number': request.form['pnumber']}
            db.Students.insert_one(info)
            #mongo.save_file(image.filename, image)
            flash("Details entered succesfully")
            return render_template('menu.html',title='Menu')
        else:
            render_template('menu.html', title = 'Home')
    return render_template('studentform.html', title = 'Form')

@app.route('/image/<path:path>')
def file(path):
    return send_from_directory('images/', path)

@app.route('/')
@app.route('/index')
def index():
    session.clear()
    if 'username' in session:
        return render_template('menu.html')
    return render_template('index.html', title='Home')
    
@app.route('/menu', methods = ['POST','GET'])
def menu():
    if 'username' in session:
        if request.method == 'POST':
            datastore = request.form['searchbox']
            record_list = db.Students.find({'first name': datastore})
            data = []
            for record in record_list:
                record["_id"] = str(record["_id"])
                data.append(record)
                #session['myvar'] = str(record["_id"])
                #print(record_list)
            if record_list is None:
                flash("No such record!")
            return render_template('menu.html', title = 'Menu', record_list=data)
        return render_template('menu.html', title = "Menu")
    flash("Login again!")
#breakpoint()

@app.route('/studentupdate/<u_id>', methods=['POST','GET'])
def studentupdate(u_id):
    if 'username' in session:
        if request.method == 'POST':
            image = request.files['picu']
            image.save('app/images/'+ image.filename)
            info ={ 'first name': request.form['firstname'],
                'middle name': request.form['middlename'],
                'last name': request.form['lastname'],
                'gender': request.form['gender'],
                'image' : image.filename,
                'email id': request.form['emailid'],
                'address': request.form['address'],
                'phone number': request.form['pnumber']}
            db.Students.update({"_id":ObjectId(u_id)},{"$set":info}, upsert=False)
            return redirect(url_for('menu'))
        user = db.Students.find_one({'_id': ObjectId(u_id)})
        return(render_template('studentupdate.html', title='Update', user=user))
    return 'Login again!'
