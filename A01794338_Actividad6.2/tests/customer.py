"""
Module for managing customer information.

This module provides a class Customer for managing customer data,
including methods for reading and writing data to JSON files,
creating, deleting, displaying, and modifying customer information.

Classes:
    - Customer: A class for managing customer information.
"""
import json


class Customer:
    """
    Class for managing customer information.

    Methods:
        - read_file(path): Read data from a JSON file.
        - write_file(data): Write data to a JSON file.
        - create(new_element, path): Create a new customer and save it to
          a JSON file.
        - delete(element): Delete a customer and save changes to a JSON file.
        - display_info(): Display customers stored information from
          a JSON file.
        - modify_info(customer, feature, new_value): Modify stored information
          for a customer.
    """
    def __init__(self):
        self.path = ''
        self.new_element = {}

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
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        file.close()

    def create(self, new_element, path):
        """
        Create a new customer profile.

        Parameters:
            - new_element (dict): A dictionary with customer data.
            - path (str): The path to the JSON file containing the information.

        """
        assert isinstance(new_element, dict), 'New_element has to be dict'
        self.path = path
        self.new_element = new_element
        list_info = self.read_file(self.path)
        if self.new_element not in list_info:
            list_info.append(self.new_element)
            self.write_file(list_info)

    def delete(self, element):
        """
        Delete a customer and save changes to a JSON file.

        Parameters:
            - element (str): Customer data.
        """
        data = self.read_file(self.path)
        assert element in data, 'Element is not in the list'
        data.remove(element)
        self.write_file(data)

    def display_info(self):
        """
        Display stored information from a JSON file.
        """
        data = self.read_file(self.path)
        for i, element in enumerate(data, start=1):
            print(f'------{i}------')
            for key, value in element.items():
                print(f'{key}: {value}')
            print('-'*15 + '\n')

    def modify_info(self, element, feature, new_value):
        """
        Modify stored information for a customer in a JSON file.

        Parameters:
            - customer (dict): A dictionary with customer info.
            - feature (str): The field of the customer's information to modify.
            - new_value (str,int): The new value for the specified field.
        """
        data = self.read_file(self.path)
        assert element in data, 'Customer not found'
        index = data.index(element)
        assert feature in data[index].keys(), 'Feature not found'
        data[index][feature] = new_value
        self.write_file(data)
