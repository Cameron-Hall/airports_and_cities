# IMPORTS
import sqlite3
import os

# LISTS
airports = []

# VARIABLES
proper_choice = False
program_running = True

# FUNCTIONS
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
        cursor.execute('SELECT * FROM airports WHERE IATA_code = ?',(airport,))
        information = cursor.fetchall()
        if information[0][5] > 1:
            plural = 's'
        else:
            plural = ''
        print(f"\033[1m{information[0][1]} ({information[0][0]})\033[m")
        print(f"{information[0][0]} is located in {information[0][2]}, {information[0][3]}. It has {information[0][5]} terminal{plural}.")
        print(f"It flies to {information[0][4]} unique destinations and has {information[0][6]} yearly passengers.")

        input("")
        os.system('cls')
        
def airport_list():
    global proper_choice
    get_all_airports()
    for i in range(30-(len(airports)%30)):
        airports.append("   ")
    print("\n \033[1mList of IATA Codes\033[m                                                                                                                                                              ")
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
    user_choice = input("\nWhich of these airports would you like to find information about?\nEnter the IATA code here: ")
    airport_info(user_choice)

with sqlite3.connect('europe_airports.db') as conn:
    cursor = conn.cursor()
    while program_running == True:
        user_choice = input("What would you like to find information about?\n1. Airports\n2. Cities (not working)\n3. Exit the program\n> ")
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
        elif user_choice == '3':
            program_running = False
        else:
            print("This is not an eligible option.")


        conn.commit()