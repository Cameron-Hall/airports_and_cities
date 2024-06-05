# IMPORTS
import sqlite3
import os

# LISTS
airports = []
info = []
sentence = []

# VARIABLES
proper_choice = False

# FUNCTIONS
def clear():
    os.system('clear')

def get_all_airports():
    cursor.execute('SELECT airports.IATA_code FROM airports')
    results = cursor.fetchall()
    for item in results:
        airports.append(item[0])

def airport_info(airport):
    global proper_choice
    get_all_airports()
    if airport not in airports:
        print("This airport is not on the list.")
        proper_choice = False
    else:
        user_choice = input(f"What would you like to find out about {airport}?\n1. City served\n2. Country served\n3. Number of unique destinations\n4. Number of terminals\n5. Yearly passengers\nYou may also enter multiple digits to find out multiple pieces of information\n> ")
        for char in range(len(user_choice)):
            if user_choice[char] in info:
                pass
            else:
                info.append(user_choice[char])
        cursor.execute('SELECT * FROM airports WHERE IATA_code = ?',(airport,))
        information = cursor.fetchall()
        print(f"{information[1]} ({information[0]})")
        
        
        
def airport_list():
    global proper_choice
    get_all_airports()
    for i in range(20-(len(airports)%20)):
        airports.append("   ")
    print("                                                   List of IATA Codes                                                    ")
    print(" ----------------------------------------------------------------------------------------------------------------------- ")
    if len(airports)%20 == 0:
        extra = 0
    else:
        extra = 1
    for i in range((len(airports)//20)+extra):
        j = i*20
        print(f"| {airports[j]} | {airports[j+1]} | {airports[j+2]} | {airports[j+3]} | {airports[j+4]} | {airports[j+5]} | {airports[j+6]} | {airports[j+7]} | {airports[j+8]} | {airports[j+9]} | {airports[j+10]} | {airports[j+11]} | {airports[j+12]} | {airports[j+13]} | {airports[j+14]} | {airports[j+15]} | {airports[j+16]} | {airports[j+17]} | {airports[j+18]} | {airports[j+19]} |")
        if i+1 != (len(airports)//20)+extra:
            print("|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(" ----------------------------------------------------------------------------------------------------------------------- ")
    user_choice = input("\nWhich of these airports would you like to find information about?\nEnter the IATA code here: ")
    airport_info(user_choice)

with sqlite3.connect('europe_airports.db') as conn:
    cursor = conn.cursor()
    user_choice = input("What would you like to find information about?\n1. Airports\n2. Cities (not working)\n> ")
    proper_choice = False
    if user_choice == '1':
        while proper_choice == False:
            user_choice = input("Enter the IATA code of the airport you'd like to find information about. If you'd like a list of airports, enter OPT.\n> ")
            if user_choice == 'OPT':
                proper_choice = True
                airport_list()
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