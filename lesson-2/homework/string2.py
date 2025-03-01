from collections import Counter

# Sample text and car names
txt = 'LMaasleitbtui'
car_names = ['Tesla', 'BMW', 'Audi', 'Toyota', 'Mazda', 'Lamborghini', 'Mercedes']

# Count the frequency of each letter in the text
txt_counter = Counter(txt.lower())

# Find car names that can be formed from the letters in txt
found_cars = []
for car in car_names:
    car_counter = Counter(car.lower())
    if all(txt_counter[char] >= count for char, count in car_counter.items()):
        found_cars.append(car)

# Display results
if found_cars:
    print("Cars found:", ', '.join(found_cars))
else:
    print("No car names found.")
