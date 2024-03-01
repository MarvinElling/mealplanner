# %%
from __future__ import annotations

from tabulate import tabulate
import datetime
from mealplanner.src.food_database import *
from mealplanner.src.recipies import *
import numpy as np


today = datetime.date.today()

# Calculate the start and end of the week
start_of_week = today - datetime.timedelta(days=today.weekday())
end_of_week = start_of_week + datetime.timedelta(days=6)

# Generate a list of days in the week
days_in_week = [start_of_week + datetime.timedelta(days=i) for i in range(7)]

# Create a table with headers and data
headers = [
    'Zeit', 'Ziel','Montag',
    'Dienstag',
    'Mittwoch',
    'Donnerstag',
    'Freitag',
    'Samstag',
    'Sonntag',
]
brote3 = [brot, brot, brot]
data = [
    #('08-10', 400, Dish('Reis', [('reis', 10)]), 0, 0, 0, 0, 0, 0),
    ('08-10', 400, [apfel, toast], [apfel, musli_morning], [apfel, sahnejoghurt], [apfel, toast], [apfel, sahnejoghurt], [apfel, toast, toast], [apfel, musli_morning]),
    ('10-12', 300, [ei,ei], 0, [ei], [ei, quark_musli], 0, quark_musli, [ei,ei]),  # noqa: F405
    ('12-14', 750, reis1, reis1, reis1, spagh_carb, spagh_carb, quinoa_bowl, quinoa_bowl),
    ('14-18', 450, brote3, brote3, brote3, brote3, brote3, brote3, [reiswaffel3]),
    ('18-20', 600, [reiswaffel3, banane], 0, [toast_kase, toast_kase], milch, [milch, lachs_reiswaffel], milch, [toast_kase, toast_kase]),
    ('20-22', 600, shake1, shake1, shake1, shake1, shake1, shake1, shake1), 
    ('Snacks', 300, [obstriegel, banane], [obstriegel, banane, schoko], [obstriegel, banane], [obstriegel, banane], [obstriegel, banane, schoko], banane, banane),
]
data2 = [
    #('08-10', 400, Dish('Reis', [('reis', 10)]), 0, 0, 0, 0, 0, 0),
    ('08-10', 400, [apfel], apfel, apfel, apfel, apfel, apfel, apfel),
    ('10-12', 300, 0, 0, 0, 0, 0, quark_musli, 0),  # noqa: F405
    ('12-14', 750, 0, 0, 0, 0, 0, 0, 0),
    ('14-18', 450, brote3, brote3, brote3, brote3, brote3, brote3, 0),
    ('18-20', 600, 0, 0, 0, 0, 0, 0, 0),
    ('20-22', 600, shake1, shake1, shake1, shake1, shake1, shake1, shake1), 
    ('Snacks', 300, [obstriegel, banane], [obstriegel, banane], [obstriegel, banane], [obstriegel, banane], [obstriegel, banane], banane, banane),
]

def calc_total(d):
    a = ['Total', '', '', '', '', '', '', '', '']
    for column in range(1, len(a)):
        values = []
        for row in d:
            if isinstance(row[column], list):
                values += row[column]
            else:
                values.append(row[column])

        total_sum = 0
        for v in values:
            total_sum += v
        a[column] = total_sum
    return tuple(a)


a = calc_total(data)
data.append(a)
a = calc_total(data2)
data2.append(a)


# print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
def format_dishes(dishes):
    return ', '.join(map(str, dishes))

# Iterate over the data and format Dish instances
formatted_data = []
for row in data:
    formatted_row = []
    for col in row:
        if isinstance(col, list) and all(isinstance(item, Dish) for item in col):
            formatted_row.append(format_dishes(col))
        else:
            formatted_row.append(col)
    formatted_data.append(formatted_row)

formatted_data2 = []
for row in data2:
    formatted_row = []
    for col in row:
        if isinstance(col, list) and all(isinstance(item, Dish) for item in col):
            formatted_row.append(format_dishes(col))
        else:
            formatted_row.append(col)
    formatted_data2.append(formatted_row)

# Print the tabulated data
print(tabulate(formatted_data, headers=headers, tablefmt="fancy_grid"))
# print(tabulate(formatted_data2, headers=headers, tablefmt="fancy_grid"))

