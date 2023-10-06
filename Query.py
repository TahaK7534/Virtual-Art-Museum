from Nested_Query import *
from Linked_Query import *


def query_function():
    ''' The purpose of this function is to generate an sql statement that can be used to query a database and find information based on that query. This function will ask the user a series of easy to understand prompts, which the user will input information into as a way to generate the query. This function imports the Nested_Query function and the Linked_Query function to assist in generating the query.

    Arguments:
    None

    This function returns an SQL string that can be executed to find specific information in the Database.

    '''
    query_type = int(
        input("Enter 1 For a Basic Query, 2 For a Nested Query, or 3 For a Linked Query: "))
    query = ''

    if (query_type == 1):

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
            query += "SELECT DISTINCT" + ' ' + \
                (', '.join(attributes)) + ' ' + \
                "FROM" + ' ' + (', '.join(tables))
        else:
            query += "SELECT" + ' ' + \
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

            query += ' ' + "WHERE" + ' ' + (' AND '.join(where_conditions))

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

            query += ' ' + "GROUP BY" + ' ' + (', '.join(group_conditions))

        having_conditions = []
        if_having = input(
            "Does your query statement have any 'HAVING' conditions (enter either 'Y' or 'N'): ")
        if (if_having == 'Y') or (if_having == 'y'):
            num_having_condition = int(
                input("How many 'HAVING' conditions does your statement have: "))
            for h_cond in range(num_having_condition):
                h_cond = input("Enter a 'HAVING' condition(s): ")
                having_conditions.append(h_cond)

            query += ' ' + "HAVING" + ' ' + (' AND '.join(having_conditions))

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

            query += ' ' + "ORDER BY" + ' ' + (', '.join(order_conditions))

        query += ';'
        return query

    elif (query_type == 2):
        nested_query_line = int(input(
            "Enter 1 if the nested query will be in the 'FROM' statement, enter 2 if it will be in the 'WHERE' statement: "))
        nested_query = nested_query_segment()
        print("Now that the nested query information has been collected, please enter the information for the outer query statement.")

        if (nested_query_line == 1):
            tables = []
            more_tables = input(
                "Are any other tables a part of your outer query statement (enter either 'Y' or 'N'): ")
            if (more_tables == 'Y') or (more_tables == 'y'):
                num_tables = int(
                    input("How many other table are you querying: "))

                if_join = input(
                    "Is your table joined with your nested query statement (enter either 'Y' or 'N'): ")
                if (if_join == 'Y') or (if_join == 'y'):
                    table1 = input("Enter the name of the table: ")
                    alias1 = input("Enter the alias of the table: ")

                    print(
                        "Choose one of the following join types: \n1. Join\n2. Natural Join\n3. Left Outer Join\n4. Right Outer Join")
                    join_type = int(input(
                        "Enter the number of the join you chose: "))

                    condition = input(
                        "Enter joining conditon in the form 'alias.condition1=alias.condition2': ")

                    if (join_type == 1):
                        tables.append(
                            f'{table1} AS {alias1} JOIN {nested_query} ON {condition}')
                    elif (join_type == 2):
                        tables.append(
                            f'{table1} AS {alias1} NATURAL JOIN {nested_query} ON {condition}')
                    elif (join_type == 3):
                        tables.append(
                            f'{table1} AS {alias1} LEFT OUTER JOIN {nested_query} ON {condition}')
                    elif (join_type == 4):
                        tables.append(
                            f'{table1} AS {alias1} RIGHT OUTER JOIN {nested_query} ON {condition}')
                else:
                    for table in range(num_tables):
                        table = input("Enter the name of a table: ")
                        alias = input("Enter the alias of the table: ")
                        tables.append(f'{table} AS {alias}')
                    tables.append(nested_query)
            else:
                tables.append(nested_query)

            attributes = []
            num_attributes = int(input(
                "How many attributes are you looking for in your outer query statement, excluding aggregate functions (Enter 00 of you are querying for all attributes): "))
            if_aggregate = input(
                "Does your outer query statement have aggregate functions (enter either 'Y' or 'N'): ")

            if (if_aggregate == 'Y') or (if_aggregate == 'y'):
                num_aggregate = int(
                    input("Enter the number of aggregate functions in your outer query statement: "))
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
                query += "SELECT DISTINCT" + ' ' + \
                    (', '.join(attributes)) + ' ' + \
                    "FROM" + ' ' + (', '.join(tables))
            else:
                query += "SELECT" + ' ' + \
                    (', '.join(attributes)) + ' ' + \
                    "FROM" + ' ' + (', '.join(tables))

            where_conditions = []
            if_where = input(
                "Does your outer query statement have any 'WHERE' conditions (enter either 'Y' or 'N'): ")
            if (if_where == 'Y') or (if_where == 'y'):
                num_where_conditions = int(
                    input("How many 'WHERE' conditions does your outer query statement have: "))
                for w_cond in range(num_where_conditions):
                    w_cond = input(
                        "Enter a 'WHERE' condition (be sure to include aliases in front of any attributes): ")
                    where_conditions.append(w_cond)

                query += ' ' + "WHERE" + ' ' + (' AND '.join(where_conditions))

            group_conditions = []
            if_group = input(
                "Does your outer query statement have any 'GROUP BY' attributes (enter either 'Y' or 'N'): ")
            if (if_group == 'Y') or (if_group == 'y'):
                num_group_conditions = int(
                    input("How many 'GROUP BY' attributes does your outer query statement have: "))
                for g_cond in range(num_group_conditions):
                    g_cond = input(
                        "Enter a 'GROUP BY' attribute with their alias: ")
                    group_conditions.append(g_cond)

                query += ' ' + "GROUP BY" + ' ' + \
                    (', '.join(group_conditions))

            having_conditions = []
            if_having = input(
                "Does your outer query statement have any 'HAVING' conditions (enter either 'Y' or 'N'): ")
            if (if_having == 'Y') or (if_having == 'y'):
                num_having_condition = int(
                    input("How many 'HAVING' conditions does your outer query statement have: "))
                for h_cond in range(num_having_condition):
                    h_cond = input("Enter a 'HAVING' condition(s): ")
                    having_conditions.append(h_cond)

                query += ' ' + "HAVING" + ' ' + \
                    (' AND '.join(having_conditions))

            order_conditions = []
            if_order = input(
                "Does your outer query statement have any 'ORDER BY' attributes (enter either 'Y' or 'N'): ")
            if (if_order == 'Y') or (if_order == 'y'):
                num_order_condition = int(
                    input("How many 'ORDER BY' attributes does your outer query statement have: "))
                for o_cond in range(num_order_condition):
                    o_cond = input(
                        "Enter a 'ORDER BY' attribute with its alias and the order you are seeking: ")
                    order_conditions.append(o_cond)

                query += ' ' + "ORDER BY" + ' ' + (', '.join(order_conditions))

            query += ';'
            return query

        elif (nested_query_line == 2):
            tables = []
            num_tables = int(
                input("How many tables are in your outer query statement: "))

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
                "How many attributes are you looking for in your outer query statement, excluding aggregate functions (Enter 00 of you are querying for all attributes): "))
            if_aggregate = input(
                "Does your outer query statement have aggregate functions (enter either 'Y' or 'N'): ")

            if (if_aggregate == 'Y') or (if_aggregate == 'y'):
                num_aggregate = int(
                    input("Enter the number of aggregate functions in your outer query statement: "))
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
                query += "SELECT DISTINCT" + ' ' + \
                    (', '.join(attributes)) + ' ' + \
                    "FROM" + ' ' + (', '.join(tables))
            else:
                query += "SELECT" + ' ' + \
                    (', '.join(attributes)) + ' ' + \
                    "FROM" + ' ' + (', '.join(tables))

            where_conditions = []
            correlation_attribute = input(
                "Enter the attribute, with its alias, that you would like to correlate with the nested query in your WHERE statement: ")
            where_conditions.append(correlation_attribute)
            where_conditions.append(nested_query)
            print(
                "Choose How You Woule Like to Correlate Them:\n1. IN\n2. EXISTS\n3. NOT EXISTS")
            correlation_method = int(
                input("Enter the number of your chose correlation method: "))
            if (correlation_method == 1):
                query += ' ' + "WHERE" + ' ' + (' IN '.join(where_conditions))
            elif (correlation_method == 2):
                query += ' ' + "WHERE" + ' ' + \
                    (' EXISTS '.join(where_conditions))
            elif (correlation_method == 3):
                query += ' ' + "WHERE" + ' ' + \
                    (' NOT EXISTS '.join(where_conditions))

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

                query += ' ' + "AND" + ' ' + \
                    (' AND '.join(additional_where_conditions))

            group_conditions = []
            if_group = input(
                "Does your outer query statement have any 'GROUP BY' attributes (enter either 'Y' or 'N'): ")
            if (if_group == 'Y') or (if_group == 'y'):
                num_group_conditions = int(
                    input("How many 'GROUP BY' attributes does your outer query statement have: "))
                for g_cond in range(num_group_conditions):
                    g_cond = input(
                        "Enter a 'GROUP BY' attribute with their alias: ")
                    group_conditions.append(g_cond)

                query += ' ' + "GROUP BY" + ' ' + \
                    (', '.join(group_conditions))

            having_conditions = []
            if_having = input(
                "Does your outer query statement have any 'HAVING' conditions (enter either 'Y' or 'N'): ")
            if (if_having == 'Y') or (if_having == 'y'):
                num_having_condition = int(
                    input("How many 'HAVING' conditions does your outer query statement have: "))
                for h_cond in range(num_having_condition):
                    h_cond = input("Enter a 'HAVING' condition(s): ")
                    having_conditions.append(h_cond)

                query += ' ' + "HAVING" + ' ' + \
                    (' AND '.join(having_conditions))

            order_conditions = []
            if_order = input(
                "Does your outer query statement have any 'ORDER BY' attributes (enter either 'Y' or 'N'): ")
            if (if_order == 'Y') or (if_order == 'y'):
                num_order_condition = int(
                    input("How many 'ORDER BY' attributes does your outer query statement have: "))
                for o_cond in range(num_order_condition):
                    o_cond = input(
                        "Enter a 'ORDER BY' attribute with its alias and the order you are seeking: ")
                    order_conditions.append(o_cond)

                query += ' ' + "ORDER BY" + ' ' + (', '.join(order_conditions))

            query += ';'
            return query

    elif (query_type == 3):
        linked_query = linked_query_segment()
        query += linked_query + ';'
        return query
