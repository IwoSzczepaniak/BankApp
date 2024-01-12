from classes import *
import os

db_name ="bank.db"

if __name__ == "__main__":
    if not os.path.exists(db_name): 
        print("Creating database...")
        sql_to_python(db_name, "Queries/create_tables.txt")
        sql_to_python(db_name, "Queries/inserts.txt")
        sql_to_python(db_name, "Queries/trig.txt", "//")
    
    # result = selects_to_python(db_name, "Queries/selects.txt")
    # print(result)

    start = WindowStart("Start")
    start.vis()