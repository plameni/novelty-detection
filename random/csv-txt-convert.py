import csv

csv_file = input('insert csv file path')
output_folder = input("insert output folder path")
counter = 1

with open(csv_file, 'r') as my_input_file:
    for line in my_input_file:
        with open('./../random-files/generated-text-files/' + output_folder + "/" + str(counter) + '.txt', 'w') as generatedTxtFile: 
            generatedTxtFile.write(line)
            counter = counter + 1

