"""
-------------------------------------------------------------------------------
Q1. Please complete the following function to use your APIKEY to get current temperature (in Celsius) in your hometown from openweathermap.org.

If you don't have YOUR_OWN_APIKEY, you can use the APIKEY below, but you will lose 10 points.

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
-------------------------------------------------------------------------------
"""

from urllib import response
import urllib.request
import json

def get_current_temp(city, country):
    """
    Returns current temperature in Celsius in your hometown
     from api.openweathermap.org

    Notice: the temperature returned from the API is in Kelvin.
    Below is the conversion formula form Kelvin to Celsius:
    T(°C) = T(°K) - 273.15
    """


    APIKEY = '3bada50fc4b8667695d10d85e01d661f' # import from another file to hide sensitive information

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={APIKEY}'

    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # print(response_data)

    # How do we get current temperature?
    temperature = response_data['main']['temp'] - 273.15

    return str(temperature) + " Celsius"




# When you've completed your function, uncomment the following lines and run this file to test!

print(get_current_temp('Wellesley', 'us'))
print(get_current_temp('Tokyo', 'jp'))

## Expected output - of course the temperature in your hometown might be different:
# 11


"""
-------------------------------------------------------------------------------
Q2. One of OIM-APIs (https://oim-apis.herokuapp.com/students) returns JSON data of all the students. Please complete the function to read the names into a list. Each name will be one item in the list. This list should be sorted alphabetically.
-------------------------------------------------------------------------------
"""


def get_name_list():
    """
    Return: a sorted list of names
    """

    url = 'https://oim-apis.herokuapp.com/students'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    names = list()
    for i in response_data['students']:
        # print(i['name'])
        names.append(i['name'])
    # names = names.sort()
    names.sort()
    return names




# get_name_list()



# When you've completed your function, uncomment the following lines and run this file to test!

names = get_name_list()
print(names)

## Expected output:
# ['Alan', 'Amoy', 'Andrew', 'Angelina', 'Brandon', 'Caroline', 'Changli', 'Daisy', 'Devang', 'Eli', 'Erin', 'Gabriel', 'Helen', 'Henry', 'Jason', 'Julia', 'K', 'Kate', 'Kike', 'Maciej', 'Manan', 'Marshall', 'Martina', 'Max', 'Mel', 'Navin', 'Priyavrat', 'Rafael', 'Runyi', 'Shaan', 'Thomas', 'Tomas', 'Weiye', 'Xavier', 'Xiner', 'Yash', 'Yu', 'Ziya']


"""
-------------------------------------------------------------------------------
Q3. Please complete the function that gets names from a list to run a simulation of 200 times of class participation. In each class participation, only one student will be called randomly. This function should return a dictionary that records how many times each student gets called. Please do not change any code outside function.
-------------------------------------------------------------------------------
"""


# Please do not modify the following two lines
import random

random.seed(42)


def simulation(names, num_of_calls):
    """
    names: a list of names
    num_of_calls: total times of cold-calls in the simulation

    Return: a dictionary of name: integer pairs
    """

    counter = 0
    for _ in names:
        counter += 1
    
    distribution = dict()

    for k in names:
        distribution[k] = 0

    for i in range(num_of_calls):
        number = random.randint(0, counter - 1)
        name = names[number]
        distribution[name] = distribution.get(name, 0) + 1

    # need to sort
    return distribution


# When you've completed your function, uncomment the following lines and run this file to test!

name_list = get_name_list()
print(simulation(name_list, 200))

## Expected output:
# {'Alan': 5, 'Amoy': 5, 'Andrew': 5, 'Angelina': 4, 'Brandon': 9, 'Caroline': 8, 'Changli': 5, 'Daisy': 7, 'Devang': 5, 'Eli': 4, 'Erin': 8, 'Gabriel': 1, 'Helen': 4, 'Henry': 6, 'Jason': 12, 'Julia': 7, 'K': 6, 'Kate': 8, 'Kike': 3, 'Maciej': 3, 'Manan': 4, 'Marshall': 5, 'Martina': 3, 'Max': 7, 'Mel': 6, 'Navin': 4, 'Priyavrat': 1, 'Rafael': 6, 'Runyi': 3, 'Shaan': 6, 'Thomas': 1, 'Tomas': 4, 'Weiye': 6, 'Xavier': 4, 'Xiner': 9, 'Yash': 7, 'Yu': 3, 'Ziya': 6}


"""
-------------------------------------------------------------------------------
Q4. Please complete the following function that prints rows with the name and a number of asterisks equal to the positive integer given a dictionary of name: integer pairs. The rows should be printed in alphabetical order of names. No return is required. Please do not change any code outside function.
-------------------------------------------------------------------------------
"""
# Please do not modify the following line
random.seed(42)


def print_hist(data):
    """
    data: a dictionary of name: integer pairs
    """
    # print(data)
    for k, v in data.items():
        print(f'{k}: ' + '*'*v)


# When you've completed your function, uncomment the following lines and run this file to test!

name_list = get_name_list()
name_dict = simulation(name_list, 200)
print_hist(name_dict)

## Expected output:
# Alan: *****
# Amoy: *****
# Andrew: *****
# ...
# Yash: *******
# Yu: ***
# Ziya: ******


"""
-------------------------------------------------------------------------------
Q5. Please complete the following function that prints rows with the name and a number of asterisks equal to the positive integer given a dictionary of name: integer pairs. The rows should be printed in descending order of number of asterisks. No return is required. Please do not change any code outside function.
-------------------------------------------------------------------------------
"""
# Please do not modify the following line
random.seed(42)


def print_hist_by_number(data):
    """"""
    lst = list()
    for k, v in data.items():
        #print(f'{k}: ' + '*'*v)
        lst.append(k + ': ' + str('*'*v))

    lst.sort(reverse=True)
    
    return lst


## When you've completed your function, uncomment the following lines and run this file to test!

# name_list = get_name_list()
# name_dict = simulation(name_list, 200)
# print_hist_by_number(name_dict)

## Expected output:
# Jason: ************
# Brandon: *********
# Xiner: *********
# Caroline: ********
# Erin: ********
# ...