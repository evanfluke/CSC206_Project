from flask import Flask, render_template
app = Flask(__name__)

from db import get_connection

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/sell')
def sell():
    return render_template('sell.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/vehicles')
def vehicles():
    return render_template('vehicles.html')

@app.route('/vehicle_id')
def vehicle_id():
    return render_template('vehicle_id.html')

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

if __name__ == '__main__':
    app.run(debug=True)
