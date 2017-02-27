# Daniel Brown
# dsb9ef
import csv
import psycopg2


PG_USER = "postgres"
PG_USER_PASS = "6616"
PG_DATABASE = "mydb1"
PG_HOST_INFO = "" # use "" for OS X or Windows


def load_course_database(db_name, csv_filename):
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS coursedata;")
    cur.execute("CREATE TABLE coursedata (deptID text, courseNum int,semester int,meetingType text,seatsTaken int,seatsOffered int, instructor text);")
    # Execute a command: this creates a new table, but first removes it if it's there already

   # print("** Created table.")

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
  #  cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
   # print("** Exectuted SQL INSERT into database.")

    # Query the database and obtain data as Python objects
  # cur.execute("SELECT * FROM test;")
 #   print("** Output from SQL SELECT: ", cur.fetchone())

    # Make the changes to the database persistent


    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO coursedata (deptid, coursenum, semester, meetingtype,seatstaken, seatsoffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3] , row[4] , row[5], row[6]))



    # Make the changes to the database persistent

    cur.execute("SELECT * from coursedata;")
    print(cur.fetchall())
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    print("** Closed connection and database.  Bye!.")

if __name__ == "__main__":
    load_course_database("course1", "seas-courses-5years.csv")

