from db import fetch_all, insert_row

vehicles = fetch_all("vehicles")
print("Cars table:")
for vehicles in vehicles:
    print(vehicles)

insert_row("vehicles", ["make", "model", "year"], ["Toyota", "Camry", 2020])
print("Inserted a new row.")
