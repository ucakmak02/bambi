from flask import Flask, render_template,request,redirect,flash,url_for,session,send_from_directory
from flask_mysqldb import MySQL
from form_classes import *
from functools import wraps
from werkzeug.utils import secure_filename
from datetime import datetime
import os

data_path = "./static/images"

app = Flask(__name__,static_folder="./static")

app.secret_key ='3d6f45a5fc12445dbac2f59c3b6c7cb1'


# Check if user logged in
def is_logged_in(f):
    '''this function checks whether user is logged in or not. Use this function as a decorator
    for example, if you don't want user to reach some functions without logging in put this function on top of the other function as a decorator. See upload funcion'''
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Doğrulanamadı Lütfen Giriş Yapınız', 'danger')
            return redirect(url_for('home'))
    return wrap

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
   app.logger.info('Login function is processing')
   if request.method == 'POST':
      # Get Form Fields
      global username
      username = request.form['username']
      password_candidate = request.form['password']
      

      # Compare Passwords
      if password_candidate == "admin" and username == "admin":
      #if check_password_hash(password_candidate, password):
            # Passed
            session['logged_in'] = True
            session['username'] = username

            app.logger.info('username "{}" logged in'.format(session['username']))
            return redirect(url_for('home'))
      else:
            error = 'Yanlış kuullanıcı adı yada şifre. Lütfen tekrar deneyiniz.'
            print(error)
            return render_template('admin.html', error=error)
      # Close connection
   return render_template("admin.html")

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    '''this function signs out user and clears the session. session.clear() function clears the current variables available to the Flask.'''
    session.clear()

    flash('Çıkış yaptınız', 'danger')
    return redirect(url_for('home'))

@app.route('/urunler/<product_name>', methods=['GET','POST'])
def products(product_name):
   product_name = product_name
   return render_template("products.html",**locals())



ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/urun_ekle', methods=['GET','POST'])
def urun_ekle():
   if request.method == 'POST':
      aciklama = request.form['aciklama']
      
      files = request.files.getlist('files_main[]')
      for file in files:
         if file and allowed_file(file.filename):
            filename = secure_filename(str(datetime.now())+"_date_"+file.filename)
            print("filename:",filename)
            file.save(os.path.join(data_path, filename))
   return render_template("add_product.html")

@app.route('/satin_al/<product_id>', methods=['GET','POST'])
def buy(product_id):
   product_id = product_id
   return render_template("buy.html",**locals())



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)