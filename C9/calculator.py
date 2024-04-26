class Calculator:
    """ A simple calculator App"""
    def add(self, x, y):
        return x + y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    def average(self, x, y):
        return self.add(x, y) / 2

    def calculate_c_in_triangle(self, a, b):
        """ Use Pythagoras theorem """
        return (a ** 2 + b ** 2) ** 0.5

    def calculate_zero_of_the_parabolic_function(self, a, b, c):
        """ Use the quadratic formula """
        return (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
