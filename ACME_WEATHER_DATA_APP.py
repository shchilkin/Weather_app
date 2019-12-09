import csv
from datetime import datetime


class data_processor:
    data = []

    @staticmethod
    def data_loading():
        try:
            data_processor.data = []
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
                        average_temperature = day_data[0][2]
                        lowest_temperature = day_data[0][3]
                        highest_temperature = day_data[0][4]
                        precipitation = day_data[0][1]
                        print("The weather on {} was on average {} centigrade"
                              .format(given_date, average_temperature))
                        print("The lowest temperature was {} and the highest temperature was {}"
                              .format(lowest_temperature, highest_temperature))
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
        average_temperature_list = []
        average_lowest_temperature_list = []
        average_highest_temperature_list = []
        try:
            if not data_processor.data:
                print("Please, load the data by using the option 1 first!\n")
            else:
                for day_data in data_processor.data:
                    average_temperature_list.append(day_data[0][2])
                    average_lowest_temperature_list.append(day_data[0][3])
                    average_highest_temperature_list.append(day_data[0][4])
            average_temperature = round(
                sum(average_temperature_list) / len(average_temperature_list), 2)
            average_highest_temperature = round(
                sum(average_highest_temperature_list) / len(average_highest_temperature_list), 2)
            average_lowest_temperature = round(
                sum(average_lowest_temperature_list) / len(average_lowest_temperature_list), 2)
            print("The average temperature for the {} day period was {}"
                  .format(len(average_temperature_list), average_temperature))
            print("The average lowest temperature was {}".format(average_lowest_temperature))
            print("The average highest temperature was {}\n".format(average_highest_temperature))
        except ZeroDivisionError:
            pass

    @staticmethod
    def render_chart():
        if not data_processor.data:
            print("Please, load the data by using the option 1 first!\n")
        else:
            def print_temperature_line(day_and_month, temp):
                print(day_and_month + " ", end="")
                print("   " * (round(temp) + 5) + "-", end="")
                print()

            def print_temperature_axis():
                print("      ", end="")
                for i in range(-5, 16):
                    print("{:02d} ".format(i), end="")
                print()

            for day_data in data_processor.data:
                date = day_data[0][0]
                average_temperature = day_data[0][2]
                print_temperature_line(date, average_temperature)
            print_temperature_axis()
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