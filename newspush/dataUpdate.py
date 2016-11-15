import os
import json
import shlex
import traceback
import subprocess
from django.db import models



# insert news or noice json file
def data_insert(data):
	# get information
	try:
		#data = open(data_name)
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
	path = os.path.abspath('..')+"/src"
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
		f = open(file_path + "/" + str(ID) + ".json","a+")
	except Exception as e:
		traceback.print_exc()
		return
	else:
		f.write(content)
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
def init_academy():
	path = os.path.abspath('..') 
	data = open(path+"/src/academy.json");
	try:
		data = open(data_name)
		s = json.load(data)
	except Exception as e:
		traceback.print_exc()
		return
	else:
		lenth = len(s["academy"])
		for i in range(0,lenth):
#			code = s["academy"][i]["code"]
			name = s["academy"][i]["name"]
			address = s["academy"][i]["address"]
			models.Academy.objects.create(name=name,address=address)
	data.close()

# run rhe jar files to get sources
def runjar(input):
	cmd = "java -jar notice_crawler-assembly-0.1.jar"
	p = subprocess.Popen(shlex.split(cmd),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	out, err = p.communicate(input.encode('gbk'))
	# print(out.decode('gbk'))
	return out.decode('gbk')

# use listsources commend to update listsources
def listsources():
	cmd = """{"type":"listsources"}"""
	content = runjar(cmd)
	path = os.path.abspath('..')
	f = open(path+"/src/listsources.json","w")
	f.write(content)
	f.close()
	# print(content)

# use getnews commend to get information
# sava them into file system
# not completeds
def getdata():
	def getdata():
	path = os.path.abspath('..') 
	file = open(path+"/src/listsources.json");
	li = open(file)
	s = json.load(li)	
	length1 = len(s["sources"])

	for i in range(0, length1):
		academy = s["sources"][i][school]
		select = s["sources"][i][name]
		cmd = """{"type":"getnews","source":\""""+select+"\"}"
		get = runjar(cmd)
		
		length2 = len(get["result"][0]["news"])
		if select.find("通知") != -1:
			category = "notice";
		if select.find("新闻") != -1:
			category = "news"
		for i in range(0,length2):
			# create a json file
			info = {}
			info["originURL"] = s["result"][0]["news"][i]["url"]
			info["title"] = s["result"][0]["news"][i]["title"]
			info["content"] = s["result"][0]["news"][i]["content"]
			info["time"] = s["result"][0]["news"][i]["date"]
			info["academy"] = academy
			info["category"] = category
			# inset into database
			data_insert(info)
