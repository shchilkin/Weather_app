import csv
from datetime import datetime


def data_loading():
    try:
        file_name_input = str(input("Please enter the CSV file name: "))
        file = open(file_name_input, newline='')
        print("Successfully opened {} reading contents...".format(file_name_input))
        reader = csv.reader(file)
        header = next(reader)
        # print(header)
        data = []
        for row in reader:
            row = row[0].split(";")
            date = datetime.strptime(row[0], "%Y-%m-%d")
            precipitation = float(row[1])
            mean_temperature = float(row[2])
            minimum_temperature = float(row[3])
            maximum_temperature = float(row[4])
            typical_maximum_temperature = float(row[5])
            typical_maximum_temperature_1 = float(row[6])
            typical_minimum_temperature = float(row[7])
            typical_minimum_temperature_1 = float(row[8])
            fairly_typical_maximum_temperature = float(row[9])
            fairly_typical_maximum_temperature_1 = float(row[10])
            fairly_typical_minimum_temperature = float(row[11])
            fairly_typical_minimum_temperature_1 = float(row[12])
            data.append([date, precipitation, mean_temperature, minimum_temperature, maximum_temperature,
                         typical_maximum_temperature, typical_maximum_temperature_1,
                         typical_minimum_temperature, typical_minimum_temperature_1,
                         fairly_typical_maximum_temperature, fairly_typical_maximum_temperature_1,
                         fairly_typical_minimum_temperature, fairly_typical_minimum_temperature_1])
        print("Loaded weather data from {}\n".format(file_name_input[:-4].capitalize()))
    except FileNotFoundError:
        print("File not found! Please enter the valid name of the file!")


def show_daily_data():
    print("Option number 2 code here")
    # TODO See data for selected day


def calculate_average():
    # TODO Calculate average statistics for the data
    print("Option number 3 code here")


def print_scatterplot():
    # TODO Print a scatterplot of the average temperatures
    print("Option number 4 code here")


while True:
    print("""ACME WEATHER DATA APP
    1) Choose weather data file
    2) See data for selected day
    3) Calculate average statistics for the data
    4) Print a scatterplot of the average temperatures
    0) Quit program""")
    try:
        user_input = int(input("Choose what to do: "))
        if user_input == 0:
            break
        elif user_input == 1:
            data_loading()
        elif user_input == 2:
            show_daily_data()
        elif user_input == 3:
            calculate_average()
        elif user_input == 4:
            print_scatterplot()
        else:
            print("Please choose the menu option by choosing number from 1 to 4.")
            print("Type 0 to exit the program\n")
    except ValueError:
        print("Please choose the menu option by choosing number from 1 to 4."
              " If you want to exit the program, enter 0\n")
