import program_mysql
from tabulate import tabulate

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
			films = (program_mysql.get_films())
			print(tabulate(films[:5], tablefmt="simple"))

		elif (choice == "2"):
			print("Actors")
			print("-" * 5)

			# Inputs
			year = int(input("Year of Birth: "))
			gender = str(input("Gender <Male/Female>: "))

			actors = program_mysql.get_actor(year, gender)
			print(tabulate(actors))
			
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