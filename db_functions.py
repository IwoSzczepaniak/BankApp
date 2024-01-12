import sqlite3

def execute_sql_querry(db_name:str, query_text:str):
    try:
        conn = sqlite3.connect(db_name)
        conn.execute(query_text)
        conn.commit()
    except Exception as e:
                    print(e)
                    print(query_text)
                    print()
    finally:
        conn.close()

def sql_to_python(db_name:str, filename:str, separator:str = ';'):
         with open(filename, 'r') as file:
             content = file.read().split(separator)
         for command in content:
            execute_sql_querry(db_name, command)

def get_select(db_name:str, query_text:str):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.execute(query_text)
        result = cursor.fetchall()
    except Exception as e:
                print(e)
                print(query_text)
                print()
                result = None
    finally:
        conn.close()
        return result

# currently not used
def selects_to_python(db_name:str, filename:str, separator:str = ';'):
        with open(filename, 'r') as file:
            content = file.read().split(separator)
        result = []
        for command in content:
            res = get_select(db_name, command)
            if len(res)>0: 
                result.append(res)

        return result
