def delete_function():
    '''
        This function asks the user for several inputs and creats an SQL delete function based on the inputs.

        Parameters:
        None

        Return:
        tab1: A string that is the SQL delete statement.
    '''
    print("Choose one of the folowing:")
    print("Delete an existing value (Enter 1):")
    print("Delete all values without deleting the table (Enter 2):")

    inp = input("Choose an option:")
    while (inp != '1') and (inp != '2'):
        print('Invalid input. Please try again:')
        inp = input("Choose an option again:")

    table1 = input("Enter the table you would like to delete from:")
    table = table1.lower()

    if (inp == '1'):
        column = input("Enter the column you would like to delete from:")
        record = input("Enter the value you would like to delete:")
        if (record == 'NULL') or (record == 'Null') or (record == 'null'):
            record = None
            tab1 = "DELETE FROM "+table.upper()+" WHERE "+column+"=(%s)"
            tup1 = (record,)
            return tab1, tup1
        else:
            tab1 = "DELETE FROM "+table.upper()+" WHERE "+column+"='"+record+"';"
            return tab1

    else:
        tab1 = "DELETE FROM "+table.upper()+";"
        return tab1
