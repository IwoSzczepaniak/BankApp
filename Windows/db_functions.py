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
        return e

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
        result = e
    finally:
        return result
