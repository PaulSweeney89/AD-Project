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

