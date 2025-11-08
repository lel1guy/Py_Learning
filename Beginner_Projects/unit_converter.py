# Unit Converter
#goal: Convert messsearmentes from one type to another
#steps: 1.Great User
#       2. Can handle multiple measurement types 
#       4. Have a menu

def main():
    print("=" * 50)
    print("Welcome to the Unit Converter!")
    print("=" * 50)
    print("This will take care of the conversian between different units of mesurment")
    print("=" * 50)
    print()

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 1:
            print("Lenght Conversion Chossen")
            #todo: Implement length Conversion
        elif choice == 2:
            print("Temperature Conversion Chossen")
            #todo: Implement Temperature Conversion
        elif choice == 3:
            print("Volume Conversion Chossen")
            #todo: Implement Volume Conversion
        elif choice == 4:
            print("Weight Conversion Chossen")
            #todo: Implement Weight Conversion
        elif choice == 5:
            print("GoodBye! Hope to see you next time!")
        
        print()
    
def show_menu():
    print("Select which conversion type you want!")
    print("1. Length (inches, feet, meters, etc.)")
    print("2. Weight (pounds, kilograms, ounces, etc.)")
    print("3. Temperature (Fahrenheit, Celsius, Kelvin)")
    print("4. Volume (gallons, liters, cups, etc.)")
    print("5. Quit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def validate_numeric_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be greater than or equal to {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print("Value must be less than or equal to {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
def get_conversion_value():
    return validate_numeric_input("Enter the conversion value: ")

def get_unit_selection(units, direction):
    while True:
        try:
            choice = int(input(f"Select unit to convert {direction} (1-{len(units)}): "))
            if 1 <= choice <= len(units):
                return choice
            else:
                print(f"Please enter a number between 1 and {len(units)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def convert_length(value, from_unit, to_unit):
    to_meters = {
        "inches": 0.0254,
        "feet": 0.3048,
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "yards": 0.9144,
        "miles": 1609.34,
        "kilometers": 1000,
    }

    meters + value * to_meters{from_unit}

    from_meters = {
        "inches": 1/0.0254,
        "feet": 1/0.3048,
        "meters": 1,
        "centimeters": 100,
        "millimeters": 1000,
        "yards": 1/0.9144,
        "miles": 1/1609.34,
        "kilometers": 1/1000,
    }

    return_meter * from_meters[to_unit]
def lenght_conversion():
    print("Lenght Conversion Chossen")
    units = ["inches", "feet", "meters", "centimeters", "millimeters", "yards", "miles", "kilometers"]
    print()
    for i, unit in enumerate(units, 1):
        print(f"{i}. {unit.capitalize()}")

        value = get_conversion_value()

        from_choice = get_unit_selection(units, "from")
        to_choice = get_unit_selection(units, "to")

        from_unit = units[from_choice - 1]
        to_unit = units[to_choice - 1]

        result = convert_length(value, from_unit, to_unit)

        print()
        print(f"{value} {from_unit(s).capitalize() = {results: .4f} {to_unit(s).capitalize()}}")
        print(f"Rounded: {result: .2f} {to_unit(s)}")




if __name__ == "__main__":
    main()