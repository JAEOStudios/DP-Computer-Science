#imports
import pyodbc
import os
import sys

import os

#path to database
database_path = r'C:\Users\MichaelHill\OneDrive - Alcuin School\Desktop\GoodsNX\DP\Lessons\A3-Hospital.accdb'  # Change to your Access DB path

#trying to open the database
try:
    #making sure the database exists
    if not os.path.exists(database_path):
        raise FileNotFoundError("Database file not found")

    #making sure the driver is installed
    drivers = [x for x in pyodbc.drivers() if 'Access' in x]
    conn_str = (
        f'DRIVER={{{drivers[0]}}};'  # This adds the required {} around the driver name
        f'DBQ={database_path};'
    )

    #trying to connect to the database
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to database")


        ###INSERT DATABASE COMMANDS HERE
        cursor = conn.cursor()
        query = 'INSERT INTO Employees (EmployeeID, DepartmentID, LastName, FirstName) VALUES (100, 101, \'Toe\', \'Joe\') ;' #change to desired query
        cursor.execute(query)
        conn.commit()
        print("Query successful.")

        #GOES AT THE END OF THIS TRY BLOCK
        conn.close()


    #error if can't connect
    except pyodbc.Error as e:
        raise ConnectionError("Failed to connect to database: " , e)

#catching other errors (file not found, etc.)
except Exception as err:
    print("Error: " , err)
    sys.exit(1)
