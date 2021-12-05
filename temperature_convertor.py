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
