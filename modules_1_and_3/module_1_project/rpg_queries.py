TOTAL_CHARACTERS = '''
SELECT	COUNT(*) AS total_characters
FROM	charactercreator_character;
'''

TOTAL_SUBCLASS = '''
SELECT	(
	SELECT COUNT(*)
	FROM charactercreator_cleric
	) AS count_cleric,
	(
	SELECT COUNT(*)
	FROM charactercreator_fighter
	) AS count_fighter,
	(
	SELECT COUNT(*)
	FROM charactercreator_mage
	) AS count_mage,
	(SELECT COUNT(*)
	FROM charactercreator_thief
	) AS count_thief;
'''

TOTAL_ITEMS = '''
SELECT  COUNT(DISTINCT item_id) as num_items
FROM    charactercreator_character_inventory;
'''

WEAPONS = '''
SELECT	COUNT(*) AS num_weapons
FROM	armory_weapon;
'''

NON_WEAPONS = '''
SELECT	COUNT(*) AS non_weapons
FROM	armory_item
WHERE	NOT EXISTS(
	    SELECT * 
	    FROM armory_weapon 
	    WHERE armory_weapon.item_ptr_id = armory_item.item_id);
'''

CHARACTER_ITEMS = '''
SELECT	character_id, 
	    COUNT(item_id) AS num_items
FROM	charactercreator_character_inventory
GROUP	BY character_id
LIMIT	20;
'''

CHARACTER_WEAPONS = '''
SELECT	    cc_inv.character_id, 
	        COUNT(aw.item_ptr_id) AS num_weapons
FROM	    armory_weapon AS aw
LEFT JOIN	armory_item AS ai
ON	        aw.item_ptr_id = ai.item_id
LEFT JOIN	charactercreator_character_inventory as cc_inv
ON	        cc_inv.item_id = ai.item_id
GROUP	    BY cc_inv.character_id
LIMIT	    20;
'''

AVG_CHARACTER_ITEMS = '''
SELECT	AVG(num_items)
FROM
    (
	SELECT	character_id, 
		    COUNT(item_id) AS num_items
	FROM	charactercreator_character_inventory
	GROUP	BY character_id
    )
AS avg_num_items;
'''

AVG_CHARACTER_WEAPONS = '''
SELECT	AVG(num_weapons)
FROM (
	SELECT	    cc_inv.character_id, COUNT(aw.item_ptr_id) AS num_weapons
	FROM	    armory_weapon AS aw
	LEFT JOIN	armory_item AS ai
	ON 	        aw.item_ptr_id = ai.item_id
	LEFT JOIN	charactercreator_character_inventory AS cc_inv
	ON	        ai.item_id = cc_inv.item_id
	GROUP	    BY cc_inv.character_id)
AS	avg_num_weapons;
'''
