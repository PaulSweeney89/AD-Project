
#gender = input("Gender <Male/Female> :")

#while gender not in {"Male", "Female", ""}:
	#print("Please enter Gender <Male/Female>")
	#gender = input("Gender <Male/Female> :")


def get_id():
	try:
		ID = int(input("ID : "))
	except:
		print("Enter Valid ID")
		get_id()

def get_countryname():
	name = input("Name : ")
	if name == "":
		get_countryname()
	return name

validate_inputs = True
while validate_inputs:
	ID = get_id()
	name = get_countryname()
	
	validate_inputs = False





def get_id():
	try:
		ID = int(input("ID : "))
	except:
		get_id()
	return ID 

def get_countryname():
	name = input("Name : ")
	if name == "":
		get_countryname()
	return name

