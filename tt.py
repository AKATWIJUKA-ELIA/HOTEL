import sqlite3

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()


cur.execute("DELETE FROM gold_products")
conn.commit()
conn.close()
