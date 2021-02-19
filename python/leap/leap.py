def leap_year(year):
    if is_divisible_by(year, 400):
        return True
    elif is_divisible_by(year, 100):
        return False
    elif is_divisible_by(year, 4):
        return True
    else:
        return False


def is_divisible_by(number, amount):
    return number % amount == 0
