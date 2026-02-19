# NESTED DICTIONARIES

# Structure: Dictionary -> List -> Dictionary


'''
1. Create an empty dictionary called calendar
2. Ask user for a date
3. Create an event dictionary with volunteer name and status
4. Store the event inside calendar under the date key
5. Print the full calendar

Bonus:
Change an event's status from 'Available' to 'Booked'
'''

# 1. Create empty dictionary
calendar = {}

# 2. Ask for date
date = input('Enter date: ')

# 3. Create event dictionary
event = {
    'Volunteer': 'Sipho',
    'Status': 'Available'
}

# 4. Store event under date
calendar[date] = event

# change status from Available to Booked
event.update({'Status': 'Booked'})

# 5. Print full calendar
print(calendar)
