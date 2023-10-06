import mysql.connector
from Query import *
from alter import *
from delete import *
from update import *
from create_table import *
from create_view import *
from Insert import *


def main():
    # Welcome user to Olympic Archery Database
    print("Welcome to the Olympic Archery Database. Please Enter Your Username and Password!")

    # Ask for username and password
    user_name = input("Username: ")
    pass_word = input("Password: ")

    # Use the inputed username and password to establish connection to database
    cnx = mysql.connector.connect(

        user=user_name,
        password=pass_word,
        host='127.0.0.1',
        port=3306)

    # Create cursor
    cursor = cnx.cursor()
    # Connect Olympic Archery DB
    cursor.execute("use olympicarchery")

    # Present user with options for the operations they can run, and allow them to choose based on the number of the option.
    print("Welcome! Choose one of the following operations to conduct:\n1. Insert\n2. Delete\n3. Update\n4. Create Table\n5. Create View\n6. Alter\n7. Query\n8. Quit Program")
    user_action = int(input("Enter the number of your chosen operation: "))

    # Program will run until user exits.
    while (user_action != 8):
        if (user_action == 1):
            try:
                # Get an insert query using the insert function.
                sequel_query = insert_function()

                # If the returned sql query is in tuple form.
                if (isinstance(sequel_query, tuple) == True):
                    # Execute query and commit changes to DB.
                    cursor.execute(sequel_query[0], sequel_query[1])
                    cnx.commit()
                else:
                    # Execute query and commit changes to DB.
                    cursor.execute(sequel_query)
                    cnx.commit()
                # Print that the insert query worked and ask them for the next operation.
                print("Your Insert Statement was successfully executed! Please execute the query operation to if you wish to see your changes.")
                user_action = int(
                    input("Enter the number of your next operation: "))
            except:
                # If sql query doesn't work then print error and allow them to try choosing operation again.
                print(
                    "An error was detected in your Insert Statement! Please Try Again!")
                user_action = int(
                    input("Enter the number of your operation again: "))

        if (user_action == 2):
            try:
                # Get delete query from delete function
                sequel_query = delete_function()
                # If the returned sql query is in tuple form.
                if (isinstance(sequel_query, tuple) == True):
                    # Execute query and commit changes to DB.
                    cursor.execute(sequel_query[0], sequel_query[1])
                    cnx.commit()
                else:
                    # Execute query and commit changes to DB.
                    cursor.execute(sequel_query)
                    cnx.commit()
                # Print that the delete query worked and ask them for the next operation.
                print("Your Delete Statement was successfully executed! Please execute the query operation to if you wish to see your changes.")
                user_action = int(
                    input("Enter the number of your next operation: "))
            except:
                # If sql query doesn't work then print error and allow them to try choosing operation again.
                print(
                    "An error was detected in your Delete Statement! Please Try Again!")
                user_action = int(
                    input("Enter the number of your operation again: "))

        if (user_action == 3):
            try:
                # Get update query from update function
                sequel_query = update_function()
                # Execute query and commit changes to DB.
                cursor.execute(sequel_query)
                cnx.commit()
                # Print that the delete query worked and ask them for the next operation.
                print(
                    "Your table was successfully updated! Please execute the query operation to if you wish to see your changes.")
                user_action = int(
                    input("Enter the number of your next operation: "))
            except:
                # If sql query doesn't work then print error and allow them to try choosing operation again.
                print(
                    "An error was detected in your Update Statement! Please Try Again!")
                user_action = int(
                    input("Enter the number of your operation again: "))

        if (user_action == 4):
            try:
                # Get create table query from create table function
                sequel_query = create_table()
                # Execute query
                cursor.execute(sequel_query)
                # Print that the create table query worked and ask them for the next operation.
                print(
                    "Your table was successfully created! Please execute the query operation to if you wish to see the table.")
                user_action = int(
                    input("Enter the number of your next operation: "))
            except:
                # If sql query doesn't work then print error and allow them to try choosing operation again.
                print(
                    "An error was detected in your Create Table Statement! Please Try Again!")
                user_action = int(
                    input("Enter the number of your operation again: "))

        if (user_action == 5):
            try:
                # Get create view query from create view function
                sequel_query = create_view()
                # Execute query
                cursor.execute(sequel_query)
                # Print that the create view query worked and ask them for the next operation.
                print(
                    "Your view was successfully created! Please execute the query operation to if you wish to see the view.")
                user_action = int(
                    input("Enter the number of your next operation: "))
            except:
                # If sql query doesn't work then print error and allow them to try choosing operation again.
                print(
                    "An error was detected in your Create View Statement! Please Try Again!")
                user_action = int(
                    input("Enter the number of your operation again: "))

        if (user_action == 6):
            try:
                # Get alter query from alter function
                sequel_query = alter_function()
                # Execute query and commit changes to DB.
                cursor.execute(f'{sequel_query}')
                cnx.commit()
                # Print that the alter query worked and ask them for the next operation.
                print(
                    "Your table was successfully altered! Please execute the query operation to if you wish to see your changes.")
                user_action = int(
                    input("Enter the number of your next operation: "))
            except:
                # If sql query doesn't work then print error and allow them to try choosing operation again.
                print("An error was detected in your Alter Statement! Please Try Again!")
                user_action = int(
                    input("Enter the number of your operation again: "))

        if (user_action == 7):
            try:
                # Get query from query function
                sequel_query = query_function()
                # Execute query
                cursor.execute(f'{sequel_query}')

                # Get the attribute names and how many attributes there are
                attribute_names = cursor.column_names
                attributes_size = len(attribute_names)

                print(
                    f"The table for the following query statement ({sequel_query}) is shown below:\n")

                # Print out the attribute names
                for i in range(attributes_size):
                    print(f'{attribute_names[i]:<30}', end='')
                print()
                print((attributes_size * 30) * '-')

                # Get all the rows for the queried table and the number of rows
                information = cursor.fetchall()
                information_size = len(information)

                # Print out the information in the rows.
                for j in range(information_size):
                    for k in range(len(information[j])):
                        string = str(information[j][k])
                        print(f'{string:<30}', end='')
                    print()

                # Ask the user for their next operation.
                user_action = int(
                    input("Enter the number of your next operation: "))
            except:
                # If sql query doesn't work then print error and allow them to try choosing operation again.
                print(
                    f"An error was detected in your Query Statement! Please Try Again!")
                user_action = int(
                    input("Enter the number of your operation again: "))

    # Thank user for using program and close database.
    print("Thank You for Visiting the Olympic Archery Database!")
    cnx.close()


if __name__ == '__main__':  # Main program is being run.
    main()  # Calling on "main()" function.
