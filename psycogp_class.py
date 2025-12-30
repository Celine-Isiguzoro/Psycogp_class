import psycopg2

# db_conn = psycopg2.connect(
#     dbname = "sample_database",
#     user = "postgres",
#     password = "Password123"
# )
try:
    db_conn = psycopg2.connect(
        dbname = "testdb",
        user = "postgres",
        password = "Password123!",
        host = "localhost",
        port = "5432"
    )
except psycopg2.OperationalError as e: # When the database doesn't exist
    print("Could not connect to the database.")
    db_conn = psycopg2.connect(
        dbname = "postgres", #Connecting to the default database
        user = "postgres",
        password = "Nono2365",
        host = "localhost",
        port = "5432"
    )
    db_conn.autocommit = True # Allows to connect to the database in postgres and step out to create another database without leaving postgresql

    cur = db_conn.cursor() # to perform operations in the database
    cur.execute("CREATE DATABASE testdb;") # basically, the execute command in sql is used to write sql queries 
    cur.commit() # Establishes an attachment to avoid disposal
    cur.close() 
    db_conn.close() # Close the previous database to enable the use of the new database

    db_conn_new = psycopg2.connect(
        dbname = "testdb",
        user = "postgres",
        password = "Nono2365"
    )

finally:
    print("Successfully connnected to the new database")

cur = db_conn_new.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS users( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT
    CURRENT_TIMESTAMP
    ); 
    """) # Two constraints were given to email; it must be unique and not be found empty. Timestamp gives us the time and date in the column, created_at.

# IF NOT EXISTS saves us the stress of removing or commenting out the table. 
