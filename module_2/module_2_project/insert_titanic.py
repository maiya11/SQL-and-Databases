import psycopg2
from data import DBNAME, USER, PASSWORD, HOST
import queries as q
import pandas as pd

# Create database with data to be transferred to PostgreSQL
data = pd.read_csv('titanic.csv')
df = pd.DataFrame(data)

# Establish connection to PostgreSQL


def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    connection = psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    cursor = connection.cursor()
    return connection, cursor

# Create function to modify table in PostgreSQL


def modify_db(connection, cursor, query):
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':

    # Create table
    pg_connection, pg_cursor = connect_to_pg()
    for query in q.INITIAL_QUERIES_LIST:
        modify_db(pg_connection, pg_cursor, query)

   # Populate table with values from df
    for row in df.iterrows():

        # To account for names that have apostrophes in them
        if "'" in row[1][2]:
            row[1][2] = row[1][2].replace("'", "''")

        modify_db(pg_connection, pg_cursor,
                  f'''
                    INSERT INTO titanic("name", "sex", "age", "fare", "siblings_spouses_aboard",
                    "parents_children_aboard", "passenger_class", "survived")
                    VALUES ('{row[1][2]}', '{row[1][3]}', {row[1][4]}, {row[1][7]}, {row[1][5]}, 
                    {row[1][6]}, '{row[1][1]}', '{row[1][0]}');
                    '''
                  )
