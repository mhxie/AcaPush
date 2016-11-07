from django.shortcuts import render

# Create your views here.

def commit_comment(request, news_id):
    news_ = news.objects.get(id=news_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            newsComment.objects.create(
                
            )

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
    
