"""
Module for managing hotel information.

This module provides a class Hotel inheriting
from Customer, which includes methods for
managing hotel-specific operations such as
checking if a hotel is registered, modifying
stored information, making room reservations,
and canceling reservations.

Classes:
    - Hotel: A class for managing hotel information, inheriting from Customer.
"""
from customer import Customer


class Hotel(Customer):
    """
    Class for managing hotel information, inheriting from Customer.

    Inherits from:
        Customer: A class for managing customer information.

    Methods:
        - hotel_is_registered(hotel_name): Check if a hotel is registered.
        - modify_info(hotel, feature, new_value): Modify stored information
          in a JSON file.
        - reserve_room(hotel): Reserve a room in a hotel.
        - cancel_reservation(hotel): Cancel a reservation in a hotel.
    """
    def __init__(self):
        super(Customer, self).__init__()
        self.path = ''
        self.new_element = {}

    def hotel_is_registered(self, hotel):
        """
        Check if a hotel is registered.

        Parameters:
            - hotel (dict): A dictionary with hotel data.

        Returns:
            tuple: A tuple containing a boolean indicating whether the
            hotel is registered and the index of the hotel in the list
            of registered hotels.
        """
        data = self.read_file(self.path)
        for i, element in enumerate(data):
            if (element['hotel_name'] == hotel['hotel_name'] and
                    element['location'] == hotel['location']):
                return (True, i)
        return (False, -1)

    def modify_info(self, element, feature, new_value):
        """
        Modify stored information for a customer in a JSON file.

        Parameters:
            - customer (dict): A dictionary with customer info.
            - feature (str): The field of the customer's information to modify.
            - new_value (str,int): The new value for the specified field.
        """
        data = self.read_file(self.path)
        hotel_in_list, idx = self.hotel_is_registered(element)
        assert hotel_in_list, 'Hotel is not registered'
        assert feature in data[idx].keys(), 'Feature not found'
        data[idx][feature] = new_value
        self.write_file(data)

    def reserve_room(self, hotel):
        """
        Make a reservation at a hotel.

        This method makes a reservation at a hotel based on the provided
        hotel information.

        Parameters:
            - hotel (dict): A dictionary containing the information
             of the hotel.
        """
        data = self.read_file(self.path)
        hotel_in_list, idx = self.hotel_is_registered(hotel)
        assert hotel_in_list, 'Hotel is not registered'
        assert data[idx]['rooms'] >= 1, 'No rooms available'
        data[idx]['rooms'] -= 1
        self.write_file(data)

    def cancel_reservation(self, hotel):
        """
        Cancel a reservation at a hotel.

        This method cancels a reservation at a hotel based on the provided
        hotel information.

        Parameters:
            - hotel (dict): A dictionary containing the information
            of the hotel.
        """
        data = self.read_file(self.path)
        hotel_in_list, idx = self.hotel_is_registered(hotel)
        assert hotel_in_list, 'Hotel not registered'
        data[idx]['rooms'] += 1
        self.write_file(data)
