from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from newspush.models import News, NewsComment, StudentInfo
from newspush.forms import CommentForm, LoginForm
from django.core.exceptions import ValidationError
import requests
# Create your views here.

def commit_comment(request, news_id):
    news_ = News.objects.get(id=news_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            newsComment.objects.create(

            )

def login(request):
    if request.method = 'POST':
        form = LoginForm(request.POST)
        try:
            form_data = form.cleaned_data
        except ValidationError:
            return HttpResponseNotFound
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

def fetch_news(request):
    new_id=request.GET['news_id']
    response_data=serializers.serialize("json",news.objects.filter(id=news_id)
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def fetch_notice(request):
    notice_id=request.GET['notice_id']
    response_data=serializers.serialize("json",notice.objects.filter(id=notice_id)
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def search_news(request):
    aca=request.GET['academy']
    d=request.GET['date']
    response_data=serializers.serialize("json",news.objects.filter(academy=aca,date<=d)
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def search_notice(request):
    aca=request.GET['academy']
    d=request.GET['date']
    response_data=serializers.serialize("json",notice.objects.filter(academy=aca,date<=d)
    return HttpResponse(json.dumps(response_data),content_type="application/json")
