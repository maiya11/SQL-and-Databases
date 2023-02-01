import psycopg2
from data import USER, PASSWORD

# Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname='playground', user=USER,
                              password=PASSWORD, host='kashin.db.elephantsql.com')

# A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()

# An example query
cursor.execute('SELECT * FROM test_table;')
cursor.fetchone()
