def classify(number):
    if number <= 0:
        raise ValueError(".+")

    if (sum_factors := sum(factors(number))) == number:
        return "perfect"
    elif sum_factors > number:
        return "abundant"
    else:
        return "deficient"


def factors(n):
    return [x for x in range(1, n) if n % x == 0]
