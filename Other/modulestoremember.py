'''import glob

myfiles = glob.glob('*.txt')
print(myfiles)

'''

'''
import csv

with open("weather.csv", r) as file:
    data = csv.reader(file)
    for row in data:
        print(row)
'''

'''
import shutil
shutil.make_archive('archive', 'zip', 'files')
'''


import webbrowser

user_input = input("Enter a search term: ").replace(" ", "+")
webbrowser.open("https://www.google.com/search?q=" + user_input)