https://sqlite.org/cli.html

General SQLite Information:
    -Storage classes used:
        null - Null value
        int - Signed integer stored in 0-8 bytes depending on magnitude
        real - Floating point value
        text - Text string, stored using database encoding
        blob - BLOB (binary large object: up to several gigabytes) of data stored exactly as it was input

    -SQL statements/commands need to be terminated with a semicolon
        If you don't input a semicolon and just press ENTER, sqlite3 will extend your command to the next line, allowing you to write multiline commands.

To open SQLite3 Shell:
    Type "sqlite3 (FILE_NAME)" in terminal. 
    -This creates a new SQLite database named "(FILE_NAME)"
    -If no file name is specified then a temporary database is created, which will be deleted when you exit the "sqlite3" program

After creating the database:
    To create a table:
        create table <TABLE_NAME>(<COLUMN_NAME> <DATA_TYPE>);
            Ex: create table tbl1(one text, two int) 
                #Creates table with 2 columns, with first being text values and second being int values

    To insert values into the table:
        insert into <TABLE_NAME> values(<VALUE>);
            Ex: insert into tbl1 values('hello!',10);
                #Inserts 'hello!' into the first column of tbl1 and 10 into the second column.
    
    To select column(s) from the table:
        select < * or <COLUMN_NAME> > from <TABLE_NAME>
            Ex: select * from tbl1
                #Selects all columns from tbl1
            Ex: select 2 from tbl1
                #Selects column 2 from tbl1
