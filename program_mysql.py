import pymysql

conn = None

def connect():
	global conn
	conn = pymysql.connect(host="localhost", user="root", password="root", db="MoviesDB", cursorclass=pymysql.cursors.DictCursor, port=3306)

def get_films():
	if (not conn):
		connect();

	query = """	SELECT f.FilmName, a.ActorName
    				FROM Film f
				INNER JOIN FilmCast fc
    				ON f.FilmID = fc.CastFilmID
				INNER JOIN Actor a
    				ON fc.CastActorID = a.ActorID
				ORDER BY f.FilmName, a.ActorName;
			"""

	with conn:
		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()
		result = cursor.fetchall()

		return result

def get_actor(year, gender):
	if (not conn):
		connect();

	query = """	SELECT ActorName, MONTHNAME(ActorDOB), ActorGender
    				FROM Actor
				WHERE YEAR(ActorDOB) = %s AND ActorGender = %s;
			"""

	with conn:
		cursor = conn.cursor()
		cursor.execute(query, (year, gender))
		conn.commit()
		result = cursor.fetchall()

		return result