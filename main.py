from classes import *
import os

db_name ="bank.db"

if __name__ == "__main__":
    create_db = True
    if os.path.exists(db_name): 
        create_db = False

    
    if create_db: 
        sql_to_python("Querries/create_tables.txt",db_name)
        sql_to_python("Querries/inserts.txt",db_name)
    direct_sql_to_python("Querries/trig.txt",db_name)
    
    sql_to_python("Querries/selects.txt",db_name)
