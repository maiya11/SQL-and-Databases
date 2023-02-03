import pandas as pd
import sqlite3
from queries import QUERY_LIST


def connect_to_db(db_name='buddymove_holidayiq.sqlite3'):
    return sqlite3.connect(db_name)


# df = pd.read_csv('buddymove_holidayiq.csv')
# df.to_sql(name='review', con=connect_to_db())

cursor = connect_to_db().cursor()


def execute_query(connection, query):
    cursor.execute(query)
    return cursor.fetchall()


def execute_multiple_queries(cursor, queries):
    answers = {}
    for index, query in enumerate():
        answers[index] = execute_query(cursor, query)
    return answers


if __name__ == '__main__':
    connection = connect_to_db()
    answers = execute_multiple_queries(cursor, QUERY_LIST)
    for key, value in enumerate(answers.values()):
        print(f'{key}: {value}')
