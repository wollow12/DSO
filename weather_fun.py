import csv
import config
import requests


def country_code_to_country_name(country_code):
    """Opens csv file with country codes and names
    to translate code to country name by checking if
    code exists in the list, if exists returns country
    name and if not returns country code"""
    rows = []
    with open("./static/countries.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
            if row[0] == country_code and not row[1] == "":
                return row[1]
        return country_code


def legal_search_word(word):
    """Checks if each char in city name is number
    or alphabet letter to check if the input is legal"""
    for index, char in enumerate(word):
        if not char.isnumeric() and not char.isalpha():
            # if name doesn't start with space
            if char == ' ' and index != 0:
                continue
            return False
    return True


def take_data(api_city):
    """Takes specific data , for next 7 days in specific city
    from the api using the api key from config.py and returns
    list of usable information"""
    apikey = config.api_key
    url = f'https://api.weatherbit.io/v2.0/forecast/daily?city={api_city}&days=7&key={apikey}'
    try:
        res = requests.get(url)
        print(res.status_code)
    except requests.exceptions.ConnectionError:
        return "api_error"
    # if city not found
    if res.status_code == 204:
        return None
    # if status is not successful
    elif res.status_code not in range(200, 300):
        return "api_error"
    # no errors found
    data = res.json()
    return data


def api_data_to_needed_lists(api_data):
    """Creates a dictionary with lists containing max temp,min temp,humidity,
    date,icon code for each day for next 7 days"""
    max_temp = []
    min_temp = []
    humidity_list = []
    date_list = []
    icon_list = []
    for api_index in range(7):
        humidity_list.append(api_data['data'][api_index]['rh'])
        max_temp.append(api_data['data'][api_index]['high_temp'])
        min_temp.append(api_data['data'][api_index]['low_temp'])
        date_list.append(api_data['data'][api_index]['valid_date'])
        icon_list.append(api_data['data'][api_index]['weather']['icon'])
    return {
        "humidity": humidity_list,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "country": country_code_to_country_name(api_data['country_code']),
        "city": api_data['city_name'],
        "valid_date": date_list,
        "icons": icon_list
    }


def error_checking(city_name):
    """Checks if the input from search bar is empty,illegal
    or city not found"""
    if city_name == "" or city_name is None:
        # Empty input
        return "empty"
    elif not legal_search_word(city_name):
        # Illegal input
        return "illegal"
    else:
        api_data = take_data(city_name)
        if api_data is None:
            # City name wasn't found
            return "not_found"
        elif api_data == "api_error":
            return "api_error"
        else:
            return api_data_to_needed_lists(api_data)
