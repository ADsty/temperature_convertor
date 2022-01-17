import temperature_convertor


def test_celsius_to_fahrenheit_converting():
    celsius_value = 10
    fahrenheit_value = temperature_convertor.celsius_to_fahrenheit(celsius_value)
    assert fahrenheit_value == 50


def test_celsius_to_kelvin_converting():
    celsius_value = 10
    kelvin_value = temperature_convertor.celsius_to_kelvin(celsius_value)
    assert kelvin_value == 283.15


def test_fahrenheit_to_celsius_converting():
    fahrenheit_value = 50
    celsius_value = temperature_convertor.fahrenheit_to_celsius(fahrenheit_value)
    assert celsius_value == 10


def test_fahrenheit_to_kelvin_converting():
    fahrenheit_value = 50
    kelvin_value = temperature_convertor.fahrenheit_to_kelvin(fahrenheit_value)
    assert kelvin_value == 283.15


def test_kelvin_to_celsius_converting():
    kelvin_value = 283.15
    celsius_value = temperature_convertor.kelvin_to_celsius(kelvin_value)
    assert celsius_value == 10


def test_kelvin_to_fahrenheit_converting():
    kelvin_value = 283.15
    fahrenheit_value = temperature_convertor.kelvin_to_fahrenheit(kelvin_value)
    assert fahrenheit_value == 50
