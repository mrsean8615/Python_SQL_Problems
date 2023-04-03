import pymssql
import sqlite3


#Remote database
def connect_db():
    try:
        conn = pymssql.connect(
            host='stairway.usu.edu', 
            user='bryant_seanpayne', 
            password='GoAggies!', 
            database='bryant_seanpayne') 
        cursor = conn.cursor()
        return cursor, conn
    except:
        print("Connection Failed")

#Local database
def connect_dblite():
    conn = sqlite3.connect("SQL/dbvac_sqlite.db")
    cursor = conn.cursor()
    return cursor, conn

