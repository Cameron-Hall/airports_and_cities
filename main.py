# IMPORTS
import sqlite3
import os

# LISTS
airports = []

# VARIABLES
proper_choice = False

# FUNCTIONS
def clear():
    os.system('clear')

def airport_info(airport):
    global proper_choice
    cursor.execute('SELECT airports.IATA_code FROM airports')
    results = cursor.fetchall()
    for item in results:
        airports.append(item[0])
    if airport not in airports:
        print("This airport is not on the list.")
        proper_choice = False
    else:
        print(f"What would you like to find out about {airport}?\n1. Official name\n2. City served\n3. Country served\n4. Number of unique destinations\n5. Number of terminals\n6. Yearly passengers\nYou may also enter multiple digits to find out multiple pieces of information\n> ")


def airport_list():
    clear()


with sqlite3.connect('europe_airports.db') as conn:
    cursor = conn.cursor()
    user_choice = input("What would you like to find information about?\n1. Airports\n2. Cities (not working)\n> ")
    proper_choice = False
    if user_choice == '1':
        while proper_choice == False:
            user_choice = input("Enter the IATA code of the airport you'd like to find information about. If you'd like a list of airports, enter OPT (currently not working).\n> ")
            if user_choice == 'OPT':
                proper_choice = True
                airport_list('all')
            elif len(user_choice) != 3:
                print('Invalid entry, IATA codes are 3 letters long.')
            else:
                proper_choice = True
                airport_info(user_choice)
    elif user_choice == '2':
        user_choice = input("Enter the name of the city you'd like to find information about. If you'd like a list of cities, enter options.")
    else:
        print("This is not an eligible option.")


    conn.commit()