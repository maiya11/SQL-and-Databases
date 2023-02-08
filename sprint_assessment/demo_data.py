import sqlite3

connection = sqlite3.connect('demo_data.sqlite3')
cursor = connection.cursor()


def execute_query(connection, query):
    cursor.execute(query)
    return cursor.fetchall()


CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS demo
        (
        "S" VARCHAR(10) NOT NULL PRIMARY KEY,
        "X" INT NOT NULL,
        "Y" INT NOT NULL
        );
'''

INSERT_INTO_TABLE = '''
    INSERT INTO demo
        ("S", "X", "Y")
    VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7);
'''

# if __name__ == '__main__':
#     execute_query(connection=connection, query=CREATE_TABLE)
#     execute_query(connection=connection, query=INSERT_INTO_TABLE)

row_count = execute_query(connection=connection, query='''
    SELECT COUNT(*)
    FROM demo;
''')

xy_at_least_5 = execute_query(connection=connection, query='''
    SELECT COUNT(*)
    FROM demo
    WHERE X >= 5 AND Y >= 5;
''')

unique_y = execute_query(connection=connection, query='''
    SELECT COUNT(DISTINCT Y)
    FROM demo;
''')

print(row_count)
print(xy_at_least_5)
print(unique_y)
