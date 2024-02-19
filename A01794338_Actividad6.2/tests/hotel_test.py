import unittest
import sys
from io import StringIO
from hotel import Hotel

PATH = 'hotels.json'
PATH_C = 'customers.json'
PATH_1 = 'hotels_modify.json'
PATH_2 = 'hotels_example.json'
CUSTOMER = {'first_name': 'Isabella', 'last_name': 'Gomez', 'phone_number': '234-567-8901'}
HOTEL = {'hotel_name': 'Sheraton', 'location': 'New York', 'rooms': 84}
CUSTOMER_1 = {'first_name': 'Israel', 'last_name': 'Garcia', 'phone_number': '245-567-8451'}
CUSTOMER_2 = {'first_name': 'Sergio', 'last_name': 'Esparza', 'phone_number': '55-33-98-01-18'}
HOTEL_2 = {'hotel_name': 'Ritz-Carlton', 'location': 'Madrid', 'rooms': 72}
HOTEL_3 = {'hotel_name': 'Hilton', 'location': 'Mexico City', 'rooms': 115}

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.new_hotel = Hotel()

    def test_init_method_raises_typeerror(self):
        self.assertRaises(TypeError, self.new_hotel.__init__, PATH)

    def test_read_file_method_raises_assertionerror_when_data_format_not_correct(self):
        self.assertRaises(AssertionError, self.new_hotel.read_file, 'hotels_1.json')

    def test_read_file_method_raises_filenotfounderror(self):
        self.assertRaises(FileNotFoundError, self.new_hotel.read_file, 'hotel.json')

    def test_read_file_method_returns_dict(self):
        self.assertIsInstance(self.new_hotel.read_file(PATH), list)

    def test_write_file_method_raises_typeerror_when_receives_no_path(self):
        self.assertRaises(TypeError, self.new_hotel.write_file)

    def test_write_file_method_writes_the_right_format(self):
        sample_data = [HOTEL_2, HOTEL_3]
        self.new_hotel.create(HOTEL_2, PATH_2)
        self.new_hotel.create(HOTEL_3, PATH_2)
        self.new_hotel.write_file([HOTEL_2, HOTEL_3])
        data = self.new_hotel.read_file(PATH_1)
        self.assertEqual(data, sample_data)


    def test_create_method_raises_assertionerror_when_not_receiving_dict(self):
        self.assertRaises(AssertionError, self.new_hotel.create, [], PATH)

    def test_delete_method_raises_assertionerror_when_element_not_in_data(self):
        self.new_hotel.create(HOTEL, PATH)
        self.assertRaises(AssertionError, self.new_hotel.delete, CUSTOMER_1)

    def test_display_method_raises_typeerror_when_receives_parameter(self):
        self.new_hotel.create(HOTEL, PATH)
        self.assertRaises(TypeError, self.new_hotel.display_info, CUSTOMER_1)

    def test_display_method_prints_the_right_format(self):
        expected_output = [
            "------1------\nhotel_name: Ritz-Carlton\nlocation: Madrid\nrooms: 72\n---------------\n\n"
            "------2------\nhotel_name: Hilton\nlocation: Mexico City\nrooms: 115\n---------------\n\n"
        ]
        captured_output = StringIO()
        sys.stdout = captured_output
        self.new_hotel.create(HOTEL_2, PATH_1)
        self.new_hotel.display_info()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), ''.join(expected_output))

    def test_modify_method_raises_assertionerror_when_customer_not_found(self):
        self.new_hotel.create(HOTEL, PATH)
        self.assertRaises(AssertionError, self.new_hotel.modify_info, HOTEL_2, 'hotel_name', 'Hilton')

    def test_modify_method_raises_assertionerror_when_feature_not_found(self):
        self.new_hotel.create(HOTEL, PATH)
        self.assertRaises(AssertionError, self.new_hotel.modify_info, HOTEL, 'hotel', 'Hilton')

    def test_reserve_room_method_raises_assertionerror_when_hotel_not_registered(self):
        self.new_hotel.create(HOTEL, PATH)
        self.assertRaises(AssertionError, self.new_hotel.reserve_room, HOTEL_3)

    def test_reserve_room_method_raises_assertionerror_when_no_rooms(self):
        self.new_hotel.create(HOTEL, PATH)
        self.new_hotel.modify_info(HOTEL, 'rooms', 0)
        self.assertRaises(AssertionError, self.new_hotel.reserve_room, HOTEL)

    def test_cancel_reservation_method_raises_assertionerror_when_hotel_not_registered(self):
        self.new_hotel.create(HOTEL, PATH)
        self.assertRaises(AssertionError, self.new_hotel.cancel_reservation, HOTEL_3)

    def test_modify_calling_father_customer_class_raises_assertionerror_customer_not_found(self):
        self.new_hotel.create(CUSTOMER, PATH_C)
        with self.assertRaises(AssertionError):
            super(Hotel, self.new_hotel).modify_info(CUSTOMER_1, 'first_name', 'Omar')

    def test_modify_calling_father_customer_class_raises_assertionerror_feature_not_found(self):
        self.new_hotel.create(CUSTOMER, PATH_C)
        with self.assertRaises(AssertionError):
            super(Hotel, self.new_hotel).modify_info(CUSTOMER_2, 'name', 'Omar')

if __name__ == '__main__':
    unittest.main()
