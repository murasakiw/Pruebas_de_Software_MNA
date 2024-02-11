"""
A program to calculate total sales from JSON files and write the results
to a text file.

This program reads data from two JSON files: one containing available
products in a store and the other containing the sales of that store.
It calculates the total sales for each product and writes the results
to a text file.
"""
import sys
import time
import json


def read_json(file_name):
    """
    Read data from a JSON file and return a list of dictionaries.

    Parameters:
        file_path (str): The path to the JSON file to be read.

    Returns:
        list: A list of dictionaries containing the data from the JSON file.
    """
    with open(file_name, 'r', encoding='utf-8') as opened_file:
        datum = json.load(opened_file)
    opened_file.close()
    return datum


def get_prices_dict(price_datum):
    """
    Create a dictionary with product names as keys and prices as values.

    Parameters:
        price_datum (list): A list of dictionaries.

    Returns:
        dict: A dictionary where the keys are product names
              and the values are their prices.
    """
    prices_dictionary = {}
    for dictionary in price_datum:
        prices_dictionary[dictionary['title']] = dictionary['price']
    return prices_dictionary


def get_sales_dict(sales_datum, prices_dictionary):
    """
    Calculate the total sales for each product and return a dictionary.

    This function takes a list of dictionaries containing sales datum,
    where each dictionary represents a sale with product names and
    quantities sold. It also takes a dictionary with the prices of
    each product. It calculates the total sales for each product and
    returns a dictionary where the keys are product names and the values
    are the total sales for each product.

    Parameters:
        sales_datum (list): A list of dictionaries containing sales data.
        prices_dictionary (dict): A dictionary containing prices data.

    Returns:
        sales_dict (dict): A dictionary where the keys are
        product names and the values are the
        total quantities sold of each product.
    """
    sales_dict = {}
    for key in prices_dictionary.keys():
        sales_count = 0
        for sale in sales_datum:
            if sale['Product'] == key:
                sales_count += sale['Quantity']
        sales_dict[key] = sales_count
    return sales_dict


def get_total_sales_dict(prices_dictionary, sales_dict):
    """
    Calculate the revenue generated from the sales of each product.

    This function takes a dictionary of product prices and a
    dictionary of quantities sold per product. It calculates
    the revenue generated from the sales of each product
    by multiplying the price of each product by the quantity
    sold. It returns a dictionary where the keys are product
    names and the values are the revenue generated from the
    sales of each product.

    Parameters:
        prices_dictionary (dict): A dictionary where the keys are product
                                  names and the values are the prices
                                  of each product.
        sales_dict (dict): A dictionary where the keys are product names
                           and the values are the quantities sold per
                           product.

    Returns:
        total_sales_dict (dict): A dictionary where the keys are product names
                                and the values are the revenue generated
                                from the sales of each product.
    """
    total_sales_dict = {}
    for key in prices_dictionary.keys():
        item_total_sale = prices_dictionary[key]*sales_dict[key]
        total_sales_dict[key] = round(item_total_sale, 2)
    return total_sales_dict


def format_results(total_sales_dict, prices_dictionary, results_list):
    """
    Format the results obtained by the program.

    This function takes the dictionary of total sales, the prices
    dictionary, a list with the total sales results summing all
    products, the execution time of the program, and the file name
    that was read to calculate the sales. It formats these data
    into a string and returns it.

    Parameters:
        total_sales_dict (dict): A dictionary containing the total
                                 sales for each product.
        prices_dictionary (dict): A dictionary containing the prices
                                  of each product.
        total_sales (float): A float containing the total sales
                             summing all products.
        elapsed_time (float): The execution time of the program.
        file_name (str): The name of the file that was read to
                         calculate the sales.

    Returns:
        results (str): A formatted string containing the results.
    """
    results = 'Item'.center(40) + 'Price'.ljust(10) + 'Sales'.ljust(10)+'\n\n'
    for key, value in total_sales_dict.items():
        results += (
            f'{key}'.ljust(40, '-') +
            f'${prices_dictionary[key]}'.ljust(10, '-') +
            f'${value}'.ljust(10) + '\n'
        )
    results += (
        '\n' + 'Total sales'.ljust(50, '-') +
        f'${results_list[0]}' + '\n\n'
    )
    results += (
        f'Execution time for file {results_list[2]}: '
        f'{results_list[1]} seconds\n\n'
    )
    results += '*'*60 + '\n\n'
    return results


def write_results_file(results, results_file):
    """
    Write formatted results to a text file.

    This function takes a string with the formatted results and a filename.
    It writes the results to a text file with the given filename.

    Parameters:
        results (str): A string containing the formatted results.
        results_file (str): The name of the file to write the results to.

    Returns:
        None
    """
    with open(results_file, 'a', encoding='utf-8') as txt_file:
        txt_file.write(results)
    txt_file.close()


def main():
    """
    Main function of the program.

    This function is the main entry point of the program.
    It performs the necessary operations to execute the program
    and coordinate different functionalities.

    Parameters:
    None.

    Returns:
    None.
    """
    start_time = time.time()
    prices_file = sys.argv[1]
    sales_file = sys.argv[2]
    results_file = 'SalesResults.txt'

    price_datum = read_json(prices_file)
    sales_datum = read_json(sales_file)

    prices_dictionary = get_prices_dict(price_datum)
    sales_dict = get_sales_dict(sales_datum, prices_dictionary)
    total_sales_dict = get_total_sales_dict(prices_dictionary, sales_dict)
    total_sales = round(sum(total_sales_dict.values()), 2)
    end_time = time.time()
    elapsed_time = end_time - start_time
    results_list = [total_sales, elapsed_time, sales_file]
    results = format_results(total_sales_dict, prices_dictionary, results_list)
    print(results)
    write_results_file(results, results_file)


if __name__ == '__main__':
    main()
