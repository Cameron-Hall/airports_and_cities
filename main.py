import sqlite3
import os

def clear():
    os.system('clear')

def airport_info(airport):
    clear()
    print(f"What would you like to find out about {airport}?\n1. Official name\n2. City served\n3. Country served\n4. Number of unique destinations\n5. Number of terminals\n6. Yearly passengers\nYou may also enter multiple digits to find out multiple pieces of information\n\n> ")
    

def airport_list():
    clear()


with sqlite3.connect('europe_airpots.db') as conn:
    cursor = conn.cursor()
    user_choice = input("What would you like to find information about?\n1. Airports\n2. Cities\n> ")
    if user_choice == 1:
        user_choice = input("Enter the IATA code of the airport you'd like to find information about. If you'd like a list of airports, enter OPT")
        if user_choice == 'OPT':
            airport_list('all')
        else:
            airport_info(user_choice)

    conn.commit()