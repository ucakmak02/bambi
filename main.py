from flask import Flask, render_template,request,redirect,flash,url_for,session,send_from_directory
from flask_mysqldb import MySQL
from form_classes import *
from functools import wraps
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from config import mysql_data,product_list,admin_username,admin_password
import random

data_path = "./static/images"

app = Flask(__name__,static_folder="./static")

app.secret_key ='3d6f45a5fc12445dbac2f59c3b6c7cb1'

app.config['MYSQL_HOST'] = mysql_data["MYSQL_HOST"]
app.config['MYSQL_USER'] = mysql_data["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = mysql_data["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = mysql_data["MYSQL_DATABASE"]
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['default_authentication_plugin']='sha2_password'

mysql = MySQL(app)

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
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM products WHERE product_name = %s",['firstSlide'])
   firstSlide =cur.fetchone()

   cur.execute("SELECT * FROM products WHERE product_name = %s",['secondSlide'])
   secondSlide =cur.fetchone()

   cur.execute("SELECT * FROM products WHERE product_name = %s",['thirdSlide'])
   thirdSlide =cur.fetchone()

   return render_template("index.html",**locals())

@app.route('/admin', methods=['GET', 'POST'])
def admin():
   app.logger.info('Login function is processing')
   if request.method == 'POST':
      # Get Form Fields
      global username
      username = request.form['username']
      password_candidate = request.form['password']


      # Compare Passwords
      if password_candidate == admin_password and username == admin_username:
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

@app.route('/produits/<product_name>', methods=['GET','POST'])
def products(product_name):
   if product_name == 'chambres':
      nameTitle='Chambres a Coucher'
      product_name ='yatak'
   elif product_name == 'salons':
      nameTitle='Salons'
      product_name ='koltuk'
   elif product_name == 'commode':
      nameTitle='Commode'
      product_name ='komidin'
   elif product_name == 'linge':
      nameTitle='Linge de Maison'
      product_name ='tekstil'
   elif product_name == 'decoration':
      nameTitle='Décoration'
      product_name ='aksesuar'
   elif product_name == 'salle-a-manger':
      nameTitle='Salle à Manger'
      product_name ='masa-sandalye'


   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM products WHERE product_class= %s",[product_name])
   all_products =cur.fetchall()
   all_products = list(all_products)

   return render_template("products.html",**locals())



ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@is_logged_in
@app.route('/urun_ekle', methods=['GET','POST'])
def urun_ekle():
   cur = mysql.connection.cursor()
   _product_list = product_list
   if request.method == 'POST':
      image_key = random.randint(10, 100000000000000)
      products_class = request.form['products_class']
      slideNumber = request.form['slideNumber']
      productTitle = request.form['productTitle']
      productExpo = request.form['productExpo']
      productName = request.form['productName']
      productPrice = request.form['productPrice']

      if products_class == 'main_page':
         # Execute query
         cur.execute('delete from products where product_name = %s', [slideNumber])
         mysql.connection.commit()
         # Execute query
         cur.execute("INSERT INTO products (product_class, product_image,product_name,product_price,product_title,product_expo) VALUES (%s, %s,%s, %s,%s, %s)",(products_class, str(image_key)+'.jpg',slideNumber,productPrice,productTitle,productExpo))
         mysql.connection.commit()
         cur.close()
      else:
         # Execute query
         cur.execute("INSERT INTO products (product_class, product_image,product_name,product_price,product_title,product_expo) VALUES (%s, %s,%s, %s,%s, %s)",(products_class, str(image_key)+'.jpg',productName,productPrice,productTitle,productExpo))
         # Commit to DB
         mysql.connection.commit()
         # Close connection
         cur.close()

      files = request.files.getlist('files_main[]')
      for file in files:
         if file and allowed_file(file.filename):
            filename = secure_filename(str(image_key)+'.jpg')
            print("filename:",filename)
            file.save(os.path.join(data_path, filename))
   return render_template("add_product.html",**locals(),)

@app.route('/save_changes', methods=['GET','POST'])
def save_changes():
   cur = mysql.connection.cursor()
   if request.method == 'POST':
      _id= request.form['id']
      _name= request.form['name']
      _price= request.form['price']
      print(_id,_name,_price)
      cur.execute("UPDATE products SET product_name=%s,product_price=%s  WHERE id= %s",[_name,_price,_id])
      # Commit to DB
      mysql.connection.commit()
      # Close connection
      cur.close()
   return render_template("buy.html",**locals())

@app.route('/delete_product', methods=['GET','POST'])
def delete_product():
   cur = mysql.connection.cursor()
   if request.method == 'POST':
      _id= request.form['id']
      image_path = request.form['image_path']

      cur.execute('delete from products where product_image = %s', [image_path])
      # Commit to DB
      mysql.connection.commit()
      # Close connection
      cur.close()
      os.remove('./static/images' + '/' + image_path)
   return render_template("buy.html",**locals())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

