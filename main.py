# IMPORTS
import sqlite3
import os
import time

# LISTS
airports = []
airports_filtered = []
cities = []

# VARIABLES
proper_choice = False
program_running = True
from_options = False
from_city = False

# FUNCTIONS
def clear():
    os.system('cls')
    time.sleep(0.1)

clear()

def get_all_airports():
    cursor.execute('SELECT airports.IATA_code FROM airports')
    results = cursor.fetchall()
    for item in results:
        airports.append(item[0])
    for i in range(30-(len(airports)%30)):
        airports.append("   ")

def airport_info(airport):
    global information
    global proper_choice
    if airport not in airports:
        print(f"'{airport}' is not a valid airport.")
        proper_choice = False
    else:
        cursor.execute('SELECT * FROM airports WHERE IATA_code = ?',(airport,))
        information = cursor.fetchall()
        if information[0][5] > 1:
            plural = 's'
        else:
            plural = ''
        print(f"\033[1m{information[0][1]} ({information[0][0]})\033[m")
        print(f"{information[0][0]} is located in {information[0][2]}, {information[0][3]}. It has {information[0][5]} terminal{plural}.")
        print(f"It flies to {information[0][4]} unique destinations and has {information[0][6]} yearly passengers.")
        
def airport_list():
    print("\n \033[1mList of IATA Codes\033[m")
    print(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    if len(airports)%30 == 0:
        extra = 0
    else:
        extra = 1
    for i in range((len(airports)//30)+extra):
        j = i*30
        print(f"| {airports[j]} | {airports[j+1]} | {airports[j+2]} | {airports[j+3]} | {airports[j+4]} | {airports[j+5]} | {airports[j+6]} | {airports[j+7]} | {airports[j+8]} | {airports[j+9]} | {airports[j+10]} | {airports[j+11]} | {airports[j+12]} | {airports[j+13]} | {airports[j+14]} | {airports[j+15]} | {airports[j+16]} | {airports[j+17]} | {airports[j+18]} | {airports[j+19]} | {airports[j+20]} | {airports[j+21]} | {airports[j+22]} | {airports[j+23]} | {airports[j+24]} | {airports[j+25]} | {airports[j+26]} | {airports[j+27]} | {airports[j+28]} | {airports[j+29]} |")
        if i+1 != (len(airports)//30)+extra:
            print("|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|")
    print(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")

def get_all_cities():
    cursor.execute('SELECT cities.city_name FROM cities')
    results = cursor.fetchall()
    for item in results:
        cities.append(item[0])
    for i in range(10-(len(cities)%10)):
        cities.append(" ")

def city_info(city):
    global proper_choice
    cursor.execute('SELECT * FROM cities WHERE city_name = ?',(city,))
    information = cursor.fetchall()
    if information[0][2] > 1:
        plural = 's'
        are_or_is = 'are'
    else:
        plural = ''
        are_or_is = 'is'
    print(f"\033[1m{information[0][1]}\033[m")
    print(f"There {are_or_is} {information[0][2]} airport{plural} in {information[0][1]}. {information[0][1]} is home to approximately {information[0][3]} people.")
    input('')
    
def city_list():
    print("\n \033[1mList of Cities \033[m")
    print(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    if len(cities)%10 == 0:
        extra = 0
    else:
        extra = 1
    for i in range((len(cities)//10)+extra):
        j = i*10
        print(f"| {cities[j]:<15} | {cities[j+1]:<15} | {cities[j+2]:<15} | {cities[j+3]:<15} | {cities[j+4]:<15} | {cities[j+5]:<15} | {cities[j+6]:<15} | {cities[j+7]:<15} | {cities[j+8]:<15} | {cities[j+9]:<15} |")
        if i+1 != (len(cities)//10)+extra:
            print("|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|")
    print(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")

def airport_caller(user_choice):
    global information
    global proper_choice
    user_choice = user_choice.upper()
    alphabetic_string = ''
    for char in range(len(user_choice)):
        if user_choice[char].isalpha():
            alphabetic_string += user_choice[char]
    user_choice = alphabetic_string
    if user_choice == 'OPT':
        while not proper_choice:
            proper_choice = False
            airport_list()
            user_choice = input("1. Choose airport from list\n2. Back to homepage\n> ")
            clear()
            if user_choice == '1':
                user_choice = input("Enter the IATA code of the airport you'd like to find information about.\n> ")
                airport_caller(user_choice)
                proper_choice = True
            elif user_choice == '2':
                proper_choice = True
            else:
                airport_caller(user_choice)
    elif len(user_choice) % 3 != 0 or len(user_choice) == 0:
        clear()
        print("Invalid length of entry. Make sure all IATA codes entered are 3 letters long")
    else:
        if len(user_choice) == 3:
            plural = ''
        else:
            plural = 's'
        clear()
        if not from_city:
            print(f"To confirm, you want to view information about the following airport{plural}:")
            front_end = 0
            back_end = 3
            for i in range(len(user_choice)//3):
                print(f"{user_choice[front_end:back_end]}")
                front_end += 3
                back_end += 3
            confirmation = input("Type Y to proceed, or nothing to reselect your airports: ")
        else:
            confirmation = 'Y'
        if confirmation.upper() == 'Y':
            proper_choice = True
            front_end = 0
            back_end = 3
            clear()
            num_of_airports = len(user_choice)//3
            for airport in range(num_of_airports):
                entry = user_choice[front_end:back_end]
                airport_info(entry)
                print(" ")
                front_end += 3
                back_end += 3
                time.sleep(0.1)
            input("")
        else:
            pass
        clear()

# CODE
with sqlite3.connect('airports_and_cities.db') as conn:
    cursor = conn.cursor()
    get_all_airports()
    get_all_cities()
    while program_running:
        print("\033[1mEUROPEAN AND AMERICAN AIRPORTS AND CITIES\033[m")
        user_choice = input("What would you like to find information about?\n1. Airports\n2. Cities\n3. Exit the program\n> ")
        clear()
        proper_choice = False
        if user_choice == '1':
            while not proper_choice:
                user_choice = input(f"Enter the IATA code(s) of the airport you'd like to find information about. They are three letters and all alphabetic.\nIf you'd like a list of cities, enter OPT. \nIf you'd like to look at information for multiple airports, simply separate the IATA codes with a space.\n> ")
                airport_caller(user_choice)
        elif user_choice == '2':
            while not proper_choice:
                if from_options == True:
                    options = ''
                    from_options = False
                else:
                    options = "If you'd like a list of cities, enter options."
                user_choice = input(f"Enter the name of the city you'd like to find information about. {options}\n> ")
                proper_choice = False
                if user_choice.title() in cities:
                    clear()
                    city_info(user_choice.title())
                    city = user_choice.title()
                    while not proper_choice:
                        user_choice = input(f"1. View all airports in {city}.\n2. Back to home page\n> ")
                        if user_choice == '1':
                            cursor.execute("SELECT airports.IATA_code FROM airports WHERE city_served = ?",(city, ))
                            information = cursor.fetchall()
                            airports_in_city = ''
                            for i in information:
                                airports_in_city += i[0] 
                            from_city = True
                            airport_caller(airports_in_city)     
                            proper_choice = True   
                            from_city = False
                        elif user_choice == '2':
                            clear()
                            proper_choice = True
                        else:
                            clear()
                            print("This is not a valid option")
                elif user_choice.lower() == 'options':
                    clear()
                    proper_choice = False
                    city_list()
                    user_choice = '2'
                    from_options = True
                else:
                    clear()
                    print(f"'{user_choice}' is not a valid city")
        elif user_choice == '3':
            program_running = False
        else:
            print("This is not an eligible option.")

        conn.commit()