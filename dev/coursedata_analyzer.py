# Daniel Brown
# dsb9ef

import csv
import psycopg2


PG_USER = "postgres"
PG_USER_PASS = "6616"
PG_DATABASE = "mydb1"
PG_HOST_INFO = "" # use "" for OS X or Windows

def instructor_numbers(dept_id):
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("SELECT * FROM coursedata WHERE deptid = '" + dept_id + "';")
    d={}
    for course in cur.fetchall():
        d[course[6]] = course[4]
    return d

if __name__=="__main__":
    print(instructor_numbers("CS"))
