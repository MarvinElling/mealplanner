from tabulate import tabulate
import datetime

# Function to generate a week overview
def generate_week_overview():
    # Get the current date
    today = datetime.date.today()

    # Calculate the start and end of the week
    start_of_week = today - datetime.timedelta(days=today.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)

    # Generate a list of days in the week
    days_in_week = [start_of_week + datetime.timedelta(days=i) for i in range(7)]

    # Create a table with headers and data
    headers = ["Day", "Date"]
    data = [(day.strftime("%A"), day.strftime("%Y-%m-%d")) for day in days_in_week]

    # Print the table using tabulate
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# Generate and print the week overview
generate_week_overview()
