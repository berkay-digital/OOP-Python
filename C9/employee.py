class Employee:
    """A sample Employee class"""

    raise_amt = 1.05
    cut_amt = 0.95

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.last, self.first)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    def apply_cut(self):
        self.pay = int(self.pay * self.cut_amt)