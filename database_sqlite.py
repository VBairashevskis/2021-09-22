import sqlite3

with sqlite3.connect("my_db_test") as con:  # create file
    cur = con.cursor()  # Cursor

    cur.execute(""" DROP TABLE IF EXISTS myteam """)
    cur.execute(""" CREATE TABLE IF NOT EXISTS myteam (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT,
        phone INTEGER,
        mail TEXT
     )""")

    cur.execute(""" INSERT INTO myteam (name, position, phone, mail) 
    VALUES ('Valerijs', 'CEO', 20202020, 'vb@ml.lv'),
    ('Mihails', 'Project Manager', 20304050, 'mh@ml.lv'),
    ('Janis', 'Developer', +37120202020, 'vb@ml.lv');
     """)