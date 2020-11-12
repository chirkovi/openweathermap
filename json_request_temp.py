import datetime
import requests
import statistics
# import json


def get_json(url="http://api.openweathermap.org/data/2.5/forecast"):
    return requests.get(url, params=parameters).json()


def get_temperature(input_list):
    temperature_dict = {}
    for weather in input_list:
        date = datetime.datetime.strptime(weather['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
        if date in temperature_dict:
            temperature_dict[date].append(weather['main']['temp'])
        else:
            temperature_dict[date] = [weather['main']['temp']]
    return temperature_dict


def get_max_temperature(input_list):
    max_temperature_dict = {}
    morning_hour = {9, 12}
    for weather in input_list:
        date_time = datetime.datetime.strptime(weather['dt_txt'], '%Y-%m-%d %H:%M:%S')
        date = date_time.date()
        hour = date_time.time().hour
        if date in max_temperature_dict and hour in morning_hour:
            max_temperature_dict[date].append(weather['main']['temp'])
        elif hour in morning_hour:
            max_temperature_dict[date] = [weather['main']['temp']]
    return max_temperature_dict


def print_temperature(temp_dict, max_temp_dict):
    print("Average temperature")
    for day, temp in temp_dict.items():
        temp = statistics.mean(temp)
        print(day, temp)
    print("\nMorning temperature")
    for day, max_temp in max_temp_dict.items():
        max_temp = statistics.mean(max_temp)
        print(day, max_temp)


if __name__ == "__main__":
    parameters = {'id': '524901', 'mode': 'json', 'units': 'metric', 'appid': '03f90859bfa5b3b6d0c0c63e54c61172'}
    # print(json.dumps(get_json(), indent=4, sort_keys=True))  # Print JSON data
    json_list = get_json()['list']
    max_temperature = get_max_temperature(json_list)
    temperature = get_temperature(json_list)
    print_temperature(temperature, max_temperature)

