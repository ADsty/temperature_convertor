def celsius_to_fahrenheit(value):
    fahrenheit = (value * 9 / 5) + 32
    return fahrenheit


def celsius_to_kelvin(value):
    kelvin = value + 273.15
    return kelvin


def fahrenheit_to_celsius(value):
    celsius = (value - 32) * 5 / 9
    return celsius


def fahrenheit_to_kelvin(value):
    kelvin = (value - 32) * 5 / 9 + 273.15
    return kelvin


def kelvin_to_celsius(value):
    celsius = value - 273.15
    return celsius


def kelvin_to_fahrenheit(value):
    fahrenheit = (value - 273.15) * 9 / 5 + 32
    return fahrenheit


print("Temperature convertor v1.0")
print("To convert temperature type: [value] [initial temperature unit] [needed temperature unit]")
print("To stop the program type 'quit' ")
print("Maintained temperature units are: Kelvin (type as K), Celsius (type as C), Fahrenheit (type as F)")


while True:
    input_string = input("Type what do you want: ").strip()
    parsed_string = input_string.split(" ")

    if input_string == "quit":
        print("Program was closed")
        break

    if len(input_string) == 0 or len(parsed_string) != 3:
        print("Your input is not valid, required format : [value] [initial temperature unit] [needed temperature unit]")
        print("Maintained temperature units are: Kelvin (type as K), Celsius (type as C), Fahrenheit (type as F)")
        continue

    value = int(parsed_string[0])
    initial_unit = parsed_string[1]
    needed_unit = parsed_string[2]

    if initial_unit == "C":
        if needed_unit == "F":
            print("Your result is", celsius_to_fahrenheit(value), "F")
        elif needed_unit == "K":
            print("Your result is", celsius_to_kelvin(value), "K")
        else:
            print("Your needed temperature unit is not valid")
            print("Maintained temperature units are: Kelvin (type as K), Celsius (type as C), Fahrenheit (type as F)")

    elif initial_unit == "F":
        if needed_unit == "C":
            print("Your result is", fahrenheit_to_celsius(value), "C")
        elif needed_unit == "K":
            print("Your result is", fahrenheit_to_kelvin(value), "K")
        else:
            print("Your needed temperature unit is not valid")
            print("Maintained temperature units are: Kelvin (type as K), Celsius (type as C), Fahrenheit (type as F)")

    elif initial_unit == "K":
        if needed_unit == "C":
            print("Your result is", kelvin_to_celsius(value), "C")
        elif needed_unit == "F":
            print("Your result is", kelvin_to_fahrenheit(value), "F")
        else:
            print("Your needed temperature unit is not valid")
            print("Maintained temperature units are: Kelvin (type as K), Celsius (type as C), Fahrenheit (type as F)")

    else:
        print("Your initial temperature unit is not valid")
        print("Maintained temperature units are: Kelvin (type as K), Celsius (type as C), Fahrenheit (type as F)")
