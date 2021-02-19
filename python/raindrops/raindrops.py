drops = {
    "Pling": 3,
    "Plang": 5,
    "Plong": 7,
}


def convert(number):
    sounds = "".join(sound(number, drops.get(k), k) for k, v in drops.items())
    return sounds or str(number)


def sound(n, k, txt):
    return (n % k == 0) and txt or ""
