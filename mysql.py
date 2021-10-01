import sqlite3
import webbrowser

connection = sqlite3.connect('database.db')

if connection:
    print("Connected Successfully")
else:
    print("Connection Not Established")

cursor = connection.cursor()

# Create identification table
# command1 = '''CREATE TABLE IF NOT EXISTS
#     identification(id_client INTEGER  PRIMARY KEY , name_client MESSAGE_TEXT , age INTEGER, city MESSAGE_TEXT,
#      attendance_time INTEGER,  violence_time INTEGER,  over_consumption INTEGER)'''
# cursor.execute(command1)

# Add to identification table
# cursor.execute("INSERT INTO identification VALUES (1, 'chris_hemsworth', 30, 'Paris', 21, 0, 3)")
# cursor.execute("INSERT INTO identification VALUES (2, 'jeremy_renner', 25, 'Reims', 21, 0, 3)")

# Update table information
# cursor.execute("UPDATE identification SET attendance_time = 1, violence_time = 0, over_consumption = 3 WHERE id_client=1")

# Delete with condition
# cursor.execute("DELETE FROM identification WHERE id_client = 1")

# Save data
# connection.commit()

# # delete all rows from table
# cursor.execute('DELETE FROM identification;',)
# print('We have deleted', cursor.rowcount, 'records from the table.')
# #commit the changes to db
# connection.commit()
# #close the connection
# connection.close()

