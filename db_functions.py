import sqlite3

def execute_sql_querry(db_name:str, query_text:str):
    conn = sqlite3.connect(db_name)
    conn.execute(query_text)
    conn.commit()
    conn.close()

def sql_to_python(db_name:str, filename:str, separator:str = ';'):
         with open(filename, 'r') as file:
             content = file.read().split(separator)
         for command in content:
            try:    
                execute_sql_querry(db_name, command)
            except Exception as e:
                print(e)
                print(command)
                print()

def get_select(db_name:str, query_text:str):
    conn = sqlite3.connect(db_name)
    cursor = conn.execute(query_text)
    result = cursor.fetchall()

    conn.close()
    return result

def selects_to_python(db_name:str, filename:str, separator:str = ';'):
        with open(filename, 'r') as file:
            content = file.read().split(separator)
        result = []
        for command in content:
            try:
                res = get_select(db_name, command)
                if len(res)>0: 
                    result.append(res)
            except Exception as e:
                print(e)
                print(command)
                print()
        return result
