def create_table():
    """
    Function to prompt a user to form a CREATE TABLE sql expression.
    
    Paramaters:
    None

    Returns: 
    expression: String of SQL create_table expression
        
    """
    table_name = input('Enter the name of the table you are creating: ')
    expression = f"DROP TABLE IF EXISTS {table_name}; CREATE TABLE "
    expression += table_name
    copy = input("Does this table use data from other tables? (Y/N) ")
    if copy == "Y" or copy == "y":
        print("Please enter the information to find the table in you wish to retrieve data from, in the form of a query:")
        query_table = query_function()
        expression += " AS " + query_table
    else:
        attributes_n = int(
            input("How many attributes (columns) will this table have? "))
        attribute_list = []
        for i in range(attributes_n):
            attribute_name = input(
                "What is the name of attribute number " + str(i+1) + "? ")
            attribute = attribute_name
            attribute_data_type = str(
                input("What data type is " + attribute_name + "? "))
            attribute += " " + attribute_data_type + " "
            optional_parameters = input(
                "Will " + attribute_name + " accept null values? (Y/N) ")
            if optional_parameters == "N" or optional_parameters == "n":
                attribute += "NOT NULL "
            default = input(
                "Will you like to set a default value or this attribute? (Y/N) ")
            if default == 'Y' or default == 'y':
                default_val = input(
                    "What is the default value for this attribute? ")
                attribute += "Default " + default_val + " "
            attribute_list.append(attribute)
        expression += "(" + (', '.join(attribute_list))

        constraints = input("Would you like to enter any constraints? (Y/N): ")
        if constraints == 'Y' or constraints == 'y':
            expression += ", "
            num_constraints = int(
                input("Enter the number of constraints you would like to add: "))
            constraint_list = []
            for i in range(num_constraints):
                complete_constraint = "CONSTRAINT "
                constraint_name = input(
                    "Enter a label name for your contraint: ")
                complete_constraint += constraint_name + " "
                print(
                    "What type of constraint would you like to add:\n1. Primary Key\n2. Foreign Key\n3. Unique")
                constraint_type = int(
                    input("Enter the number of your selection: "))
                if (constraint_type == 1):
                    prim_key = input(
                        "Enter the name of your primary key attribute (if multiple attributes, enter them as comma seperated): ")
                    complete_constraint += "PRIMARY KEY (" + prim_key + ")"
                if (constraint_type == 2):
                    foreign = input("Enter the foreign key attribute: ")
                    reference = input(
                        "Enter the referenced table and attribute in the form 'TABLE_NAME(attribute_name)': ")
                    on_delete = input(
                        "Enter the action you would like to take on delete (i.e. Cascade): ")
                    on_update = input(
                        "Enter the action you would like to take on update (i.e. Cascade): ")
                    complete_constraint += "FOREIGN KEY (" + foreign + ") REFERENCES " + \
                        reference + " ON DELETE " + on_delete + " ON UPDATE " + on_update
                if (constraint_type == 3):
                    unique_val = input(
                        "Enter the name of your unique attribute (if multiple attributes, enter them as comma seperated): ")
                    complete_constraint += "UNIQUE (" + unique_val + ")"

                constraint_list.append(complete_constraint)

            expression += (', '.join(constraint_list))

        check = input(
            "Is there an attribute with a check condition you would like to implement? (Y/N) ")
        if check == "Y" or check == "y":
            expression += ", "
            checks = []
            check_n = int(
                input("How many check conditions would you like to enter? "))
            for k in range(check_n):
                if k == 0:
                    check_att = input(
                        "Enter the " + str(k+1) + " attribute and the condition (Ex: Age>=18): ")
                    checks.append(check_att)
                if k+1 > 1:
                    check_att = input(
                        "Enter the " + str(k+1) + " attribute and the condition (Ex: Age>=18): ")
                    checks.append(check_att)
            expression += "CHECK (" + (', '.join(checks)) + ")"

        expression += ");"
    return (expression)
