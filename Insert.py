from Query import *


def insert_function():
    '''
        This function asks the user for several inputs and creats an SQL insert function based on the inputs.

        Parameters:
        None
        
        Return:
        Insert statement (insert) and a tuple (attnum) when user wants to insert 1 tuple. 
        Insert statement (insert) when user wants to insert multiple tuples.
    '''
    print("Choose one of the folowing:")
    print("Insert One Tuple (Enter 1):")
    print("Insert Multiple Tuples (Enter 2):")

    inp = input("Choose an option:")
    while (inp != '1') and (inp != '2'):
        print('Invalid input. Please try again:')
        inp = input("Choose an option again:")

    insert = "INSERT INTO "
    table1 = input("Select the table you would like to insert into:")
    table = table1.lower()

    attnum = input("Enter the number of attributes you would like to insert: ")

    while attnum.isnumeric() == False:
        print("Invalid input")
        attnum = input("Enter the number of attributes you would like to insert: ")

    attnum = int(attnum)

    insert += table.upper()

    if (inp == '1'):
        insert += " ("
        for i in range(attnum):
            column = input("Enter the name of attribute "+str(i)+":")
            insert += column
            insert += ", "

        insert = insert[:-2]
        insert += ") VALUES ("
        for i in range(attnum):
            insert += '%s,'
        insert = insert[:-1] + ')'
        att_values = []
        for i in range(attnum):
            records = input("Enter the value for  attribute "+str(
                i)+" (remember to enter values for all 'NOT NULL' attributes and supply any necessery nulls):")
            if (records == 'NULL') or (records == 'Null') or (records == 'null'):
                records = None
            att_values.append(records)
        att_values = tuple(att_values)
        return insert, att_values

    else:
        insert += " ("
        for i in range(attnum):
            column = input("Enter the name of attribute "+str(i)+":")
            insert += column
            insert += ", "

        insert = insert[:-2]
        insert += ") "
        print(
            "Enter the information for the table you want to extrct multiple tuples from, in the form of a query:")
        query = query_function()
        insert += query
        return insert
