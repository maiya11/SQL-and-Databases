import psycopg2
from gitignore import DBNAME, USER, PASSWORD, HOST
from queries import DROP_CHARACTER_TABLE, CREATE_CHARACTER_TABLE, INSERT_RYAN
# from module_1.sqlite_example import connect_to_db, execute_query
# from module_1.queries import GET_CHARACTERS
# Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(
    dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)

# A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()

if __name__ == '__main__':
    # sl_connection = connect_to_db()
    # sl_characters = execute_query(sl_connection, GET_CHARACTERS)
    # print(sl_characters[5:])

    cursor.execute(DROP_CHARACTER_TABLE)
    cursor.execute(CREATE_CHARACTER_TABLE)
    cursor.execute(INSERT_RYAN)
    connection.commit()
