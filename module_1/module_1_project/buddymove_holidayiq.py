import pandas as pd
import sqlite3
import queries as q


def connect_to_db(db_name='buddymove_holidayiq.sqlite3'):
    return sqlite3.connect(db_name)


# df = pd.read_csv('buddymove_holidayiq.csv')
# df.to_sql(name='review', con=connect_to_db())


def execute_query(connection, query):
    # Make the "cursor"
    cursor = connection.cursor()

    # Execute the query
    cursor.execute(query)

    # Pull (and return) the results
    return cursor.fetchall()


if __name__ == '__main__':
    connection = connect_to_db()
    results = execute_query(connection, q.NUM_ROWS)
    print(results[:5])
