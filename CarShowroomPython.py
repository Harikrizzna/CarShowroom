# Constants
DATABASE_FILE = "CarShowroomDatabase.txt"

# Function to add a car to the database
def add_car():
    with open(DATABASE_FILE, "a") as file:
        brand = input("Enter the brand: ")
        model = input("Enter the model: ")
        year = input("Enter the year: ")
        price = input("Enter the price: ")
        file.write(brand + "," + model + "," + year + "," + price + "\n")
        print("Car added successfully!")

# Function to view all cars in the database with serial numbers
def view_cars():
    with open(DATABASE_FILE, "r") as file:
        print()
        print("SNo.|    Brand     |    Model     | Year |  Price (INR)")
        print("-" * 56)
        for i, line in enumerate(file, start=1):
            brand, model, year, price = line.strip().split(',')
            print(str(i) + "   " + "| " + brand + " " * (13 - len(brand)) + "| " + model + " " * (13 - len(model)) + "| " + year + " " * (5 - len(year)) + "| " + price + " " * (13 - len(price)))

# Function to search for cars in the database
def search_cars():
    keyword = input("Enter a keyword or number to search for: ")
    with open(DATABASE_FILE, "r") as file:
        found = False
        for line in file:
            brand, model, year, price = line.strip().split(',')
            if keyword in line:
                found = True
                print("Brand: " + brand + ", Model: " + model + ", Year: " + year + ", Price: " + price)
        if not found:
            print("No matching cars found.")

# Function to update a car in the database
def update_car():
    car_id = int(input("Enter the car ID to update (1-based index): "))
    updated_data = []
    
    with open(DATABASE_FILE, "r") as file:
        lines = file.readlines()
        if 1 <= car_id <= len(lines):
            brand, model, year, price = input("Enter updated brand, model, year, and price separated by commas: ").split(',')
            updated_data.append(brand + "," + model + "," + year + "," + price + "\n")
            lines[car_id - 1] = updated_data[0]
    
    with open(DATABASE_FILE, "w") as file:
        file.writelines(lines)
        print("Car details updated successfully!")

# Function to delete a car from the database
def delete_car():
    car_id = int(input("Enter the car ID to delete (1-based index): "))
    
    with open(DATABASE_FILE, "r") as file:
        lines = file.readlines()
        if 1 <= car_id <= len(lines):
            deleted_car = lines.pop(car_id - 1)
    
    with open(DATABASE_FILE, "w") as file:
        file.writelines(lines)
        print("Car details deleted successfully: " + deleted_car)

# Main program loop
while True:
    print("\nCar Showroom Menu:")
    print("1. Add a car")
    print("2. View cars")
    print("3. Search for cars")
    print("4. Update car details")
    print("5. Delete a car")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_car()
    elif choice == '2':
        view_cars()
    elif choice == '3':
        search_cars()
    elif choice == '4':
        update_car()
    elif choice == '5':
        delete_car()
    elif choice == '6':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
