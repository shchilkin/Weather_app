# import os
import csv
from datetime import datetime
#
#
# def clear():
#     os.system("cls" if os.name == "nt" else "clear")

data = []
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
            print("Option number 0 code here")
            quit()
        elif user_input == 1:
            # TODO Choose weather data file
            try:
                user_input = str(input("Please enter the CSV file name: "))
                file = open(user_input, newline='')
                print("Successfully opened {} reading contents...".format(user_input))
                reader = csv.reader(file)
                header = next(reader)
                data = []
                for row in reader:
                    print(row)
                print(header)
                print(data)

            except FileNotFoundError:
                print("File not found! Please enter the valid name of the file!")
        elif user_input == 2:
            print("Option number 2 code here")
            # TODO See data for selected day
        elif user_input == 3:
            # TODO Calculate average statistics for the data
            print("Option number 3 code here")
        elif user_input == 4:
            # TODO Print a scatterplot of the average temperatures
            print("Option number 4 code here")
        else:
            print("Please choose the menu option by choosing number from 1 to 4.")
            print("Type 0 to exit the program\n")
    except ValueError:
        print("Please choose the menu option by choosing number from 1 to 4."
              " If you want to exit the program, enter 0\n")
        # clear() #Clear terminal window comand
