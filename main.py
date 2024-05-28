import sqlite3
import os

def clear():
    os.system('clear')

def airport_info():
    clear()
    


with sqlite3.connect('europe_airpots.db') as conn:
    cursor = conn.cursor()
    user_choice = input("What would you like to find information about?\n1. Airports\n2. Cities\n> ")

    conn.commit()