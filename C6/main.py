class Person:
    def __init__(self, name, age="20") -> None:
        self._name = name
        self._age = age

    def info(self):
        print(f"Name: {self._name}, Age: {self._age}")


person = Person("John", 23)
person2 = Person("Jane")

person.info()
person2.info()

print(person._name)
print(person._age)

class Test:
    def __init__(self) -> None:
        self.foo = 11
        self._bar = 23
        self.__baz = 23
    
    @property
    def baz(self):
        return self.__baz
    
    @baz.setter
    def baz_setter(self, value):
        self.__baz = value
    
t = Test()
print(dir(t))
print(t.foo)
print(t._bar)
print(t._Test__baz)
print(t.baz)
t.baz_setter = 100
print(t.baz)