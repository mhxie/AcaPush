from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from newspush.models import News, NewsComment, StudentInfo
from newspush.forms import CommentForm, LoginForm
from django.core.exceptions import ValidationError, OperationalError
from django.core import serializers
import requests
import json
# Create your views here.

def commit_comment(request, news_id, stu_id):
    try:
        news_ = News.objects.get(id=news_id)
        student_ = StudentInfo.objects.get(studentID=stu_id)
    except OperationalError:
        return HttpResponseNotFound
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save(for_news=news_, for_stu_info=student_)
            html = "<html><body>Comment succeed.</body></html>"
            return HttpResponse(html)

def fetch_comments(request, news_id):
    try:
        news_ = News.objects.get(id=news_id)
    except OperationalError:
        return HttpResponseNotFound
    returned_comments = NewsComment.objects.filter(news=news_)
    response_data = serializers.serialize('json', returned_comments)
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def login(request):
    if request.method = 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponseNotFound
        form_data = form.data
        post_data = {
            'zjh': form_data['scu_id'],
            'mm': form_data['password'],
        }
        s = requests.Session()
        r = s.post('http://202.115.47.141/loginAction.do', data=post_data)
        if r.ok:
            r = s.get('http://202.115.47.141/menu/s_top.jsp')
            if r.ok:
                stu_name = '你的名字' # 需要从中提取姓名
                stu = StudentInfo(studentID=form_data['scu_id'])
                stu.nickname = form_data['nickname']
                stu.name = stu_name
                stu.save()
                html = "<html><body>This guy's name is %s.</body></html>" % stu_name
                return HttpResponse(html)
            else:
                raise HttpResponseNotFound
        else:
            raise HttpResponseForbidden

def fetch_news(request,aca_id,d):
    aca_id=request.GET['aca_id']
    d=request.GET['d']
    
    try:
        response_data=serializers.serialize("json",News.objects.filter(academy=aca_id,date<=d)
    except OperationalError:
        return HttpResponseNotFound
                                        
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def fetch_notice(request,aca_id,d):
    aca_id=request.GET['aca_id']
    d=request.GET['d']
    
    try:
        response_data=serializers.serialize("json",Notice.objects.filter(academy=aca_id,date<=d)
    except OperationalError:
        return HttpResponseNotFound
                                        
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def search(request,flag,keyword,aca_id,d):
    flag=request.GET['flag']
    keyword=request.GET['keyword']                                    
    aca=request.GET['academy']
    d=request.GET['date']

    if flag==0  #news                              
    try:
        response_data=serializers.serialize("json",News.objects.filter(academy=aca_id,date<=d)
    except OperationalError:
        return HttpResponseNotFound
                                        
    return HttpResponse(json.dumps(response_data),content_type="application/json")

    else if flag==1  #notice
    try:
        response_data=serializers.serialize("json",Notice.objects.filter(academy=aca_id,date<=d)
    except OperationalError:
        return HttpResponseNotFound
                                        
    return HttpResponse(json.dumps(response_data),content_type="application/json")

# To-Do
# 1. 完成视图测试
# 2. 完成名字提取
# 3. 注意中文编码
