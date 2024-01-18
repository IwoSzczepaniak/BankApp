from Windows.start import *
import os

db_name ="bank.db"

if __name__ == "__main__":

    sql_to_python("Queries/drop_tab.sql")
    sql_to_python("Queries/create_tables.sql")
    sql_to_python("Queries/trig.sql")
    sql_to_python("Queries/inserts.sql")
   

    views_dir = "Queries/views/"
    for file in os.listdir(views_dir):
        sql_to_python(views_dir + file)
    
    start = WindowStart("Start")
    start.vis()
