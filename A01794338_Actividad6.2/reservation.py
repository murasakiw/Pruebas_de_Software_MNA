"""
Module for managing hotel reservations.

This module provides a class and methods to read and write reservation data
to JSON files, check if a hotel is registered, create reservations, and cancel
existing reservations.

Classes:
    - Reservation: A class for managing hotel reservations.
"""
import json

class Reservation:
    """
    Class that manages hotel reservations.

    Methods:
        - read_file(path): Read data from a JSON file.
        - write_file(data, path): Write data to a JSON file.
        - hotel_is_registered(hotel_name): Check if a hotel is registered.
        - create(hotel_name, customer): Create a new reservation for a hotel.
        - cancel(hotel_name, customer): Cancel an existing reservation for a hotel.
    """
    def __init__(self, path_reservation):
        self.path_reservation = path_reservation

    def read_file(self, path):
        """
        Read data from a JSON file.

        Parameters:
            - path (str): The path to the JSON file.

        Returns:
            dict: Data read from the JSON file.
        """
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        file.close()
        assert isinstance(data, list), 'Data does not have correct format'
        return data

    def write_file(self, data):
        """
        Write data to a JSON file.

        Parameters:
            - data (dict): The data to write to the JSON file.
        """
        with open(self.path_reservation, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        file.close()

    def hotel_is_registered(self, hotel):
        """
        Check if a hotel is registered.

        Parameters:
            - hotel (dict): A dictionary with hotel data.

        Returns:
            tuple: A tuple containing a boolean indicating whether the hotel is registered
                   and the index of the hotel in the list of registered hotels.
        """
        data = self.read_file(self.path_reservation)
        for i, element in enumerate(data):
            if (element['hotel_name'] == hotel['hotel_name'] and
            element['location'] == hotel['location']):
                return (True, i)
        return (False, -1)

    def create(self, hotel, customer):
        """
        Create a new reservation for a hotel.

        Parameters:
            - hotel (dict): A dictionary with hotel data.
            - customer (dict): The customer data for the reservation.

        """
        data_reservation = self.read_file(self.path_reservation)
        hotel_in_list, idx = self.hotel_is_registered(hotel)
        if hotel_in_list and data_reservation[idx].get('reservations') is not None:
            data_reservation[idx]['reservations'] += [customer]
            data_reservation[idx]['rooms'] -= 1
        else:
            data_reservation.append(hotel)
            data_reservation[-1]['reservations'] = [customer]
            data_reservation[-1]['rooms'] -= 1
        self.write_file(data_reservation)

    def cancel(self, hotel, customer):
        """
        Cancel an existing reservation for a hotel.

        Parameters:
            - hotel (dict): A dictionary with hotel data.
            - customer (dict): The customer data of the reservation to cancel.
        """
        data_reservation = self.read_file(self.path_reservation)
        hotel_in_list, idx = self.hotel_is_registered(hotel)
        assert hotel_in_list, 'Hotel not registered'
        data_reservation[idx]['reservations'].remove(customer)
        data_reservation[idx]['rooms'] += 1
        self.write_file(data_reservation)
