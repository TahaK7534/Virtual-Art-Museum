def linked_query_segment():
    '''The purpose of this function is to generate an sql query that will query through the combination of two or more tables. This function will ask a series of easy to understand prompts, to gather information from the user for each queried table. Once the tables' queries are generated, the function will combine the table based on the users' choice.

    Arguments:
    None

    This function returns a query that will combine two or more tables, using their individual  queries, to the main Query function. 

    '''
    print("Choose how your query statements are combined:\n1. Union All\n2. Union Distinct\n3. Intersect All\n4. Intersect Distinct")
    combination_method = int(
        input("Enter the number of your chose combination method: "))
    query = ''
    print("Now You Will Enter the Information For Each Query Statement Being Combined")
    num_combined_statements = int(
        input("How many query statements are you going to combine: "))
    list_of_combined_query_statements = []
    for statement in range(num_combined_statements):
        tables = []
        num_tables = int(
            input("How many tables are in your query statement: "))

        if (num_tables == 2):
            if_join = input(
                "Are your tables joined (enter either 'Y' or 'N'): ")
            if (if_join == 'Y') or (if_join == 'y'):
                table1 = input("Enter the name of the first table: ")
                alias1 = input("Enter the alias of the first table: ")

                table2 = input("Enter the name of the second table: ")
                alias2 = input("Enter the alias of the second table: ")

                print(
                    "Choose one of the following join types: \n1. Join\n2. Natural Join\n3. Left Outer Join\n4. Right Outer Join")
                join_type = int(input(
                    "Enter the number of the join you chose: "))

                condition = input(
                    "Enter joining conditon in the form 'alias.condition1=alias.condition2': ")

                if (join_type == 1):
                    tables.append(
                        f'{table1} AS {alias1} JOIN {table2} AS {alias2} ON {condition}')
                elif (join_type == 2):
                    tables.append(
                        f'{table1} AS {alias1} NATURAL JOIN {table2} AS {alias2} ON {condition}')
                elif (join_type == 3):
                    tables.append(
                        f'{table1} AS {alias1} LEFT OUTER JOIN {table2} AS {alias2} ON {condition}')
                elif (join_type == 4):
                    tables.append(
                        f'{table1} AS {alias1} RIGHT OUTER JOIN {table2} AS {alias2} ON {condition}')
            else:
                for table in range(num_tables):
                    table = input("Enter the name of a table: ")
                    alias = input("Enter the alias of the table: ")
                    tables.append(f'{table} AS {alias}')
        else:
            for table in range(num_tables):
                table = input("Enter the name of a table: ")
                alias = input("Enter the alias of the table: ")
                tables.append(f'{table} AS {alias}')

        attributes = []
        num_attributes = int(input(
            "How many attributes are you looking for, excluding aggregate functions (Enter 00 of you are querying for all attributes): "))
        if_aggregate = input(
            "Does your query statement have aggregate functions (enter either 'Y' or 'N'): ")

        if (if_aggregate == 'Y') or (if_aggregate == 'y'):
            num_aggregate = int(
                input("Enter the number of aggregate functions in your statement: "))
            for aggregate in range(num_aggregate):
                aggregate = input(
                    "Enter an aggregate function in the form 'AGGREGATE_FUNCTION(attribute)': ")
                aggregate_alias = input(
                    "Enter the alias of your aggregate function: ")
                attributes.append(f'{aggregate} AS {aggregate_alias}')
            if (num_attributes == 00):
                attributes.append('*')
            elif (num_attributes != 0):
                for attribute in range(num_attributes):
                    attribute = input(
                        "Enter the name of your attribute in the form 'alias.attribute_name': ")
                    attributes.append(attribute)
        else:
            if (num_attributes == 00):
                attributes.append('*')
            elif (num_attributes != 0):
                for attribute in range(num_attributes):
                    attribute = input(
                        "Enter the name of an attribute (in the format 'alias.attribute_name'): ")
                    attributes.append(attribute)

        distinction = input(
            "Are any of your attributes distinct (enter either 'Y' or 'N'): ")
        if (distinction == 'Y') or (distinction == 'y'):
            statement += "SELECT DISTINCT" + ' ' + \
                (', '.join(attributes)) + ' ' + \
                "FROM" + ' ' + (', '.join(tables))
        else:
            statement += "SELECT" + ' ' + \
                (', '.join(attributes)) + ' ' + \
                "FROM" + ' ' + (', '.join(tables))

        where_conditions = []
        if_where = input(
            "Does your query statement have any 'WHERE' conditions (enter either 'Y' or 'N'): ")
        if (if_where == 'Y') or (if_where == 'y'):
            num_where_conditions = int(
                input("How many 'WHERE' conditions does your statement have: "))
            for w_cond in range(num_where_conditions):
                w_cond = input(
                    "Enter a 'WHERE' condition (be sure to include aliases in front of any attributes): ")
                where_conditions.append(w_cond)

            statement += ' ' + "WHERE" + ' ' + (' AND '.join(where_conditions))

        group_conditions = []
        if_group = input(
            "Does your query statement have any 'GROUP BY' attributes (enter either 'Y' or 'N'): ")
        if (if_group == 'Y') or (if_group == 'y'):
            num_group_conditions = int(
                input("How many 'GROUP BY' attributes does your statement have: "))
            for g_cond in range(num_group_conditions):
                g_cond = input(
                    "Enter a 'GROUP BY' attribute with their alias: ")
                group_conditions.append(g_cond)

            statement += ' ' + "GROUP BY" + ' ' + \
                (', '.join(group_conditions))

        having_conditions = []
        if_having = input(
            "Does your query statement have any 'HAVING' conditions (enter either 'Y' or 'N'): ")
        if (if_having == 'Y') or (if_having == 'y'):
            num_having_condition = int(
                input("How many 'HAVING' conditions does your statement have: "))
            for h_cond in range(num_having_condition):
                h_cond = input("Enter a 'HAVING' condition(s): ")
                having_conditions.append(h_cond)

            statement += ' ' + "HAVING" + ' ' + \
                (' AND '.join(having_conditions))

        order_conditions = []
        if_order = input(
            "Does your query statement have any 'ORDER BY' attributes (enter either 'Y' or 'N'): ")
        if (if_order == 'Y') or (if_order == 'y'):
            num_order_condition = int(
                input("How many 'ORDER BY' attributes does your statement have: "))
            for o_cond in range(num_order_condition):
                o_cond = input(
                    "Enter a 'ORDER BY' attribute with its alias and the order you are seeking: ")
                order_conditions.append(o_cond)

            statement += ' ' + "ORDER BY" + ' ' + (', '.join(order_conditions))

        list_of_combined_query_statements.append(statement)

    if (combination_method == 1):
        query += (' UNION ALL '.join(list_of_combined_query_statements))
    if (combination_method == 2):
        query += (' UNION DISTINCT '.join(list_of_combined_query_statements))
    if (combination_method == 3):
        query += (' INTERSECT ALL '.join(list_of_combined_query_statements))
    if (combination_method == 4):
        query += (' INTERSECT DISTINCT '.join(list_of_combined_query_statements))

    return query
