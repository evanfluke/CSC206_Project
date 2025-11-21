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


@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/vehicles')
def vehicles():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicles;")
    vehicles_list = cursor.fetchall()
    cursor.close()
    conn.close()
    print(vehicles_list)
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
