import json
import csv
import PySimpleGUI as sg
import pandas
import numpy
file_list = sg.popup_get_file('Select or write the path of the file you wish to convert.')
obt_json = pandas.read_json(file_list)
file_list1 = sg.popup_get_folder('Select location to save file.')
file_list1 += "\KS_generated_csv_file.csv"
obt_json.to_csv(file_list1, index=None)
# obt_csv = pandas.read_csv(file_list1)
# GFG = pandas.ExcelWriter('KS_generated_spreedsheet_file.xlsx')
# obt_csv.to_excel(GFG, index=False)
