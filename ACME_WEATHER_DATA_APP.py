import csv
from datetime import datetime


class data_processor:
    data = []

    @staticmethod
    def data_loading():
        try:
            file_name_input = str(input("Please enter the CSV file name: "))
            file = open(file_name_input, newline='')
            print("Successfully opened {} reading contents...".format(file_name_input))
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                row = row[0].split(";")
                date = datetime.strptime(row[0], "%Y-%m-%d").strftime("%d.%m")
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
                data_processor.data.append(
                    [[date, precipitation, mean_temperature, minimum_temperature, maximum_temperature,
                      typical_maximum_temperature, typical_maximum_temperature_1,
                      typical_minimum_temperature, typical_minimum_temperature_1,
                      fairly_typical_maximum_temperature, fairly_typical_maximum_temperature_1,
                      fairly_typical_minimum_temperature, fairly_typical_minimum_temperature_1]])
            print("Loaded weather data from {}\n".format(file_name_input[:-4].capitalize()))
        except FileNotFoundError:
            print("File not found! Please enter the valid name of the file!\n")

    @staticmethod
    def show_daily_data():
        try:
            if not data_processor.data:
                print("Please, load the data by using the option 1 first!")
            else:
                user_date_input = str(input("Give a date (dd.mm): "))
                given_date = datetime.strptime(user_date_input, "%d.%m").strftime("%d.%m")
                data_found = False
                for day_data in data_processor.data:
                    if day_data[0][0] == given_date:
                        print("day data [0][1]", day_data[0][1])
                        average_temperature = day_data[0][2]
                        lowest_temperature = day_data[0][3]
                        highest_temperature = day_data[0][4]
                        precipitation = day_data[0][1]
                        print("The weather on {} was on average {} centigrade".format(given_date, average_temperature))
                        print("The lowest temperature was {} and the highest temperature was {}".format(
                            lowest_temperature, highest_temperature))
                        print("There was {} mm rain".format(precipitation))
                        data_found = True
                        break
                if not data_found:
                    print("The data for entered date is not found in the dataset!")
        except TypeError:
            print("Please enter the valid date!")
        print()

    @staticmethod
    def calculate_average():
        # TODO Calculate average statistics for the data
        print("Option number 3 code here")
        print()

    @staticmethod
    def render_chart():
        # TODO Print a scatterplot of the average temperatures
        print("Option number 4 code here")
        print()


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
            data_processor.data_loading()
        elif user_input == 2:
            data_processor.show_daily_data()
        elif user_input == 3:
            data_processor.calculate_average()
        elif user_input == 4:
            data_processor.render_chart()
        else:
            print("Please choose the menu option by choosing number from 1 to 4.")
    except ValueError:
        print("Please choose the menu option by choosing number from 1 to 4."
              " If you want to exit the program, enter 0\n")
