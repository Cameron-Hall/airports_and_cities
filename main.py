import sqlite3

with sqlite3.connect('europe_airpots.db') as conn:
    cursor = conn.cursor()
    user_choice = input("What would you like to find information about?\n1. Airports\n2. Cities\n> ")

    conn.commit()