# Step 0 - import sqlite3
import sqlite3
import queries as q

# Step 1 - connect to database
connection = sqlite3.connect('rpg_db.sqlite3')

# Step 2 - make the "cursor" - an intermediary to access the database
cursor = connection.cursor()

# Step 3 - write a query
# (see queries.py file)

# Step 4 - execute the query on the cursor and fetch the results
# "pulling the results from the cursor"
cursor.execute(q.SELECT_ALL)
results = cursor.fetchall()

if __name__ == '__main__':
    print(results[:5])
