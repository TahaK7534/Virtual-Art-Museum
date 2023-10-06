def create_view():
    """
    Function to prompt a user to form a CREATE VIEW sql expression.
    
    Paramaters:
    None

    Returns: 
    expression: String of SQL create_view expression
        
    """
    table_name = input('Enter the name of the view you are creating: ')
    expression = f'DROP VIEW IF EXISTS {table_name}; CREATE VIEW '
    expression += table_name
    selections_n = int(
        input("How many attributes (selections of data) will this view have? "))
    select = []
    for i in range(selections_n):
        attribute_spec = input(
            "Would you like to specify the alias of the table which data selection " + str(i+1) + " is selected from? (Y/N) ")
        if attribute_spec == "Y" or attribute_spec == "y":
            spec = input("What is the alias of the table to be specified? ")
            attribute_name = input(
                "What is the name of data selection " + str(i+1) + "? ")
            select.append(spec + "." + attribute_name)
        if attribute_spec == "N":
            attribute_name = input(
                "What is the name of data selection " + str(i+1) + "? ")
            select.append(attribute_name)

    expression += " AS SELECT " + (', '.join(select)) + " FROM "
    from_n = int(input("How many tables will data be retrieved from? "))
    table = []
    for j in range(from_n):
        from_table = input("What is the name of table " + str(j+1) +
                           " (Enter table name with alias in the format 'table_name as alias')? ")
        table.append(from_table)

    expression += (', '.join(table)) + " "
    where = input(
        "Does the creation of your view require where conditions? (Y/N) ")
    if (where == 'Y') or (where == 'y'):
        query = input("Does the where condition involve another table? (Y/N) ")
        if (query == 'Y') or (query == 'y'):
            print("Please enter the information to find the table in your where condition, in the form of a query:")
            query_table = query_function()
            correlation_attribute = input(
                "Enter the attribute, with its alias, that you would like to correlate with this table: ")
            print(
                "Choose How You Woule Like to Correlate Them:\n1. IN\n2. EXISTS\n3. NOT EXISTS")
            correlation_method = int(
                input("Enter the number of your chose correlation method: "))
            if (correlation_method == 1):
                expression += "WHERE" + " " + correlation_attribute + \
                    " IN (" + query_table[:-1] + ")"
            elif (correlation_method == 2):
                expression += "WHERE" + " " + correlation_attribute + \
                    " EXISTS (" + query_table[:-1] + ")"
            elif (correlation_method == 3):
                expression += "WHERE" + " " + correlation_attribute + \
                    " NOT EXISTS (" + query_table[:-1] + ")"

            additional_where_conditions = []
            if_where = input(
                "Does your outer query statement have any other 'WHERE' conditions (enter either 'Y' or 'N'): ")
            if (if_where == 'Y') or (if_where == 'y'):
                num_where_conditions = int(
                    input("How many other 'WHERE' conditions does your outer query statement have: "))
                for w_cond in range(num_where_conditions):
                    w_cond = input(
                        "Enter a 'WHERE' condition (be sure to include aliases in front of any attributes): ")
                    additional_where_conditions.append(w_cond)

                expression += " " + "AND " + \
                    (' AND '.join(additional_where_conditions))
        else:
            where_conditions = []
            num_where_conditions = int(
                input("How many 'WHERE' conditions does your outer query statement have: "))
            for w_cond in range(num_where_conditions):
                w_cond = input(
                    "Enter a 'WHERE' condition (be sure to include aliases in front of any attributes): ")
                where_conditions.append(w_cond)
            expression += " WHERE " + (' AND '.join(where_conditions))

    expression += ";"
    return (expression)