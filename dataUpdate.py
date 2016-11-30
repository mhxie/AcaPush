import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AcaPush.settings")
django.setup()

# import os
import json
import time
import shlex
import traceback
import subprocess
from newspush.models import *

# insert news or noice json file
def data_insert(data):
	# get information
	try:
		#data = open(data_name)
		# s = json.loads(data)
		s = data
		# print(s)
		academy = s["academy"]
		title = s["title"]
		time = s["time"]
		originURL = s["originURL"]
		category = s["category"]
		content = s["content"]
	except Exception as e:
		traceback.print_exc()
		return

	time = '2016-11-19'
	# s = {}
	# originURL = "originURL"
	# title = "title"
	# content = "content"
	# time = "time"
	# academy = "academy"
	# category = "category"

	# create dir, we will do this in the begining
	table = category
	path = os.path.abspath('.')+"/src"
	#os.makedirs(path)

	file_path = ""
	ID = 0
	# insert information into database
	ac = Academy.objects.get(name=academy)

	if table=="News":
		dup = News.objects.filter(originURL=originURL)
		if(len(dup)!=0):
			print("this data exists now")
			return
		file_path = path + "/News"
		try:
			News.objects.create(academy=ac,title=title,time=time,sourceURL=file_path,originURL=originURL)
			print("succ insert into database news")
		except Exception as e:
			traceback.print_exc()
			return
		try:
			re = News.objects.filter(originURL=originURL)
			ID = re[0].id
			print("ID is "+str(ID))
		except Exception as e:
			traceback.print_exc()
			return

	elif table=="Notice":
		dup = Notice.objects.filter(originURL=originURL)
		if(len(dup)!=0):
			print("this data exists now")
			return
		file_path = path + "/Notice"
		try:
			Notice.objects.create(academy=ac,title=title,time=time,sourceURL=file_path,originURL=originURL,)
			print("succ insert into database notice")
		except Exception as e:
			traceback.print_exc()
			return
		try:
			re = Notice.objects.filter(originURL=originURL)
			ID = re[0].id
		except Exception as e:
			traceback.print_exc()
			return

	# save the information to file system
	try:
		print("file_path is "+file_path)
		f = open(file_path + "/" + str(ID) + ".json","w+")
	except Exception as e:
		traceback.print_exc()
		return
	else:
		f.write(str(data))
		f.close()
	# data.close()

# init academy json file
def init_academy():
	path = os.path.abspath('.')
	file_name = path+"/src/listsources.json"
	# file_name = "D:/resp/AcaPush/src/listsources.json"
	li = open(file_name)
	js = json.load(li)
	s = js["result"]
	# print(s)
	lenth = len(s["sources"])
	for i in range(0,lenth):
#		code = s["academy"][i]["code"]
		name = s["sources"][i]["school"]
		address = s["sources"][i]["index"]
		dup = Academy.objects.filter(name=name)
		if(len(dup)!=0):
			print("this data exists now")
			continue
		Academy.objects.create(name=name,address=address)
		print("insert academy "+name+"successfully!")
	li.close()

# run rhe jar files to get sources
def runjar(input):
	cmd = "java -jar notice_crawler-assembly-0.1.jar"
	p = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	out, err = p.communicate(input.encode())
	# print(out.decode('gbk'))
	return out.decode()

# use listsources commend to update listsources
def listsources():
	cmd = """{"type":"listsources"}"""
	content = runjar(cmd)
	path = os.path.abspath('.')
	f = open(path+"/src/listsources.json","w")
	f.write(content)
	f.close()
	# print(content)

# use getnews commend to get information
# sava them into file system
def getdata():
	# get listsources
	path = os.path.abspath('.')
	file_name = path+"/src/listsources.json"
	# file_name = "D:/resp/AcaPush/src/listsources.json"
	li = open(file_name)
	js = json.load(li)
	s = js["result"]
	# print(s)
	length1 = len(s["sources"])
	count = 0

	# get information for each element
	for i in range(0, length1):
		academy = s["sources"][i]["school"]
		select = s["sources"][i]["name"]
		print("select is "+select)
		# check it is news or notice
		if select.find("新闻") != -1:
			category = "News"
		elif select.find("通知") != -1:
			category = "Notice"
		else:
			continue
		# get news or notices by running jar files
		cmd = """{"type":"getnews","source":\""""+select+"\"}"
		print(cmd)
		g = runjar(cmd)
		# print("lalala "+g+" lalla")
		get = json.loads(g)
		if(get["type"] == "err"):
			print("err in getnews commend when get "+select)
			continue
		# save data
		length2 = len(get["result"]["news"])
		print("get "+str(length2)+" "+select+" successfully!")
		for i in range(0,length2):
			# create a json file
			info = {}
			info["originURL"] = get["result"]["news"][i]["url"]
			info["title"] = get["result"]["news"][i]["title"]
			info["content"] = get["result"]["news"][i]["html"]
			info["time"] = get["result"]["news"][i]["date"]
			info["academy"] = academy
			info["category"] = category
			# print("info is ")
			# print(info)
			data_insert(info)
			# # save test
			# file2_name = path+"/src/"+category+"/"+str(count)+".json"
			# # print(file2_name)
			# file2 = open(file2_name,"w")
			# file2.write(str(info))
			# file2.close()
			# count += 1
			#print(info)
			# inset into database

# update every 5 min
def timer(n):
    while True:
        getdata()
        time.sleep(n)

if __name__ == '__main__':
	t = 10*5
	timer(t)
