def convert(number):
    return f"{sound(number, 3, 'Pling')}{sound(number, 5, 'Plang')}{sound(number, 7, 'Plong')}" or str(number)


def sound(n, k, txt):
    return (n % k == 0) and txt or ''
