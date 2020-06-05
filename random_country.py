import csv

countries = open('cou_caps.csv')
csv_countries = csv.reader(countries)
print(csv_countries)