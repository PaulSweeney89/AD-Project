import program_mysql
from tabulate import tabulate

def get_id():
	return input("ID : ")

def get_countryname():
	name = input("Name : ")
	if name == "":
		get_countryname()
	return name

def main():
	"""
	Main Python Program
	"""
	app_display()

	while True:
		choice = input("Choice: ")

		if (choice == "1"):
			print("Films")
			print("-" * 5)

			# output of get.films() query
			program_mysql.get_films()

		elif (choice == "2"):
			print("Actors")
			print("-" * 5)

			# Inputs
			year = input("Year of Birth: ")
			gender = input("Gender <Male/Female> :")

			print("Actors")
			print("-" * 5)
			try:
				actors = program_mysql.get_actor(year, gender)
				print(tabulate(actors, tablefmt="simple"))
			except:
				print("Error")
			
		elif (choice == "3"):
			print("Studios")
			print("-" * 5)

			# output of get.studios() query
			studio = program_mysql.get_studios()
			print(tabulate(studio, tablefmt="simple"))

		elif (choice == "4"):
			print("Add New Country")
			print("-" * 14)

			#inputs
			while True:
				try:
					ID = int(get_id())
					name = get_countryname()
					program_mysql.add_country(ID, name)
				except:
					print("")

		elif (choice == "x"):
			# Exit Application
			print()
			break;



def app_display():
	"""
	Python Program Display Options
	"""
	print("Movies DB")
	print("-" * 9)
	print("")
	print("MENU")
	print("=" * 4)
	print("1 - View Films")
	print("2 - View Actors by Year of Birth & Gender")
	print("3 - View Studios")
	print("4 - Add New Country")
	print("5 - View Movie with Subtitles")
	print("6 - Add New MovieScript")
	print("x - Exit application")




if __name__ == "__main__": 
	main()