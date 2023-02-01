CREATE_TYPE_SEX = '''
    CREATE TYPE SEX AS ENUM ('male', 'female')
'''

CREATE_TYPE_CLASS = '''
    CREATE TYPE CLASS AS ENUM ('1', '2', '3')
'''
DROP_TITANIC_TABLE = '''
    DROP TABLE IF EXISTS titanic
'''

CREATE_TITANIC_TABLE = '''
    CREATE TABLE IF NOT EXISTS titanic
    (
        "id" SERIAL NOT NULL PRIMARY KEY,
        "name" VARCHAR(100) NOT NULL,
        "sex" SEX NOT NULL,
        "age" FLOAT NOT NULL,
        "fare" FLOAT NOT NULL,
        "siblings_spouses_aboard" INT NOT NULL,
        "parents_children_aboard" INT NOT NULL,
        "passenger_class" CLASS NOT NULL,
        "survived" BOOLEAN NOT NULL
    );
'''

INITIAL_QUERIES_LIST = [DROP_TITANIC_TABLE, CREATE_TITANIC_TABLE]
