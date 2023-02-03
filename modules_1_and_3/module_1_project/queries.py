NUM_ROWS = '''
SELECT  COUNT(*)
FROM    review;
'''

NUM_USERS = '''
SELECT	COUNT(*)
FROM	review
WHERE	Nature >= 100 AND Shopping >= 100;
'''

AVERAGES = '''
SELECT	AVG(Sports) AS avg_sports,
	AVG(Religious) AS avg_religious,
	AVG(Nature) AS avg_nature,
	AVG(Theatre) AS avg_theatre,
	AVG(Shopping) AS avg_shopping,
	AVG(Picnic) AS avg_picnic
FROM review;
'''

QUERY_LIST = [NUM_ROWS, NUM_USERS, AVERAGES]
