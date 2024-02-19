import unittest
import sys
from io import StringIO
from customer import Customer

PATH = 'customers.json'
PATH_1 = 'customers_modify.json'
PATH_2 = 'customers_example.json'
CUSTOMER = {'first_name': 'Isabella', 'last_name': 'Gomez', 'phone_number': '234-567-8901'}
CUSTOMER_1 = {'first_name': 'Israel', 'last_name': 'Garcia', 'phone_number': '245-567-8451'}
CUSTOMER_2 = {'first_name': 'Sergio', 'last_name': 'Esparza', 'phone_number': '55-33-98-01-18'}
CUSTOMER_3 = {'first_name': 'Selef', 'last_name': 'Garcia', 'phone_number': '55-45-96-54-23'}

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.cust = Customer()

    def test_init_method_raises_typeerror(self):
        self.assertRaises(TypeError, self.cust.__init__, PATH)

    def test_read_file_method_raises_assertionerror_when_data_format_not_correct(self):
        self.assertRaises(AssertionError, self.cust.read_file, 'customers_1.json')

    def test_read_file_method_raises_filenotfounderror(self):
        self.assertRaises(FileNotFoundError, self.cust.read_file, 'customer.json')

    def test_read_file_method_returns_dict(self):
        self.assertIsInstance(self.cust.read_file(PATH), list)

    def test_write_file_method_raises_typeerror_when_receives_no_path(self):
        self.assertRaises(TypeError, self.cust.write_file)

    def test_write_file_method_writes_the_right_format(self):
        sample_data = [CUSTOMER_2, CUSTOMER_3]
        self.cust.create(CUSTOMER_2, PATH_2)
        self.cust.create(CUSTOMER_3, PATH_2)
        self.cust.write_file([CUSTOMER_2, CUSTOMER_3])
        data = self.cust.read_file(PATH_1)
        self.assertEqual(data, sample_data)


    def test_create_method_raises_assertionerror_when_not_receiving_dict(self):
        self.assertRaises(AssertionError, self.cust.create, [], PATH)

    def test_delete_method_raises_assertionerror_when_element_not_in_data(self):
        self.cust.create(CUSTOMER, PATH)
        self.assertRaises(AssertionError, self.cust.delete, CUSTOMER_1)

    def test_display_method_raises_typeerror_when_receives_parameter(self):
        self.cust.create(CUSTOMER, PATH)
        self.assertRaises(TypeError, self.cust.display_info, CUSTOMER_1)

    def test_display_method_prints_the_right_format(self):
        expected_output = [
            "------1------\nfirst_name: Sergio\nlast_name: Esparza\nphone_number: 55-33-98-01-18\n---------------\n\n"
            "------2------\nfirst_name: Selef\nlast_name: Garcia\nphone_number: 55-45-96-54-23\n---------------\n\n"
        ]
        captured_output = StringIO()
        sys.stdout = captured_output
        self.cust.create(CUSTOMER_2, PATH_1)
        self.cust.display_info()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), ''.join(expected_output))

    def test_modify_method_raises_assertionerror_when_customer_not_found(self):
        self.cust.create(CUSTOMER, PATH)
        self.assertRaises(AssertionError, self.cust.modify_info, CUSTOMER_1, 'first_name', 'Omar')

    def test_modify_method_raises_assertionerror_when_feature_not_found(self):
        self.cust.create(CUSTOMER, PATH)
        self.assertRaises(AssertionError, self.cust.modify_info, CUSTOMER, 'name', 'Omar')

if __name__ == '__main__':
    unittest.main()
