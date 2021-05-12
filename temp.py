import sqlite3
from contextlib import closing
connection=sqlite3.connect("project.db")
cursor=connection.cursor()
#cursor.execute("INSERT INTO fish VALUES('shark','zig',1)")
#connection.commit()
print(cursor.execute("select * from logs").fetchall())
with closing(sqlite3.connect("project.db")) as connection:
	with closing(connection.cursor()) as cursor:
		pass
