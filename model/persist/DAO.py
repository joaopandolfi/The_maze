import sqlite3

class Dao:
	def saveOnDb(self, name):
		conn = sqlite3.connect('data/db/maze.db')
		cursor = conn.cursor()
		sql = 'CREATE TABLE IF NOT EXISTS saves (name TEXT PRIMARY KEY, mapObj TEXT, playerObj TEXT)'
		cursor.execute(sql)
		
		try:
			sql = 'INSERT INTO saves (name, mapObj, playerObj) VALUES (?, ?, ?)'
			cursor.execute(sql, (name, 'none', 'none'))
			conn.commit()
			conn.close()
		except sqlite3.IntegrityError:
			return

	def saveGame(self, name, obj):
		conn = sqlite3.connect('data/db/maze.db')
		cursor = conn.cursor()		
		sql = 'UPDATE saves SET name = ?, mapObj = ?, playerObj = ? WHERE name = \"' + name + '\"'
		cursor.execute(sql, (name, obj.mapObj, obj.playerObj))
		conn.commit()
		conn.close()

	def getSaveByName(self, name):
		conn = sqlite3.connect('data/db/maze.db')
		cursor = conn.cursor()
		sql = 'SELECT * FROM saves WHERE name = \"' + name + '\"'
		cursor.execute(sql)

		for line in cursor.fetchall():
			return line

		conn.close()

	def viewDb(self):	# debug function
		conn = sqlite3.connect('data/db/maze.db')
		cursor = conn.cursor()
		sql = 'SELECT name, playerObj FROM saves'
		cursor.execute(sql)

		for line in cursor.fetchall():
			print(line)

		conn.close()