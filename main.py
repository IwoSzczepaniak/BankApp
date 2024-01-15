from Windows.start import *
import os

db_name ="bank.db"

if __name__ == "__main__":
    # TODO clear db

    sql_to_python("Queries/create_tables.txt")
    sql_to_python("Queries/inserts.txt")
    sql_to_python("Queries/trig.txt")
    
    start = WindowStart("Start")
    start.vis()
