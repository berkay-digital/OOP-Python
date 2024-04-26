from unittest import TestCase
from C9.employee import Employee


class TestEmployee(TestCase):
    def setUp(self):
        self.emp1 = Employee('John', 'Doe', 50000)
        self.emp2 = Employee('Jane', 'Doe', 60000)
        self.emp3 = Employee('Jim', 'Doe', 70000)
        self.emp4 = Employee('', 'Doe', 50000)
        self.emp5 = Employee('John', '', 50000)
        self.emp6 = Employee('John', 'Doe', 0)
        self.emp7 = Employee('John', 'Doe', -50000)

    def test_email_after_name_change(self):
        self.emp1.first = 'Jane'
        self.assertEqual(self.emp1.email, 'Doe.Jane@email.com')

    def test_fullname_after_name_change(self):
        self.emp2.first = 'Janet'
        self.assertEqual(self.emp2.fullname, 'Janet Doe')

    def test_apply_raise_effect(self):
        self.emp3.apply_raise()
        self.assertEqual(self.emp3.pay, 70001)

    def test_apply_cut_effect(self):
        self.emp1.apply_cut()
        self.assertEqual(self.emp1.pay, 47500)

    def test_email_with_empty_first_name(self):
        self.assertEqual(self.emp4.email, 'Doe.@email.com')

    def test_fullname_with_empty_last_name(self):
        self.assertEqual(self.emp5.fullname, 'John ')

    def test_apply_raise_on_zero_pay(self):
        self.emp6.apply_raise()
        self.assertEqual(self.emp6.pay, 1)

    def test_apply_cut_on_negative_pay(self):
        self.emp7.apply_cut()
        self.assertEqual(self.emp7.pay, -47500)