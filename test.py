# def get_id():
# 	try:
# 		ID = int(input("ID : "))
# 	except:
# 		print("Enter Valid ID")
# 		get_id()

# def get_countryname():
# 	name = input("Name : ")
# 	if name == "":
# 		get_countryname()
# 	return name

# validate_inputs = True
# while validate_inputs:
# 	ID = get_id()
# 	name = get_countryname()
	
# 	validate_inputs = False


import pymysql


# def get_id():
# 	try:
# 		ID = int(input("ID : "))
# 	except:
# 		get_id()
# 	return ID 

# def get_countryname():
# 	name = input("Name : ")
# 	if name == "":
# 		get_countryname()
# 	return name

# def get_year():
# 	while True:
# 		try:
# 			y = int(input("Year of Birth: "))
# 		except:
# 			print("Please enter a valid year")
# 		else:
# 			return y

# def get_gender():
# 	while True:
# 		try:
# 			g = input("Gender <Male/Female>:")
# 			if g not in {"Male", "Female", ""}:
# 				raise Exception
# 		except Exception:
# 			print("Please enter Gender <Male/Female>")
# 		else:
# 			return g

# #print(get_year())

# print(get_gender())



def get_actor(year, gender):
	"""
	Function to view actor, month of birth & gender
	"""
	db = pymysql.connect(host="localhost", user="root", password="root", db="MoviesDB", cursorclass=pymysql.cursors.DictCursor, port=3306)

	query = """	SELECT ActorName, MONTHNAME(ActorDOB), ActorGender
					FROM Actor
				WHERE YEAR(ActorDOB) = %s AND ActorGender = ISNULL(%s, %s);
			"""

	with db:
		cursor = db.cursor()
		cursor.execute(query, (year, gender))			#re-enter variables in here!
		db.commit()
		result = cursor.fetchall()

		for row in result:

			print(row["ActorName"], " : ", row["ActorGender"])
		return gender

		#if gender == "Male":
		#	for row in result:
		#		print(i["Name"], " : ", i["Month"], " : ", i["Gender"] == "Male")

x = get_actor(1960, "Male")

print(x)