import csv
import re

csv_file = input('insert csv file path')
output_folder = input("insert output folder path")
counter = 1

with open(csv_file, 'r') as my_input_file:
    for line in my_input_file:
        print(line)

