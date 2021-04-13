import pymongo

myclient = None

def connect():
	global myclient
	myclient = pymongo.MongoClient(host="localhost", port=27017)
	myclient.admin.command("ismaster")



def get_subs(lang):
	"""
	Function to return details of Input Subtitle Language 
	"""
	if (not myclient):
		try:
			connect()
		except Exception as e:
			print("Error", e)

	db = myclient["movieScriptsDB"]
	docs = db["movieScripts"]

	query = {"subtitles":lang}

	result = docs.find(query, (lang))
	return result



def insert_script(id_num, key_words, sub_lang):
	"""
	Function to insert new movie script into movieScriptDB
	"""
	if (not myclient):
		try:
			connect()
		except Exception as e:
			print("Error", e)

	db = myclient["movieScriptsDB"]
	docs = db["movieScripts"]

	new_script = [{"_id":id_num, "keywords":key_words, "subtitles":sub_lang}]

	try:
		docs.insert(new_script, (id_num, key_words, sub_lang))
		print("MovieScript:", id_num, "added to database")
	#except pymongo.errors.BulkWriteError as e:
		#print("*** ERROR ***: Film with id:", id_num, "does not exist in moviesDB")
	except pymongo.errors.DuplicateKeyError as e:
		print("*** ERROR ***: Movie Script with id:", id_num, "already exists")
	except Exception as e:
		print("Error:", e)