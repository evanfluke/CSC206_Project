from flask import Flask, render_template, request
app = Flask(__name__)

from db import get_connection

#mysql = MySQL(app)

#from flask_mysqldb import MySQL
#import MySQLdb.cursors 
#import sys
#import layout as lay

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'geneva'
#app.config['MYSQL_PASSWORD'] = 'Password'
#app.config['MYSQL_DB'] = 'csc206cars'

@app.context_processor
def inject_request():
    return dict(request=request)

@app.route('/')
def index():
    return render_template('home.html', request=request)

@app.route('/home')
def home():
    return render_template('home.html', request=request)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            session['username'] = user['username']
            session['role'] = user['role']
            return redirect(url_for('home'))
        else:
            error = "Wrong username or password, please try again."

    return render_template('login.html', request=request)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/buy')
def buy():
    return render_template('buy.html', request=request)

@app.route('/sell')
def sell():
    return render_template('sell.html', request=request)

@app.route('/reports')
def reports():
    return render_template('reports.html', request=request)

# Reportws Routes

@app.route('/reports/sales_productivity')
def report_sales_productivity():
    return render_template('report_sales_productivity.html', data=[])

@app.route('/reports/seller_history')
def report_seller_history():
    return render_template('report_seller_history.html', data=[])

@app.route('/reports/part_statistics')
def report_part_statistics():
    return render_template('report_part_statistics.html', data=[])

# other routes

@app.route('/customers')
def customers():
    return render_template('customers.html', request=request)

#@app.route('/vehicles')
#def vehicles():
    # conn = get_connection()
    # cursor = conn.cursor(dictionary=True)
    #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #cursor.execute("SELECT * FROM vehicles;")
    #vehicles_list = cursor.fetchall()
    #cursor.close()
    # conn.close()
    #print(vehicles_list)
    #return render_template('vehicles.html', vehicles=vehicles_list)
    #conn = get_connection()
    #cursor = conn.cursor(dictionary=True)
    #cursor.execute("SELECT * FROM vehicles;")
    #vehicles_list = cursor.fetchall()
    #cursor.close()
    #conn.close()
    #print(vehicles_list)
    #return render_template('vehicles.html')

@app.route('/vehicles')
def vehicles():
    conn = get_connection()
    if not conn:
        return "Database connection failed"

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicles;")
    vehicles_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('vehicles.html', vehicles=vehicles_list, request=request)

@app.route('/vehicle_id')
def vehicle_id():
    return render_template('vehicle_id.html', request=request)

# test routes

@app.route('/test_db')
def test_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicle LIMIT 1")
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return str(row)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route("/dbtest")
def dbtest():
    from db import get_db_connection
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SHOW TABLES;")
    tables = cur.fetchall()
    conn.close()
    return {"tables": tables}


if __name__ == '__main__':
    app.run(debug=True)
