# Step 0 - import sqlite3
import sqlite3
import queries as q

# DB Connect function


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(connection, query):
    # Make the "cursor"
    cursor = connection.cursor()

    # Execute the query
    cursor.execute(query)

    # Pull (and return) the results
    return cursor.fetchall()


if __name__ == '__main__':
    connection = connect_to_db()
    results = execute_query(connection, q.GET_CHARACTERS)
    print(results[:2])
