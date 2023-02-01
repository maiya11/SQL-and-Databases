CREATE_NEW_TABLE = '''
    CREATE TABLE IF NOT EXISTS another_test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country" VARCHAR(200) NOT NULL);
    '''

INSERT_NEW_ROW = '''
    INSERT INTO another_test_table
        ("name", "age", "country")
    VALUES ('Kory', 31, 'USA');

    '''

DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table;
    '''

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "experience" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''

INSERT_RYAN = '''
    INSERT INTO characters (
        "name", "level", "experience", "hp", "strength", "intelligence", "dexterity", "wisdom"
    )
    VALUES (
        'Ryan', 50, 100, 1000, 9000, 4, -5, 12
    );
'''

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS characters;
    '''
