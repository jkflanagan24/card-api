import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()


# TODO WE CAN DELETE THIS
def make_test_table():
    sql = """
    CREATE TABLE articles 
    (
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT
    );
    INSERT INTO articles VALUES (1, 'SQLite Tutorial', 'Content here…');
    INSERT INTO articles VALUES (2, 'Python SQLite Guide', 'Content here…');
    """
    cur.executescript(sql)
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()


