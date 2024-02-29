# %%
from __future__ import annotations

from tabulate import tabulate
import datetime
from mealplanner.src.food_database import *
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

data = [
    ('08-10', 400, '', '', '', '', '', '', ''),
    ('10-12', 300, '', '', '', '', '', '', ''),
    ('12-14', 750, '', '', '', '', '', '', ''),
    ('14-18', 450, '', '', '', '', '', '', ''),
    ('18-20', 600, '', '', '', '', '', '', ''),
    ('20-22', 600, '', '', '', '', '', '', ''),
    ('Snacks', 300, '', '', '', '', '', '', ''),
('Total', 300, '', '', '', '', '', '', ''), ]


numeric_values = [int(row[1]) for row in data[1:]]
total_sum = np.sum(numeric_values)

print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
print(total_sum)
