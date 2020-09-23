ERROR = 'Error: negative weight.'


def inches_to_millimeters(inches: float):
    """
    Converts inches to millimeters.

    :param inches: any measurement in inches.
    :return: input inches converted to millimeters.
    """
    return inches * 2.54


def celsius_to_fahrenheit(celsius: float):
    """
    Converts celsius to fahrenheit.

    :param celsius: input temperature in celsius.
    :return: temperature in fahrenheit.
    """
    fahrenheit = celsius * 1.8 + 32
    if celsius <= -273.15:
        fahrenheit = '-459.67, absolute zero.'
    else:
        fahrenheit = fahrenheit
    return fahrenheit


def celsius_to_kelvin(celsius: float):
    """
    Converts celsius to kelvin.

    :param celsius: input temperature in celsius.
    :return: temperature in kelvin.
    """
    kelvin = celsius + 273.15
    if celsius <= -273.15:
        kelvin = '0.0, absolute zero.'
    else:
        kelvin = kelvin
    return kelvin


def kelvin_to_celsius(kelvin: float):
    """
    Converts kelvin to celsius.

    :param kelvin: input temperature in kelvin.
    :return: temperature in celsius.
    """
    celsius = kelvin - 273.15
    if kelvin <= 0.0:
        celsius = '-273.15, absolute zero.'
    else:
        celsius = celsius
    return celsius


def kelvin_to_fahrenheit(kelvin: float):
    """
    Converts kelvin to fahrenheit.

    :param kelvin: input temperature in kelvin.
    :return: temperature in fahrenheit.
    """
    fahrenheit = kelvin * (9/5) - 459.67
    if kelvin <= 0.0:
        fahrenheit = '-459.67, absolute zero.'
    else:
        fahrenheit = fahrenheit
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float):
    """
    Converts fahrenheit to celsius.

    :param fahrenheit: input temperature in fahrenheit.
    :return: temperature in celsius.
    """
    celsius = (fahrenheit - 32) / 1.8
    if fahrenheit <= -459.67:
        celsius = '-273.15, absolute zero.'
    else:
        celsius = celsius
    return celsius


def fahrenheit_to_kelvin(fahrenheit: float):
    """
    Converts fahrenheit to kelvin.

    :param fahrenheit: input temperature in fahrenheit.
    :return: temperature in kelvin.
    """
    kelvin = (fahrenheit + 459.67) * (5/9)
    if fahrenheit <= -459.67:
        kelvin = '0.0, absolute zero.'
    else:
        kelvin = kelvin
    return kelvin


def pound_to_gram(pound: float):
    """
    Converts pounds to grams.

    :param pound: input weight in pounds.
    :return: weight in grams.
    """
    gram = pound * 453.59237
    if pound < 0:
        gram = ERROR
    else:
        gram = gram
    return gram


def pound_to_kilogram(pound: float):
    """
    Converts pounds to kilograms.

    :param pound: input weight in pounds.
    :return: weight in kilograms.
    """
    kilogram = pound * 0.45359237
    if pound < 0:
        kilogram = ERROR
    else:
        kilogram = kilogram
    return kilogram


def gram_to_pound(gram: float):
    """
    Converts grams to pounds.
    :param gram: input weight in grams.
    :return: weight in pounds.
    """
    pound = gram / 453.59237
    if gram < 0:
        pound = ERROR
    else:
        pound = pound
    return pound


def gram_to_kilogram(gram: float):
    """
    Converts grams to kilograms.

    :param gram: input weight in grams.
    :return: weight in kilograms.
    """
    kilogram = gram / 1000
    if gram < 0:
        kilogram = ERROR
    else:
        kilogram = kilogram
    return kilogram


def kilogram_to_gram(kilogram: float):
    """
    Converts kilograms to grams.

    :param kilogram: input weight in kilograms.
    :return: weight in grams.
    """
    gram = kilogram * 1000
    if kilogram < 0:
        gram = ERROR
    else:
        gram = gram
    return gram


def kilogram_to_pound(kilogram: float):
    """
    Converts kilograms to pounds.

    :param kilogram: input weight in kilograms.
    :return: weight in pounds.
    """
    pound = kilogram / 0.45359237
    if kilogram < 0:
        pound = ERROR
    else:
        pound = pound
    return pound
