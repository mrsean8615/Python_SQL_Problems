#Sean Payne
# I decided to use the local DB here since I didn't want to mess with the server side data too much.
#connect_db() for server, connect_dblite() for local
from SQL.db_connect import *

cursor, conn = connect_dblite()

#user input
ustate = input("Enter a two-letter state abbreviation: ")
try:
    upopulation = int(input("Enter population of new state: "))
except:
    print("A int value was not entered. Try again.")

#SQL
cursor.execute("UPDATE USState SET Population = %d WHERE StateID = '%s';" % (upopulation, ustate))
conn.commit()
cursor.execute(f"SELECT StateID, Population FROM USState WHERE StateID = '{ustate}';")

for x in cursor:
    print(x[0], x[1])


