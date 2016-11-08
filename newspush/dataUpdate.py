import os
import json
import traceback
from django.db import models


# it ought to be a json file 
def data_update(data_name):
	# get information
	try:
		data = open(data_name)
		s = json.load(data)
		academy = s["academy"]
		title = s["title"]
		time = s["time"]
		originURL = s["originURL"]
		category = s["category"]
		content = s["content"]
	except Exception as e:
		traceback.print_exc()
		return

	# create dir, we will do this in the begining
	table = category
	path = "D:/Resourses"
	#os.makedirs(path)

	# insert information into database
	if table=="news":
		file_path = path + "/News"
		try:
			models.News.objects.create(academy=academy,title=title,time=time,sourceURL=file_path_name,originURL=originURL)
		except Exception as e:
			traceback.print_exc()
			return
		try:
			ID = models.News.objects.get(originURL=originURL)
		except Exception as e:
			traceback.print_exc()
			return
		
	elif table=="notice":
		file_path = path + "/Notice"
		try:
			models.Notice.objects.create(academy=academy,title=title,time=time,sourceURL=file_path_name,originURL=originURL,) 
		except Exception as e:
			traceback.print_exc()
			return
		try:	
			ID = models.notice.objects.get(originURL=originURL)
		except Exception as e:
			traceback.print_exc()
			return

	# save the information to file system
	try:
		f = open(file_path + "/" + ID + ".txt","a+")
	except Exception as e:
		traceback.print_exc()
		return
	else:
		f.write(data)
		f.close()
	data.close()
			
