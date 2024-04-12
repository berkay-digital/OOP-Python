import random


class Employee:
    def __init__(self, name, salary, age, job):
        self.name = name
        self.salary = salary
        self.job = job
        self.age = age
        self.email = f"{self.name.lower()}@company.com"
        self._company = "E-Corp"
        self.__uid = random.randint(1000, 9999)

    def __str__(self):
        return f"{self.name} is a {self.job} and earns {self.salary} per year"

    @property
    def email(self):
        return f"{self.name.lower()}@company.com"

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def age(self):
        if 18 < self._age < 99:
            return self._age
        else:
            raise ValueError("Age must be between 18 and 99")

    @age.setter
    def age(self, value):
        if 18 < value < 99:
            self._age = value
        else:
            raise ValueError("Age must be between 18 and 99")

    @property
    def salary(self):
        if self._salary > 1500:
            return self._salary
        else:
            raise ValueError("Salary must be higher than minimum wage")

    @salary.setter
    def salary(self, value):
        if value > 1500:
            self._salary = value
        else:
            raise ValueError("Salary must be higher than minimum wage")

    @property
    def job(self):
        if type(self._job) is str:
            return self._job
        else:
            raise ValueError("Job must be a string")

    @job.setter
    def job(self, value):
        if type(value) is str:
            self._job = value
        else:
            raise ValueError("Job must be a string")

    def change_company(self, company):
        self._company = company

    def check_uid(self):
        return self.__uidc


class Manager(Employee):
    def __init__(self, name, salary, age, job, team):
        super().__init__(name, salary, age, job)
        self.team = team

    def __str__(self):
        return f"{self.name} is a {self.job} and earns {self.salary} per year and manages {self.team} in {self._company}"

    def add_member(self, member):
        self.team.append(member)

    def remove_member(self, member):
        self.team.remove(member)

    def check_uid(self):
        return self._Employee__uid


employee = Employee("John", 2500, 23, "Developer")
print(employee)
employee.salary = 2000
print(employee)
employee.job = "Engineer"
print(employee)
print(employee.email)
print(employee.age)

manager = Manager("Jane", 3500, 30, "Manager", ["John", "Alice"])
print(manager)
manager.add_member("Bob")
print(manager)
manager.remove_member("Alice")
print(manager)
print(manager.check_uid())
