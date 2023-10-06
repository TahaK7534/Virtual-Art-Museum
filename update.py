def update_function():
    """
    a function to resquest a SQL update function

    Parameters:
    None
    
    Return:
    update: a string with the selected SQL operation
    """


    print("You have selected to update an existing table")
    update = "UPDATE "

    table_name = input("What is the Name of the table you wish to update?\n")
    update += table_name
    update += " SET "

    check = 1
    while (check == 1):
        colum_number = input("How many columns do you wish to update?\n")

        if (colum_number.isnumeric() == True):
            check = 0
        else:
            print("You did not enter a number please try agin")

    colum_number = int(colum_number)
    while (colum_number > 0):
        colum_name = input(
            "What is the name of the column you wish to update\n")
        colum_new_value = input(
            "What is the new value you wish to set for this column\n")
        update += colum_name
        update += " = "
        update += "'"
        update += colum_new_value
        update += "'"
        if (colum_number > 1):
            update += ", "
        colum_number = colum_number - 1

    where_conditions = []
    if_where = input(
        "Does your query statement have any 'WHERE' conditions (enter either 'Y' for yes or anything esle for No): ")
    if (if_where == 'Y' or if_where == 'y'):
        num_where_conditions = int(
            input("How many 'WHERE' conditions does your statement have: "))
        for w_cond in range(num_where_conditions):
            w_cond = input(
                "Enter a 'WHERE' condition (be sure to include any necessary aliases in front of any attributes): ")
            where_conditions.append(w_cond)

        update += ' ' + "WHERE" + ' ' + (' AND '.join(where_conditions))
        update += ';'
    else:
        update += ";"
    return update
