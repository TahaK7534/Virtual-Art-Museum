def nested_query_segment():
    ''' The purpose of this functions is to assist the Query function in generating an sql query for querying the database. This function will use a series of easy to understand prompts to get information from the user and use that information to create the inner query,

    Arguments:
    None

    This function returns a query that will act as the "inner" query when nested with the outer query generated by the main Query function.

    '''
    num_nested_query = int(
        input("How many nested queries does your query statement have: "))
    query = ''

    if (num_nested_query == 1):
        tables = []
        num_tables = int(
            input("How many tables are in your nested query statement: "))

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
            "How many attributes are you looking for, excluding aggregate functions, in your nested query statement (Enter 00 of you are querying for all attributes): "))
        if_aggregate = input(
            "Does your nested query statement  have aggregate functions (enter either 'Y' or 'N'): ")

        if (if_aggregate == 'Y') or (if_aggregate == 'y'):
            num_aggregate = int(
                input("Enter the number of aggregate functions in your nested query statement: "))
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
            query += "(SELECT DISTINCT" + ' ' + \
                (', '.join(attributes)) + ' ' + \
                "FROM" + ' ' + (', '.join(tables))
        else:
            query += "(SELECT" + ' ' + \
                (', '.join(attributes)) + ' ' + \
                "FROM" + ' ' + (', '.join(tables))

        where_conditions = []
        if_where = input(
            "Does your nested query statement have any 'WHERE' conditions (enter either 'Y' or 'N'): ")
        if (if_where == 'Y') or (if_where == 'y'):
            num_where_conditions = int(
                input("How many 'WHERE' conditions does your nested query statement have: "))
            for w_cond in range(num_where_conditions):
                w_cond = input(
                    "Enter a 'WHERE' condition (be sure to include aliases in front of any attributes): ")
                where_conditions.append(w_cond)

            query += ' ' + "WHERE" + ' ' + (' AND '.join(where_conditions))

        group_conditions = []
        if_group = input(
            "Does your nested query statement have any 'GROUP BY' attributes (enter either 'Y' or 'N'): ")
        if (if_group == 'Y') or (if_group == 'y'):
            num_group_conditions = int(
                input("How many 'GROUP BY' attributes does your nested query statement have: "))
            for g_cond in range(num_group_conditions):
                g_cond = input(
                    "Enter a 'GROUP BY' attribute with their alias: ")
                group_conditions.append(g_cond)

            query += ' ' + "GROUP BY" + ' ' + (', '.join(group_conditions))

        having_conditions = []
        if_having = input(
            "Does your nested query statement have any 'HAVING' conditions (enter either 'Y' or 'N'): ")
        if (if_having == 'Y') or (if_having == 'y'):
            num_having_condition = int(
                input("How many 'HAVING' conditions does your nested query statement have: "))
            for h_cond in range(num_having_condition):
                h_cond = input("Enter a 'HAVING' condition(s): ")
                having_conditions.append(h_cond)

            query += ' ' + "HAVING" + ' ' + (' AND '.join(having_conditions))

        order_conditions = []
        if_order = input(
            "Does your nested query statement have any 'ORDER BY' attributes (enter either 'Y' or 'N'): ")
        if (if_order == 'Y') or (if_order == 'y'):
            num_order_condition = int(
                input("How many 'ORDER BY' attributes does your nested query statement have: "))
            for o_cond in range(num_order_condition):
                o_cond = input(
                    "Enter a 'ORDER BY' attribute with its alias and the order you are seeking: ")
                order_conditions.append(o_cond)

            query += ' ' + "ORDER BY" + ' ' + (', '.join(order_conditions))

        if_alias = input(
            "Does your nested query need an alias (Enter either 'Y' or 'N'): ")
        if (if_alias == 'Y') or (if_alias == 'y'):
            nested_alias = input("Give an alias to the nested query: ")
            query += ')' + ' ' + 'AS' + ' ' + nested_alias
        else:
            query += ')'
        return query

    elif (num_nested_query > 1):
        print("Choose how your nested query statements are combined:\n1. Union All\n2. Union Distinct\n3. Intersect All\n4. Intersect Distinct")
        connection = int(
            input("Enter the Number of your chosen Combination: "))
        query += '('
        list_of_nested_queries = []
        for nest_query in range(num_nested_query):
            nest_query = ''
            tables = []
            num_tables = int(
                input("How many tables are in your nested query statement: "))

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
                "How many attributes are you looking for, excluding aggregate functions, in your nested query statement (Enter 00 of you are querying for all attributes): "))
            if_aggregate = input(
                "Does your nested query statement have aggregate functions (enter either 'Y' or 'N'): ")

            if (if_aggregate == 'Y') or (if_aggregate == 'y'):
                num_aggregate = int(
                    input("Enter the number of aggregate functions in your nested query statement: "))
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
                nest_query += "SELECT DISTINCT" + ' ' + \
                    (', '.join(attributes)) + ' ' + \
                    "FROM" + ' ' + (', '.join(tables))
            else:
                nest_query += "SELECT" + ' ' + \
                    (', '.join(attributes)) + ' ' + \
                    "FROM" + ' ' + (', '.join(tables))

            where_conditions = []
            if_where = input(
                "Does your nested query statement have any 'WHERE' conditions (enter either 'Y' or 'N'): ")
            if (if_where == 'Y') or (if_where == 'y'):
                num_where_conditions = int(
                    input("How many 'WHERE' conditions does your nested query statement have: "))
                for w_cond in range(num_where_conditions):
                    w_cond = input(
                        "Enter a 'WHERE' condition (be sure to include aliases in front of any attributes): ")
                    where_conditions.append(w_cond)

                nest_query += ' ' + "WHERE" + ' ' + \
                    (' AND '.join(where_conditions))

            group_conditions = []
            if_group = input(
                "Does your nested query statement have any 'GROUP BY' attributes (enter either 'Y' or 'N'): ")
            if (if_group == 'Y') or (if_group == 'y'):
                num_group_conditions = int(
                    input("How many 'GROUP BY' attributes does your nested query statement have: "))
                for g_cond in range(num_group_conditions):
                    g_cond = input(
                        "Enter a 'GROUP BY' attribute with their alias: ")
                    group_conditions.append(g_cond)

                nest_query += ' ' + "GROUP BY" + ' ' + \
                    (', '.join(group_conditions))

            having_conditions = []
            if_having = input(
                "Does your nested query statement have any 'HAVING' conditions (enter either 'Y' or 'N'): ")
            if (if_having == 'Y') or (if_having == 'y'):
                num_having_condition = int(
                    input("How many 'HAVING' conditions does your nested query statement have: "))
                for h_cond in range(num_having_condition):
                    h_cond = input("Enter a 'HAVING' condition(s): ")
                    having_conditions.append(h_cond)

                nest_query += ' ' + "HAVING" + ' ' + \
                    (' AND '.join(having_conditions))

            order_conditions = []
            if_order = input(
                "Does your nested query statement have any 'ORDER BY' attributes (enter either 'Y' or 'N'): ")
            if (if_order == 'Y') or (if_order == 'y'):
                num_order_condition = int(
                    input("How many 'ORDER BY' attributes does your nested query statement have: "))
                for o_cond in range(num_order_condition):
                    o_cond = input(
                        "Enter a 'ORDER BY' attribute with its alias and the order you are seeking: ")
                    order_conditions.append(o_cond)

                nest_query += ' ' + "ORDER BY" + \
                    ' ' + (', '.join(order_conditions))

            list_of_nested_queries.append(nest_query)

        if (connection == 1):
            query += (' UNION ALL '.join(list_of_nested_queries))
        elif (connection == 2):
            query += (' UNION DISTINCT '.join(list_of_nested_queries))
        elif (connection == 3):
            query += (' INTERSECT ALL '.join(list_of_nested_queries))
        elif (connection == 4):
            query += (' INTERSECT DISTINCT '.join(list_of_nested_queries))

        if_alias = input(
            "Does your nested query need an alias (Enter either 'Y' or 'N'): ")
        if (if_alias == 'Y') or (if_alias == 'y'):
            nested_alias = input("Give an alias to the nested query: ")
            query += ')' + ' ' + 'AS' + ' ' + nested_alias
        else:
            query += ')'
        return query
