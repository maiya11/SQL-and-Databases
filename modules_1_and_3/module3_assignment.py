from mongo import mongo_connect
from sqlite_example import connect_to_db, execute_query
import queries as q
import pymongo

if __name__ == '__main__':
    sl_conn = connect_to_db()
    sl_characters = execute_query(sl_conn, q.GET_CHARACTERS)

    collection = mongo_connect()

    for character in sl_characters:
        doc = {
            'character_id': character[0],
            'name': character[1],
            'level': character[2],
            'exp': character[3],
            'hp': character[4],
            'strength': character[5],
            'intelligence': character[6],
            'dexterity': character[7],
            'wisdom': character[8]
        }

        collection.insert_one(doc)
