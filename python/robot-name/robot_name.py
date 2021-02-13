from random import choice
from string import ascii_uppercase, digits


class Robot:

    names = []

    def __init__(self):
        self.name = ''
        while True:
            self.name = self.compose_name()
            if self.name not in self.names:
                self.names.append(self.name)
                break

    def compose_name(self):
        return f'{"".join([choice(ascii_uppercase), choice(ascii_uppercase), choice(digits), choice(digits), choice(digits)])}'

    def reset(self):
        self.__init__()
