import psycopg2

def connect():
    return psycopg2.connect(
        host = "localhost", 
        database = "Bank",
        user = "postgres",
        password = "BazyProjekt12", 
        port = "5432",
        )

def execute_sql_query(query_text):
    try:
        with connect() as connection, connection.cursor() as cursor:
            cursor.execute(query_text)
            connection.commit()
    except Exception as e:
        print(e)
        print(query_text)
        print()
        return query_text

def sql_to_python(filename):
    with open(filename, 'r') as file:
        command = file.read()
    execute_sql_query(command)

def get_select(query_text):
    try:
        with connect() as connection, connection.cursor() as cursor:
            cursor.execute(query_text)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        print(query_text)
        print()
        result = None
    finally:
        return result


# # currently not used
# def selects_to_python(db_name:str, filename:str, separator:str = ';'):
#         with open(filename, 'r') as file:
#             content = file.read().split(separator)
#         result = []
#         for command in content:
#             res = get_select(db_name, command)
#             if len(res)>0: 
#                 result.append(res)

#         return result
