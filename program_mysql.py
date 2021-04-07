import pymysql
import tabulate

conn = None

def connect():
	global conn
	conn = pymysql.connect(host="localhost", user="root", password="root", db="MoviesDB", cursorclass=pymysql.cursors.DictCursor, port=3306)



def get_films():
	"""
	Function to view films & actors
	"""
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

		while True:
			rows = cursor.fetchmany(5)
			for row in rows:
				print(row["FilmName"], " : ", row["ActorName"])
			quit = input("-- Quit <q> --")
			if quit == "q":
				break



def get_actor(year, gender):
	"""
	Function to view actor, month of birth & gender
	"""
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



def get_studios():
	"""
	Function to view studios
	"""
	if (not conn):
		connect();

	query = "SELECT * FROM Studio ORDER BY StudioID;"

	with conn:
		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()
		result = cursor.fetchall()

		return result



def add_country(ID, name):
	"""
	Function to add a new country
	"""
	if (not conn):
		connect();

	query = """ INSERT INTO Country
				(CountryID, CountryName)
				VALUES (%s, %s)
			"""

	with conn:
		try:
			cursor = conn.cursor()
			cursor.execute(query, (ID, name))
			conn.commit()
			print("Country:", ID, name, "added to database")
		except pymysql.err.IntegrityError:
			print("*** Error ***: ID and/or Name <", ID, ",", name, "already exists")