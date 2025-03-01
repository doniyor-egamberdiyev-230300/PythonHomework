car_names = ["Tesla", "Audi", "BMW", "Mercedes", "Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Hyundai"]

txt = input("Enter the text: ")

name = txt.lower()

found_cars = [car for car in car_names if all(char.lower() in name for char in car)]

if found_cars:
    print("Car names found:", ", ".join(found_cars))
else:
    print("No car names found.")
