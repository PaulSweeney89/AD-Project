import program_mysql
import program_mongo
from tabulate import tabulate



def get_year():
	"""Function to prompt user to input Actor DOB (year) input"""
	while True:
		try:
			y = int(input("Year of Birth: "))
		except:
			print("Please enter a valid year")
		else:
			return y



def get_gender():
	""" Function to prompt user to input Actor gender """
	while True:
		try:
			g = input("Gender <Male/Female>:")
			if g not in {"Male", "Female", ""}:
				raise Exception
		except Exception:
			print("Please enter Gender <Male/Female>")
		else:
			return g



def get_id():
	"""Function to prompt user to input Country / Film ID number """
	while True:
		try:
			ID = int(input("ID : "))
		except:
			print("Please enter a valid ID")
		else:
			return ID 



def get_countryname():
	"""Function to prompt user to input Country name """
	while True:
		try:
			name = input("Name : ")
			if name == "":
				raise Exception
		except Exception:
			print("Please enter a valid Country name")
		else:
			return name



def get_lang():
	""" Function to prompt user to input subtitle language """
	while True:
		try:
			lang = input("Enter Subtitle language : ")
			if lang == "":
				raise Exception
		except Exception:
			print("Please enter a valid Subtitle Language")
		else:
			return lang



def get_keywords():
	""" Function to prompt user to input movie script keywords """
	while True:
			key_words = []
			word = input("Keyword <-1 to end> : ")
			key_words.append(word)
			
			if word == "-1":
				break

	return key_words



def get_sublang():
	""" Function to prompt user to input movie script subtitle Language """
	while True:
			sub_lang = []
			lang = input("Subtitle Language <-1 to end> : ")
			sub_lang.append(lang)
			
			if lang == "-1":
				break

	return sub_lang



def main():
	"""
	Main Python Program
	"""
	app_display()

	while True:
		choice = input("Choice: ")

		# Choice 1 - View Films	
		if (choice == "1"):											
			print("Films")									# Print Heading Text
			print("-" * 5)

			program_mysql.get_films()						# Call get_films() function		
			app_display()									# re-Display Main Menu

		# Choice 2 - View Actors by Year of Birth & Gender
		elif (choice == "2"):								
			print("Actors")									# Print Heading Text
			print("-" * 5)

			year = get_year()								# Call input functions & assign to variables
			gender = get_gender()							# Actor year & Actor gender

			print("\n")										# Print Heading Text
			print("Actors")
			print("-" * 5)

			actors = program_mysql.get_actor(year, gender)	# Call get_actor() function
			print(tabulate(actors, tablefmt="simple"))		# Display results using tabulate
			app_display()									# re-Display Main Menu

		# Choice 3 - View Studios
		elif (choice == "3"):								
			print("Studios")								# Print Heading Text
			print("-" * 5)

			studio = program_mysql.get_studios()			# Call get_studio() function
			print(tabulate(studio, tablefmt="simple"))		# Display results using tabulate
			app_display()									# re-Display Main Menu

		# Choice 4 - Add New Country
		elif (choice == "4"):								
			print("Add New Country")						# Print Heading Text
			print("-" * 14)

			ID = int(get_id())								# Call input functions & assign to variables
			name = get_countryname()						# Country ID & Country Name
			
			program_mysql.add_country(ID, name)				# Call add_country() function
			app_display()									# re-Display Main Menu

		# Choice 5 - View Movies with Subtitles
		elif (choice == "5"):								
			print("View Movie with Subtitles")				# Print Heading Text
			print("-" * 14)

			language = get_lang()							# Call input function get_lang()
			
			subs = program_mongo.get_subs(language)			# Call get_subs() function for input language
			
			id_list = []									# Loop through "_id" values from get_subs()
			for s in subs:									# and append to id_list
				id_list.append(s["_id"])
			
			print("\n")										# Print Heading Text
			print("Movies with ", language, "subtitles")
			print("-" * 29)

			synopsis = program_mysql.get_filmsyn(id_list)	# Call get_filmsys()
			print(tabulate(synopsis, tablefmt="simple"))	# Display results using tabulate

		# Choice 6 - Add New MovieScript
		elif (choice == "6"):
			print("Add New Movie Script")					# Print Heading Text
			print("-" * 20)

			print(get_keywords())
			print(get_sublang())


		# Choice x - Close Program
		elif (choice == "x"):
			# Exit Application
			print("Close Program")
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