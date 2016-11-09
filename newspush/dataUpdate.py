import os
import json
import traceback
from django.db import models



# insert news or noice json file
def data_insert(data_name):
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
			ID = models.News.objects.get(originURL=originURL).id()
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
		f = open(file_path + "/" + str(ID) + ".txt","a+")
	except Exception as e:
		traceback.print_exc()
		return
	else:
		f.write(data)
		f.close()
	data.close()


# insert news comment json file
def comment_indert(data_name):
	# get information
	try:
		data = open(data_name)
		s = json.load(data)
		news = s["news"]
		studentInfo = s["studentInfo"]
		content = s["content"]
		ip = s["ip"]
	except Exception as e:
		traceback.print_exc()
		return

	# insert news comment into database
	try:
		models.NewsComment.objects.create(news=news,studentInfo=studentInfo,content=content,time=time,ip=ip)
	except Exception as e:
		traceback.print_exc()
		return
	data.close()

# init academy json file
def init_academy(data_name):
	try:
		data = open(data_name)
		s = json.load(data)
	except Exception as e:
		traceback.print_exc()
		return
	else:
		len = len(s["academy"])
		for i in range(0,len):
			code = s["academy"][i]["code"]
			name = s["academy"][i]["name"]
			address = s["academy"][i]["address"]
			models.Academy.objects.create(code=code,name=name,address=address)
	data.close()
