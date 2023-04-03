#Sean Payne
from SQL.db_connect import *

#connect_db() for server, connect_dblite() for local
cursor, conn = connect_dblite()

#Return true or false if query lookup is empty or not
def isEmpty(query):
    cursor.execute(query)
    record = cursor.fetchall() 
    count = len(record) 
    if count == 0: 
        return False
    else: 
        return True

#returns the defined query    
def query(attribute):

    lookupQuery = (f"""SELECT CustID, FName, LName, Gender, s.StateName, s.Population
            FROM Customer
                JOIN USState as s
                ON CustState = s.StateID
            WHERE {attribute} = {uinput}""")
    return lookupQuery

#runs the results and error traps for no results
def runEmptyResults(query, strAtt):
    if isEmpty(query):
        cursor.execute(query)
        for x in cursor:
            queryResults(x)
    else:
        print(f'No result found for {strAtt}: {uinput}. ')

#accounts for improper database entries; such as a NULL value
def checkNull(value):
    if value is None:
        return 'undefined'
    else:
        return value.upper()

#returns a constructed query output
def queryResults(x):
    print(f'''Customer ID: {x[0]} First Name: {x[1]} Last Name: {x[2]} Gender: {checkNull(x[3])} State: {x[4]} Population: {int(x[5]):,} ''')

y = True

while y:
    isInt = True
    uinput = input("Enter a Customer ID or Name (press enter to stop searching): ")

    #breaks out of program when input is nothing
    if uinput == '':
        y = False
        break
    
    #Check uinput for int
    try:
        uinput = int(uinput)
    except: 
        isInt = False

    #If the user entered a ID
    if isInt:

        IDQuery = query('CustID')

        runEmptyResults(IDQuery, 'ID#')


    #If user enter a name logic
    else:
        print("Is this a last name or first name?")
        nameinput = input("'last' for last name lookup, 'first' for first name lookup: ").casefold()
        uinput = f"'{uinput}'"

        if nameinput == 'last':
            #run last name lookup 
            nameQuery = query('LName')

            runEmptyResults(nameQuery, 'Last Name')

        elif nameinput == 'first':
            #run first name lookup
            nameQuery = query('FName')

            runEmptyResults(nameQuery, 'First Name')

        else:
            print("please enter either 'first' or 'last' on the lookup")

