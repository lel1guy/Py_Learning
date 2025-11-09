#!/usr/bin/env python3
"""
Unit Converter: A program to convert between different units of measurement.
This script allows users to convert length, weight, temperature, and volume.
It features a user-friendly menu, input validation, and a conversion history.
"""

# Global list to store the history of conversions
conversion_history = []

def main():
    """Main function to run the unit converter application."""
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
            length_conversion()
        elif choice == 2:
            weight_conversion()
        elif choice == 3:
            temperature_conversion()
        elif choice == 4:
            volume_conversion()
        elif choice == 5:
            show_history()
        elif choice == 6:
            print("GoodBye! Hope to see you next time!")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")
        
        print()
    
def show_menu():
    """Displays the main menu of conversion options to the user."""
    print("Select which conversion type you want!")
    print("1. Length (inches, feet, meters, etc.)")
    print("2. Weight (pounds, kilograms, ounces, etc.)")
    print("3. Temperature (Fahrenheit, Celsius, Kelvin)")
    print("4. Volume (gallons, liters, cups, etc.)")
    print("5. View History")
    print("6. Quit")

def get_user_choice():
    """Gets and validates the user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def validate_numeric_input(prompt, min_value=None, max_value=None):
    """Prompts the user for a numeric value and validates it."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be greater than or equal to {min_value}.")
                continue
            if max_value is not None and value > max_value:
                # Corrected f-string for max_value
                print(f"Value must be less than or equal to {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
def get_conversion_value():
    return validate_numeric_input("Enter the conversion value: ")

def get_unit_selection(units, direction):
    """Gets and validates the user's choice for a unit from a list."""
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
    """Converts a value from one length unit to another using meters as a base."""
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

    # Convert the input value to the base unit (meters)
    meters = value * to_meters[from_unit]

    # Create the 'from_meters' dictionary dynamically to avoid precision errors
    from_meters = {
        unit: 1 / factor for unit, factor in to_meters.items()
    }

    # Convert from meters to the target unit
    return meters * from_meters[to_unit]

def length_conversion():
    """Handles the user interaction for length conversion."""
    print("\n--- Length Conversion ---")
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
    # Corrected f-string for displaying the result
    print(f"{value} {from_unit}(s) = {result:.4f} {to_unit}(s)")
    print(f"Rounded: {result:.2f} {to_unit}(s)")

    add_to_history("Length", value, from_unit, result, to_unit)

def convert_weight(value, from_unit, to_unit):
    """Converts a value from one weight unit to another using kilograms as a base."""
    to_kilograms = {
        "pounds": 0.453592,
        "kilograms": 1,
        "ounces": 0.0283495,
        "grams": 0.001,
        "milligrams": 0.000001,
        "tonnes": 1000,
        "stones": 6.35029,
    }

    kilograms = value * to_kilograms[from_unit]

    # Create the 'from_kilograms' dictionary dynamically
    from_kilograms = {
        unit: 1 / factor for unit, factor in to_kilograms.items()
    }

    return kilograms * from_kilograms[to_unit]

def weight_conversion():
    """Handles the user interaction for weight conversion."""
    print("\n--- Weight Conversion ---")
    print("Available Units:")
    units = ["pounds", "kilograms", "ounces", "grams", "milligrams", "tonnes", "stones"]
    for i, unit in enumerate(units, 1):
        print(f"{i}. {unit.capitalize()}")

    value = get_conversion_value()

    from_choice = get_unit_selection(units, "from")
    to_choice = get_unit_selection(units, "to")

    from_unit = units[from_choice - 1]
    to_unit = units[to_choice - 1]

    result = convert_weight(value, from_unit, to_unit)

    print(f"\n{value} {from_unit}(s) = {result:.4f} {to_unit}(s)")
    print(f"Rounded: {result:.2f} {to_unit}(s)")

    add_to_history("Weight", value, from_unit, result, to_unit)

def convert_temperature(value, from_unit, to_unit):
    """Converts a value from one temperature unit to another using Celsius as a base."""
    # Check for physically impossible temperatures
    if (from_unit == "celsius" and value < -273.15) or \
       (from_unit == "fahrenheit" and value < -459.67) or \
       (from_unit == "kelvin" and value < 0):
        print("Warning: Temperature is below absolute zero!")
        return None

    # Convert input to Celsius
    celsius = 0
    if from_unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'celsius':
        celsius = value
    elif from_unit == 'kelvin':
        celsius = value - 273.15

    # Convert from Celsius to the target unit
    if to_unit == 'fahrenheit':
        return celsius * 9/5 + 32
    elif to_unit == 'celsius':
        return celsius
    elif to_unit == 'kelvin':
        return celsius + 273.15
    return None

def temperature_conversion():
    """Handles the user interaction for temperature conversion."""
    print("\n--- Temperature Conversion ---")
    units = ["celsius", "fahrenheit", "kelvin"]
    for i, unit in enumerate(units, 1):
        print(f"{i}. {unit.capitalize()}")

    value = validate_numeric_input("Enter the temperature value: ")

    from_choice = get_unit_selection(units, "from")
    to_choice = get_unit_selection(units, "to")

    from_unit = units[from_choice - 1]
    to_unit = units[to_choice - 1]

    result = convert_temperature(value, from_unit, to_unit)

    if result is not None:
        print(f"\n{value}°{from_unit[0].upper()} = {result:.2f}°{to_unit[0].upper()}")
        add_to_history("Temperature", value, from_unit, result, to_unit)

def convert_volume(value, from_unit, to_unit):
    """Converts a value from one volume unit to another using liters as a base."""
    to_liters = {
        "liters": 1,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.24, # US cup
    }

    liters = value * to_liters[from_unit]

    from_liters = {
        unit: 1 / factor for unit, factor in to_liters.items()
    }

    return liters * from_liters[to_unit]

def volume_conversion():
    """Handles the user interaction for volume conversion."""
    print("\n--- Volume Conversion ---")
    units = ["liters", "milliliters", "gallons", "quarts", "pints", "cups"]
    for i, unit in enumerate(units, 1):
        print(f"{i}. {unit.capitalize()}")

    value = get_conversion_value()

    from_choice = get_unit_selection(units, "from")
    to_choice = get_unit_selection(units, "to")

    from_unit = units[from_choice - 1]
    to_unit = units[to_choice - 1]

    result = convert_volume(value, from_unit, to_unit)

    print(f"\n{value} {from_unit}(s) = {result:.4f} {to_unit}(s)")
    print(f"Rounded: {result:.2f} {to_unit}(s)")

    add_to_history("Volume", value, from_unit, result, to_unit)

def add_to_history(conv_type, from_val, from_u, to_val, to_u):
    """Adds a completed conversion to the history list."""
    conversion_history.append({
        "type": conv_type,
        "from_value": from_val,
        "from_unit": from_u,
        "to_value": to_val,
        "to_unit": to_u,
    })

def show_history():
    """Displays the last 10 conversions from the history."""
    print("\n--- Conversion History ---")
    if not conversion_history:
        print("No conversions have been performed yet.")
        return

    # Display the last 10 items in reverse order (most recent first)
    for i, entry in enumerate(reversed(conversion_history[-10:]), 1):
        print(f"{i}. {entry['type']}: {entry['from_value']} {entry['from_unit']} -> {entry['to_value']:.2f} {entry['to_unit']}")

if __name__ == "__main__":
    main()