def alter_function():
    """
    a function to resquest a SQL alter function

    Parameters:
    None
    
    Return:
    alter: a string with the selected SQL operation
    """

    print("You have selected to alter the existing data set")

    alter = "ALTER TABLE "

    table_name = input("What is the name of the table you wish to alter?\n")

    alter += table_name

    check = 0
    while (check == 0):
        print("Would you like to ADD COLUMN(1),  DROP COLUMN (2),  MODIFY COLUMN(3),  ADD CONSTRAINT (4), or DELETE CONSTRAINT (5) in the " + table_name + " table")
        val = int(input("Enter your selection: "))

        if (val == 1):

            alter += " ADD COLUMN "
            colum_name = input(
                "What is the name of the column you wish to add ?\n")
            alter += colum_name
            datatype = input(
                "What is the data type of the column you wish to add ex.) VARCHAR(15) or CHAR(15) or BINARY(15)? \n")
            alter += " "
            alter += datatype
            alter += ";"
            check = 1

        elif (val == 2):

            alter += " DROP COLUMN "
            colum_name = input(
                "What is the name of the column you wish to drop ?\n")
            alter += colum_name
            
            
            C_R = int(input("Would you like to CASCADE(1)  RESTRICT (2) or nither(any other number)\n"))
            if (C_R == 1):
                alter += " CASCADE" 
            
            elif (C_R == 2):
                alter += " RESTRICT" 
            
            alter += ";"
            check = 1

        elif (val == 3):

            alter += " MODIFY COLUMN "

            colum_name = input(
                "What is the name of the column you wish to modify ?\n")
            alter += colum_name
                        
            D_S = int(input("Would you like to SET DEFAULT(1) or DROP DEFAULT(2) or change data type(any other number)\n"))
            if (D_S == 1):
                alter += " SET DEFAULT "
                default = input("What value would you like to set for default\n")
                alter += "'" + default + "'"

            elif (D_S == 2):
                alter += " DROP DEFAULT" 
            
            else:
                datatype = input("What is the new data type of this colum ex.) VARCHAR(15) or CHAR(15) or BINARY(15)?\n")
                alter += " "
                alter += datatype

            alter += ";"
            check = 1


        elif (val == 4):
            alter += " ADD CONSTRAINT "
            constraint_name = input(
                "What is the name of the constraint you wish to add ?\n")
            alter += " " + constraint_name + " "
            print("Would you like to Add PRIMARY KEY CONSTRAINT(1), UNIQUE KEY CONSTRAINT (2),  FOREIGN KEY CONSTRAINT(3) in the " + table_name + " table")
            constraint_val = int(input("Enter your selection: "))
            if (constraint_val == 1):
                primary = input(
                    "Enter the attribute(s) you would like to make a primary key (seperate by comma if multiples): ")
                alter += "PRIMARY KEY (" + primary + ");"
                check = 1
            elif (constraint_val == 2):
                unique = input(
                    "Enter the attribute(s) you would like to make a unique key (seperate by comma if multiples): ")
                alter += "UNIQUE (" + unique + ");"
                check = 1
            elif (constraint_val == 3):
                foreign = input(
                    "Enter the attribute you would like to make a foreign key: ")
                alter += "FOREIGN KEY (" + foreign + ") "
                reference = input(
                    "Enter the attribute and table you would like the foreign key to reference, in the format 'TABLE_NAME(attribute_name)': ")
                alter += reference
            
                print(
                    "What action would you like to take on delete: CASCADE(1), SET NULL(2), or NO ACTION(any other value): ")
                delete_action = int(input("Enter your selection: "))
                if (delete_action == 1):
                    alter += " ON DELETE CASCADE "
                elif (delete_action == 2):
                    alter += " ON DELETE SET NULL "
                else:
                    alter += " ON DELETE NO ACTION "

                print(
                    "What action would you like to take on update: CASCADE(1), SET NULL(2), or NO ACTION(3): ")
                update_action = int(input("Enter your selection: "))
                if (update_action == 1):
                    alter += " ON UPDATE CASCADE;"
                elif (update_action == 2):
                    alter += " ON UPDATE SET NULL;"
                if (update_action == 3):
                    alter += " ON UPDATE NO ACTION;"

                check = 1

        elif (val == 5):
            alter += " DELETE CONSTRAINT"
            constraint_name = input(
                "What is the name of the constraint you wish to delete ?\n")
            alter += " " + constraint_name + ";"
            check = 1
        else:
            print(
                "You did not chose one of the options,1 ,2, 3, 4, or 5\n Please try again")

    return alter
