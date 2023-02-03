from data import DBNAME, PASSWORD
from sqlite_example import connect_to_db, execute_query
import queries as q
import pymongo
import certifi

# how request comes back from sqlite
test_characters = [(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),
                   (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)]

# how data will be stored in MongoDB
character_documents = [
    {
        'character_id': 1,
        'name': 'Aliquid iste optio reiciendi',
        'level': 0,
        'exp': 0,
        'hp': 10,
        'strength': 1,
        'intelligence': 1,
        'dexterity': 1,
        'wisdom': 1
    },
    {
        'character_id': 1,
        'name': 'Optio dolorem ex a',
        'level': 0,
        'exp': 0,
        'hp': 10,
        'strength': 1,
        'intelligence': 1,
        'dexterity': 1,
        'wisdom': 1
    }
]


def mongo_connect(password=PASSWORD, dbname=DBNAME, collection_name='characters'):
    client = pymongo.MongoClient(
        f'mongodb+srv://maiya:{password}@cluster0.ysaihyc.mongodb.net/{dbname}?retryWrites=true&w=majority',
        tlsCAFile=certifi.where())
    db = client[dbname]
    collection = db[collection_name]
    return collection


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
