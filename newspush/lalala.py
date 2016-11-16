import os
import json
import shlex
import traceback
import subprocess
from django.db import models

# run rhe jar files to get sources
def runjar(input):
	cmd = "java -jar notice_crawler-assembly-0.1.jar"
	p = subprocess.Popen(shlex.split(cmd),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	out, err = p.communicate(input.encode('gbk'))
	# print(out.decode('gbk'))
	return out.decode('gbk')

def getdata():
	# get listsources
	path = os.path.abspath('..') 
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
		# check it is news or notice
		if select.find("通知") != -1:
			category = "Notice"
		elif select.find("新闻") != -1:
			category = "News"
		else:
			continue
		# get news or notices by running jar files
		cmd = """{"type":"getnews","source":\""""+select+"\"}"
		g = runjar(cmd)
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

if __name__ == '__main__':
	getdata()