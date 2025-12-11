from flask import Flask, render_template, request, redirect, url_for, flash, session
from db import fetch_all_dict, execute_query

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = fetch_all_dict('Users')
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['user'] = username
                session['role'] = user['role']
                flash(f"Logged in as {username}", "success")
                return redirect(url_for('home'))
        flash("Invalid credentials", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out", "info")
    return redirect(url_for('home'))

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    vehicles = fetch_all_dict("Vehicles")
    filtered = vehicles

    if request.method == 'POST':
        vehicle_type = request.form.get('vehicle_type', '').lower()
        manufacturer = request.form.get('manufacturer', '').lower()
        model_year = request.form.get('model_year', '')
        color = request.form.get('color', '').lower()

        def matches(vehicle):
            if vehicle_type and vehicle_type not in vehicle['vehicle_type'].lower():
                return False
            if manufacturer and manufacturer not in vehicle['manufacturer'].lower():
                return False
            if model_year and str(vehicle['model_year']) != model_year:
                return False
            if color and color not in vehicle['color'].lower():
                return False
            return True

        filtered = [v for v in vehicles if matches(v)]

    return render_template('inventory.html', vehicles=filtered)

@app.route('/buy/<vin>', methods=['GET', 'POST'])
def buy(vehicle_id):
    vehicles = fetch_all_dict('Vehicles')
    vehicle = next((v for v in vehicles if v['vin'] == vehicle_id), None)
    if not vehicle:
        flash("Vehicle not found", "danger")
        return redirect(url_for('inventory'))

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        purchase_price = request.form['purchase_price']
        try:
            execute_query(
                "UPDATE Vehicles SET customer_id=%s, status='Purchased', purchase_price=%s WHERE vehicle_id=%s",
                (customer_id, purchase_price, vehicle_id)
            )
            flash(f"Vehicle {vehicle_id} purchased by customer {customer_id}!", "success")
        except Exception as e:
            flash(f"Error purchasing vehicle: {str(e)}", "danger")
        return redirect(url_for('inventory'))

    return render_template('buy.html', vehicle=vehicle)



@app.route('/sell/<vin>', methods=['GET', 'POST'])
def sell(vehicle_id):
    vehicles = fetch_all_dict('Vehicles')
    vehicle = next((v for v in vehicles if v['vin'] == vehicle_id), None)
    if not vehicle:
        flash("Vehicle not found", "danger")
        return redirect(url_for('inventory'))

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        sale_price = request.form['sale_price']
        try:
            execute_query(
                "UPDATE Vehicles SET customer_id=%s, status='Sold', sale_price=%s WHERE vehicle_id=%s",
                (customer_id, sale_price, vehicle_id)
            )
            flash(f"Vehicle {vehicle_id} sold to customer {customer_id}!", "success")
        except Exception as e:
            flash(f"Error selling vehicle: {str(e)}", "danger")
        return redirect(url_for('inventory'))

    return render_template('sell.html', vehicle=vehicle)



if __name__ == '__main__':
    app.run(debug=True)
