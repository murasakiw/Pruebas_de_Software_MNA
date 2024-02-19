import unittest
from reservation import Reservation

PATH = 'reservations.json'
PATH_1 = 'test_reservation.json'
PATH_2 = 'expected_reservation.json'
PATH_3 = 'test_reservation_1.json'
PATH_4 = 'expected_reservation_1.json'
HOTEL_1 = {'hotel_name': 'Sheraton','location': 'New York','rooms': 85,'reservations': []}
HOTEL_2 = {'hotel_name': 'InterContinental','location': 'London','rooms': 57}
HOTEL_3 = {'hotel_name': 'Westin', 'location': 'Los Angeles', 'rooms': 104}
CUSTOMER = {'first_name': 'Isabella', 'last_name': 'Gomez', 'phone_number': '234-567-8901'}
CUSTOMER_1 = {'first_name': 'Omar', 'last_name': 'Esparza', 'phone_number': '55-33-98-01-18'}
CUSTOMER_2 = {'first_name': 'Israel', 'last_name': 'Garcia', 'phone_number': '245-567-8451'}

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.new_reservation = Reservation(PATH)

    def test_init_method_raises_typeerror(self):
        self.assertRaises(TypeError, self.new_reservation.__init__)

    def test_read_file_method_returns_dict(self):
        self.assertIsInstance(self.new_reservation.read_file(PATH), list)

    def test_read_file_method_raises_assertionerror_when_data_format_not_correct(self):
        self.assertRaises(AssertionError, self.new_reservation.read_file, 'customers_1.json')

    def test_read_file_method_raises_filenotfounderror(self):
        self.assertRaises(FileNotFoundError, self.new_reservation.read_file, 'reserv.json')

    def test_registered_method_returns_True_if_hotel_exists(self):
        self.assertEqual(True, self.new_reservation.hotel_is_registered(HOTEL_1)[0])

    def test_registered_method_returns_False_if_hotel_does_not_exists(self):
        self.assertEqual(False, self.new_reservation.hotel_is_registered(HOTEL_3)[0])

    def test_cancel_method_raises_assertionerror_if_hotel_does_not_exists(self):
        self.assertRaises(AssertionError, self.new_reservation.cancel, HOTEL_3, CUSTOMER)

    def test_create_method_creates_reservation_succesfully(self):
        new_reservation_1 = Reservation(PATH_1)
        new_reservation_1.create(HOTEL_1, CUSTOMER_1)
        data = new_reservation_1.read_file(PATH_1)
        expected_data = new_reservation_1.read_file(PATH_2)
        self.assertEqual(data, expected_data)
    
    def test_create_method_creates_reservation_succesfully_when_hotel_not_in_list(self):
        new_reservation_2 = Reservation(PATH_3)
        new_reservation_2.create(HOTEL_2, CUSTOMER_2)
        data = new_reservation_2.read_file(PATH_3)
        expected_data = new_reservation_2.read_file(PATH_4)
        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()