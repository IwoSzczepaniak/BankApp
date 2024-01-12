import sqlite3

def execute_sql_querry(db_name:str, querry_text:str):
    conn = sqlite3.connect(db_name)

    conn.execute(querry_text)
    
    conn.commit()
    conn.close()

def sql_to_python(filename:str, database:str):
         with open(filename, 'r') as file:
             content = file.read().split(';')
         for command in content:
            try:    
                execute_sql_querry(database, command)
            except Exception as e:
                print(e)
                print(command)
                print()

def direct_sql_to_python(filename:str, database:str):
         with open(filename, 'r') as file:
             content = file.read().split("//")
         for command in content:
            try:    
                execute_sql_querry(database, command)
            except Exception as e:
                print(e)
                print(command)
                print()